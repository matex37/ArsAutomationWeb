End-to-end UI automation project for a Appliance Repair services website.
Built with Playwright + Python, using Page Object Model (POM) and Allure reporting.

1. Project Overview

This project covers a full booking flow automation:

Postal code validation
Date selection (dynamic working days)
Customer information
Appliance details
Payment step
Final review

Includes both positive and negative test scenarios.

2. Key Features

✅ End-to-End booking flow
✅ Dynamic date selection (next working days)
✅ Stable selectors strategy
✅ iFrame handling
✅ Negative testing (invalid email, empty fields)
✅ Disabled button validation (CSS / aria / state)
✅ Page Object Model (clean & scalable structure)
✅ Allure reports with screenshots

3. Tech Stack
Playwright (Python)
Pytest
Allure Reports
POM (Page Object Model)

4. Project Structure

project/
│
├── tests/
│   ├── test_booking.py
│   ├── test_booking_invalid_email.py
│   ├── test_booking_empty_customer.py
│   └── test_navigation.py
│
├── pages/
│   ├── booking_page.py
│   └── navigation_page.py
│
├── utils/
│   └── data_loader.py
│
├── test_data/
│   └── booking_data.json
│
└── README.md

5.Installation

# Clone repository
git clone https://github.com/matex37/ArsAutomationWeb.git
cd ArsAutomationWeb

# Create virtual environment 
python -m venv venv

# Activate venv
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

6. Run Tests
pytest -v

7. Run with Allure
pytest --alluredir=allure-results
allure serve allure-results

8. Allure Report
The project includes detailed reporting:

Test steps
Screenshots on each step
Pass/Fail status
Debug-friendly logs

9. Test Scenarios

✅ Positive
Full booking flow (happy path)
Successful form submission
Navigation between pages
❌ Negative
Invalid email validation
Empty required fields
Disabled "Next" button behavior

10. Future Improvements
CI/CD integration (GitHub Actions)
Parallel execution
API testing integration
Visual regression testing
   

   
   

