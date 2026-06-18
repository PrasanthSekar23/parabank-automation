"""
Step definitions for TC_006 — Account Amount Displayed After Login.
Logs in and verifies the balance table is rendered with at least one row.
"""
from behave import given, when, then
from pages.home_page import HomePage
from pages.account_overview_page import AccountOverviewPage


@given("the user is logged in with their registered account")
def step_user_is_logged_in(context):
    assert "username" in context.shared_data, (
        "No registered account found. Ensure TC_002 ran before this scenario."
    )
    context.home_page = HomePage(context.page)
    context.home_page.navigate_to_home()
    context.home_page.login(
        context.shared_data["username"],
        context.shared_data["password"],
    )
    assert context.home_page.is_logged_in(), (
        f"Login failed for user: {context.shared_data['username']}"
    )
    print(f"\n  [TC_006] Logged in as: {context.shared_data['username']}")


@when("the user navigates to the account overview page")
def step_navigate_to_overview(context):
    context.account_page = AccountOverviewPage(context.page)
    # The overview is shown immediately after login; navigate explicitly if needed
    if not context.account_page.is_overview_displayed():
        context.account_page.navigate_to_overview()


@then("the account overview page title should be visible")
def step_overview_title_visible(context):
    assert context.account_page.is_overview_displayed(), (
        "Account Overview page title should be visible"
    )
    title = context.account_page.get_page_title()
    print(f"  [TC_006] Overview page title: '{title}'")
    context.account_page.take_screenshot("TC006_account_overview")


@then("at least one account with a balance should be displayed")
def step_balance_displayed(context):
    balances = context.account_page.get_account_balances()
    assert len(balances) > 0, (
        "Expected at least one account row in the balance table, but found none"
    )
    print(f"  [TC_006] {len(balances)} account(s) found with balance:")
    for acc in balances:
        print(f"    Account: {acc['account_id']} | Balance: {acc['balance']}")
