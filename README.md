@'
This is an Automation testing project where I test the functionality of this specific website specific website

# UI Automation
**Stack:** Python · Playwright · Pytest  
**Website under test:** Demo Web Shop 
**Website URL:** https://demowebshop.tricentis.com/  
**Product under test:** Digital SLR Camera

---

## Setup

### 1. Open the project
Open the `Playwright-Phase4` folder in PyCharm.

### 2. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium

### 3 Create and activate the virtual environment(venv)

python -m venv .venv
.venv\Scripts\activate

### 4. File structure

Playwright-Phase4/
├── .venv/                         # Virtual environment
├── conftest.py                    # Shared fixtures and registration data 
├── pages/
│   ├── register_user.py           # Page Object – registration
│   ├── login_page.py              # Page Object – login / logout
│   └── checkout_page.py           # Page Object – product, cart, checkout
├   ├── base_page.py               
├── tests/
│   ├── test_01_register.py        # Part 1: Register unique user + logout
│   ├── test_02_login.py           # Part 2: Parameterized login (Valid & xfail)
│   └── test_03_checkout.py        # Part 3: Add to cart + full checkout
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
└── karabo_report.html             # Generated test report


--------------Test Data--------------

test_data = {
    "first_name": "Barbara",
    "last_name": "Gordon",
    "password": "Tosca1234!",
    "country": "Austria",
    "city": "Vienna",
    "address": "Vienna Street",
    "zip": "1234",
    "phone": "001122334455",
    "card_type": "Visa",
    "cardholder": "Barbara Gordon",
    "card_number": "4485564059489345",
    "expiry_month": "04",
    "expiry_year": "2030",
    "cvv": "123",
}

## 5 RUN COMMANDS

pytest test/test_01_register.py
pytest tests/    ---runs test scripts in order(01_register → 02_login → 03_checkout.)
pytest tests/ --html=karabo_report.html --self-contained-html


!!!!!!!!!!!!!!!!!!!!!  NB  !!!!!!!!!!!!!!!!!!!!!

test_02_login.py and test_03_checout.py do not run independently because they depend on test_01_register.py
