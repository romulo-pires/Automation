# Test Automation Project with Playwright (Python)

This project demonstrates API and UI test automation using Python, Playwright, and Pytest.

---

## Features

- API testing with Playwright
- UI automation (login and checkout flows)
- Reusable fixtures with Pytest
- Validation of status codes and response bodies
- Organized test structure

---

## Tech Stack

- Python
- Playwright
- Pytest

---

## Project Structure
automation/
│
├── pages/
│
├── tests/
│ ├── api/
│ ├── login/
│ ├── checkout/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── README.md
├── LEIA-ME.md

---

## Setup

1. Clone the repository:
    git clone https://github.com/romulo-pires/Automation.git
    cd Automation

2. Install dependencies
    pip install -r requirements.txt

3. Install Playwright
    playwright install
    
4. Run tests
    py -m pytest -s

---

## Notes
This project uses ReqRes API for learning purposes.