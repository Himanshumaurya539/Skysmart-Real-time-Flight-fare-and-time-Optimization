from flask import Flask, render_template, request, redirect, session, flash, url_for, jsonify, send_from_directory
import pandas as pd
import os
from flask_mysqldb import MySQL
import MySQLdb.cursors
import bcrypt
import re
from flask_cors import CORS
import secrets
print(secrets.token_hex(32))  # Generates a strong 64-character key

app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Update with your DB user
app.config['MYSQL_PASSWORD'] = 'root'  # Update with your DB password
app.config['MYSQL_DB'] = 'skysmart_authentication'

mysql = MySQL(app)

# SECRET KEY for Sessions
app.secret_key = "de1daae9b2cfaf76f7937c6bec4a6a55ec7c6c5a5d6faa1de7a85449a85aa923"

### 🔹 SIGNUP ROUTE (Registers a new user) ###
from flask import jsonify

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # ✅ Handle empty fields
        if not name or not email or not password:
            flash('⚠ All fields are required!', 'warning')
            return redirect(url_for('signup'))

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        # ✅ Check if email is already registered
        if user:
            flash('❌ Email already registered!', 'danger')
            return redirect(url_for('signup'))

        # ✅ Hash password before storing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # ✅ Insert new user into database
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (name, email, hashed_password))
        mysql.connection.commit()
        cursor.close()

        flash('✅ Signup successful! Please log in.', 'success')
        return redirect(url_for('login'))  # Redirect to login after successful signup

    return render_template('signup.html')  # Always return template for GET requests


### 🔹 LOGIN ROUTE (Authenticates Users) ###
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            flash('⚠ Please fill in all fields!', 'warning')
            return redirect(url_for('login'))

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            session['loggedin'] = True
            session['id'] = user['id']
            session['name'] = user['name']
            flash(f'✅ Welcome, {session["name"]}!', 'success')
            return redirect(url_for('home'))  # Redirect to homepage after login
        else:
            flash('❌ Invalid email or password!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')  # Always return a response for GET requests



### 🔹 LOGOUT ROUTE (Clears User Session) ###
@app.route('/logout')
def logout():
    session.clear()
    flash("ℹ️ You have been logged out.", "info")
    return redirect(url_for('home'))







# Excel File Path
EXCEL_FILE_PATH = "D:\\STUDY MATERIALS\\final year project TYDS\\data s UIpath\\s_data.xlsx"

# Function to read Excel file safely and handle time serialization
def read_excel1():
    try:
        if os.path.exists(EXCEL_FILE_PATH):
            #print("Reading Excel File...")
            df = pd.read_excel(EXCEL_FILE_PATH)

            # Standardize column names
            df.columns = df.columns.str.strip().str.replace(" ", "_").str.upper()

            # Convert time columns (if they exist) to string format
            if 'DEPARTURE_TIME' in df.columns:
                df['DEPARTURE_TIME'] = df['DEPARTURE_TIME'].astype(str)
            if 'ARRIVAL_TIME' in df.columns:
                df['ARRIVAL_TIME'] = df['ARRIVAL_TIME'].astype(str)

            #print(df)  # Debugging: Check the data format
            return df.to_dict(orient="records")
        else:
            print("Error: Excel file not found!")
            return []
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return []

# Page Routes
@app.route('/index.html')

@app.route('/')
def home():
    print(session)
    if 'loggedin' in session:
        return render_template('index.html', name=session['name'])  # Pass user name if logged in
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/offers.html')
def offers():
    return render_template("offers.html")

@app.route('/hotels.html')
def hotels():
    return render_template("hotels.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/result.html')
def search_results():
    return render_template("result.html")

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/get_flights', methods=['GET'])
def get_flights():
    flights = read_excel1()
    return jsonify(flights)



if __name__ == '__main__':
    app.run(debug=True)
