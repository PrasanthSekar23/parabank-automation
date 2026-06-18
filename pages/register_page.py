"""
Register Page Object — covers the registration form and its validations.
"""
from pages.base_page import BasePage


class RegisterPage(BasePage):
    """
    Represents the ParaBank registration page (/register.htm).
    All input selectors use [name="..."] to avoid CSS dot-escaping issues.
    """

    # --- Personal Info Selectors ---
    FIRST_NAME = '[name="customer.firstName"]'
    LAST_NAME = '[name="customer.lastName"]'
    ADDRESS = '[name="customer.address.street"]'
    CITY = '[name="customer.address.city"]'
    STATE = '[name="customer.address.state"]'
    ZIP_CODE = '[name="customer.address.zipCode"]'
    PHONE = '[name="customer.phoneNumber"]'
    SSN = '[name="customer.ssn"]'

    # --- Account Credentials Selectors ---
    USERNAME = '[name="customer.username"]'
    PASSWORD = '[name="customer.password"]'
    CONFIRM_PASSWORD = '[name="repeatedPassword"]'

    # --- Action & Result Selectors ---
    REGISTER_BTN = '#customerForm input[type="submit"]'
    ERROR_SPANS = 'span.error'
    RIGHT_PANEL = '#rightPanel'
    SUCCESS_HEADING = '#rightPanel h1.title'

    def navigate_to_register(self) -> None:
        """Navigate directly to the registration page."""
        self.navigate("/register.htm")

    def fill_form(self, user_data: dict) -> None:
        """
        Fill all registration form fields from a user_data dictionary.
        Keys: first_name, last_name, address, city, state, zip_code,
              phone, ssn, username, password.
        """
        self.page.locator(self.FIRST_NAME).fill(user_data["first_name"])
        self.page.locator(self.LAST_NAME).fill(user_data["last_name"])
        self.page.locator(self.ADDRESS).fill(user_data["address"])
        self.page.locator(self.CITY).fill(user_data["city"])
        self.page.locator(self.STATE).fill(user_data["state"])
        self.page.locator(self.ZIP_CODE).fill(user_data["zip_code"])
        self.page.locator(self.PHONE).fill(user_data["phone"])
        self.page.locator(self.SSN).fill(user_data["ssn"])
        self.page.locator(self.USERNAME).fill(user_data["username"])
        self.page.locator(self.PASSWORD).fill(user_data["password"])
        self.page.locator(self.CONFIRM_PASSWORD).fill(user_data["password"])

    def submit_form(self) -> None:
        """Click the Register button and wait for the page to load."""
        self.page.locator(self.REGISTER_BTN).click()
        self.page.wait_for_load_state("networkidle")

    def get_validation_errors(self) -> list[str]:
        """Return a list of all visible validation error messages."""
        return self.page.locator(self.ERROR_SPANS).all_text_contents()

    def get_success_message(self) -> str:
        """Return the full text content of the right panel after registration."""
        return self.page.locator(self.RIGHT_PANEL).text_content().strip()

    def is_registration_successful(self) -> bool:
        """Return True when the post-registration heading contains 'Welcome'."""
        try:
            heading = self.page.locator(self.SUCCESS_HEADING).text_content()
            return "Welcome" in heading
        except Exception:
            return False
