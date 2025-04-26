# Skysmart-Real-time-Flight-fare-and-time-Optimization
# Overview
This project is a smart, domestic flight booking platform that offers real-time fare and time optimization. It ensures users can:
- Search available flights dynamically
- Book tickets seamlessly
- Pay securely via Razorpay
- Receive instant downloadable invoices after booking

The system uses:
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **Automation**: RPA (Robotic Process Automation) for fetching flight data
- **Payment Gateway**: Razorpay Integration

---

# Features
- 🛫 Real-Time Flight Search and Optimization
- 🎯 Best Fare and Travel Time Recommendations
- 🧾 Instant Invoice Download After Payment
- 🔒 Secure Online Payments using Razorpay
- 🔄 Live Flight Data using RPA Automation
- 💻 Clean and Responsive UI

---

# Tech Stack
| Technology | Purpose |
|------------|---------|
| HTML, CSS, JS | Frontend development |
| Python Flask | Backend server & API |
| RPA Tools | Real-time data scraping and automation |
| Razorpay API | Payment processing |
| SQLite / MySQL | Database (optional for booking records) |

---

# Installation and Setup

1. **Clone the repository**:-----------

2.Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3.Install required packages:
pip install -r requirements.txt

4.Run the Flask app:
python app.py

5.Access the application: Open your browser and go to http://127.0.0.1:5000

#Folder Structure
/static         # CSS, JS files
/templates      # HTML Templates
/invoice        # Generated invoices
/app.py         # Main Flask application
/rpa_scraper.py # Script for live flight data
/requirements.txt


