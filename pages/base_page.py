"""
Base Page Object - common methods shared by all page classes.
"""
import os
from datetime import datetime


BASE_URL = "https://parabank.parasoft.com/parabank"


class BasePage:
    """Provides shared navigation and utility methods for all page objects."""

    def __init__(self, page):
        self.page = page
        self.base_url = BASE_URL

    def navigate(self, path: str = "") -> None:
        """Navigate to a URL relative to the base URL and wait for network idle."""
        self.page.goto(f"{self.base_url}{path}")
        self.page.wait_for_load_state("networkidle")

    def take_screenshot(self, name: str) -> str:
        """Capture a full-page screenshot and return the saved file path."""
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/{name}_{timestamp}.png"
        self.page.screenshot(path=path, full_page=True)
        print(f"  [Screenshot] Saved: {path}")
        return path

    def get_page_title(self) -> str:
        """Return the current browser page title."""
        return self.page.title()

    def get_current_url(self) -> str:
        """Return the current page URL."""
        return self.page.url
