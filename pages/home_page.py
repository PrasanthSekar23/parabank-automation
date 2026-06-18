"""
Home Page Object - covers the login panel and top-level navigation.
"""
from pages.base_page import BasePage


class HomePage(BasePage):
    """
    Represents the ParaBank homepage (index.htm).
    Contains the login form, register link, and logout link.
    """

    # --- Selectors ---
    USERNAME_INPUT = '[name="username"]'
    PASSWORD_INPUT = '[name="password"]'
    LOGIN_BTN = '#loginPanel input[type="submit"]'
    LOGIN_ERROR = '#rightPanel p.error'
    REGISTER_LINK = 'a[href*="register.htm"]'
    LOGOUT_LINK = 'a[href*="logout.htm"]'
    WELCOME_PANEL = '#leftPanel'
    WELCOME_TEXT = '#leftPanel p'
    LOGIN_PANEL = '#loginPanel'

    def navigate_to_home(self) -> None:
        """Open the ParaBank homepage with JDBC connection type."""
        self.navigate("/index.htm?ConnType=JDBC")

    def enter_username(self, username: str) -> None:
        """Type username into the login form."""
        self.page.locator(self.USERNAME_INPUT).fill(username)

    def enter_password(self, password: str) -> None:
        """Type password into the login form."""
        self.page.locator(self.PASSWORD_INPUT).fill(password)

    def click_login(self) -> None:
        """Click the Log In button and wait for navigation."""
        self.page.locator(self.LOGIN_BTN).click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    def login(self, username: str, password: str) -> None:
        """Fill credentials and submit the login form."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def click_register(self) -> None:
        """Click the Register link in the left panel."""
        self.page.locator(self.REGISTER_LINK).first.click()
        self.page.wait_for_load_state("networkidle")

    def click_logout(self) -> None:
        """Click the Log Out link and wait for redirect."""
        self.page.locator(self.LOGOUT_LINK).click()
        self.page.wait_for_load_state("networkidle")

    def get_login_error(self) -> str:
        """Return the login error message text."""
        return self.page.locator(self.LOGIN_ERROR).text_content().strip()

    def is_login_panel_visible(self) -> bool:
        """Return True when the login panel is visible (user is logged out)."""
        return self.page.locator(self.LOGIN_PANEL).is_visible()

    def is_logged_in(self) -> bool:
        """Return True when the user is logged in (logout link visible)."""
        return self.page.locator(self.LOGOUT_LINK).is_visible()
