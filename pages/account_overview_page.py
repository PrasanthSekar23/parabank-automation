"""
Account Overview Page Object - post-login dashboard showing account balances.
"""
from pages.base_page import BasePage


class AccountOverviewPage(BasePage):
    """
    Represents the ParaBank Accounts Overview page (/overview.htm).
    Provides methods to read and print account balance information.
    """

    # --- Selectors ---
    PAGE_TITLE = '#rightPanel h1.title'
    ACCOUNT_TABLE = '#accountTable'
    ACCOUNT_ROWS = '#accountTable tbody tr'
    TOTAL_BALANCE = '#accountTable tfoot .balance'
    LOGOUT_LINK = 'a[href*="logout.htm"]'

    def navigate_to_overview(self) -> None:
        """Navigate directly to the account overview page."""
        self.navigate("/overview.htm")

    def get_page_title(self) -> str:
        """Return the main heading text of the overview page."""
        return self.page.locator(self.PAGE_TITLE).first.text_content().strip()

    def is_overview_displayed(self) -> bool:
        """Return True when the account overview heading is visible."""
        try:
            titles = self.page.locator(self.PAGE_TITLE).all()
            for title in titles:
                text = title.text_content().strip()
                if "Accounts Overview" in text:
                    return True
            return False
        except Exception:
            return False

    def get_account_balances(self) -> list[dict]:
        """
        Parse the accounts table and return a list of dicts with keys:
        account_id, balance, available.
        """
        rows = self.page.locator(self.ACCOUNT_ROWS).all()
        balances = []
        for row in rows:
            cells = row.locator("td").all_text_contents()
            if len(cells) >= 2:
                balances.append({
                    "account_id": cells[0].strip(),
                    "balance": cells[1].strip(),
                    "available": cells[2].strip() if len(cells) > 2 else "N/A",
                })
        return balances

    def get_total_balance(self) -> str:
        """Return the total balance text from the table footer."""
        try:
            return self.page.locator(self.TOTAL_BALANCE).text_content().strip()
        except Exception:
            return "N/A"

    def print_balances(self) -> list[dict]:
        """
        Retrieve all account balances, print them to stdout, and return the list.
        """
        balances = self.get_account_balances()

        print("\n" + "=" * 45)
        print("         ACCOUNT BALANCE SUMMARY")
        print("=" * 45)
        for account in balances:
            print(f"  Account ID  : {account['account_id']}")
            print(f"  Balance     : {account['balance']}")
            print(f"  Available   : {account['available']}")
            print("-" * 45)
        total = self.get_total_balance()
        print(f"  Total Balance: {total}")
        print("=" * 45 + "\n")

        return balances
