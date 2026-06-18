# ParaBank Automation

BDD + POM test automation for [ParaBank](https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC) sign-up and login flow.

## Tech Stack

| Layer | Tool |
|-------|------|
| Language | Python 3.9+ |
| BDD Framework | [Behave](https://behave.readthedocs.io/) |
| Browser Automation | [Playwright for Python](https://playwright.dev/python/) |
| Design Pattern | Page Object Model (POM) |
| CI | GitHub Actions |

## Project Structure

```
parabank-automation/
├── features/               # BDD feature files (Gherkin)
│   ├── steps/              # Step definitions (one file per TC)
│   ├── environment.py      # Behave hooks (browser lifecycle)
│   └── tc00X_*.feature     # Feature files per test case
├── pages/                  # Page Object Model classes
│   ├── base_page.py
│   ├── home_page.py
│   ├── register_page.py
│   └── account_overview_page.py
├── utils/
│   └── test_data.py        # Dynamic test data generator
├── screenshots/            # Auto-saved screenshots on failure
├── reports/                # Test execution reports
└── .github/workflows/      # GitHub Actions CI
```

## Test Cases

| TC ID | Feature | Description | Priority |
|-------|---------|-------------|----------|
| TC_001 | Launch | Verify ParaBank website opens successfully | High |
| TC_002 | Registration | Register with valid details | High |
| TC_003 | Registration | Mandatory field validation (empty form) | Medium |
| TC_004 | Registration | Duplicate username validation | Medium |
| TC_005 | Login | Login with newly created account | High |
| TC_006 | Account Overview | Balance is visible post-login | High |
| TC_007 | Account Overview | Automation prints balance to logs | High |
| TC_008 | Logout | User can logout successfully | Medium |

## Setup

### Prerequisites
- Python 3.9+
- pip

### Install

```bash
pip install -r requirements.txt
playwright install chromium
```

## Running Tests

```bash
# Run all tests
behave

# Run a specific test case by tag
behave --tags=TC_001
behave --tags=TC_002
behave --tags=TC_005

# Run all registration tests
behave --tags=registration

# Run all login tests
behave --tags=login

# Run with verbose output
behave --no-capture

# Run and generate HTML report
behave -f html -o reports/report.html
```

## Test Data

Usernames are generated dynamically as `prasanth_<timestamp>` to ensure uniqueness on every run.  
Password: `password123`

## Author

**Prasanth Sekar**  
mailtoprasanthsekar@gmail.com
