"""
Step definitions for TC_005 — Login with Newly Created Account.
Reads credentials stored by TC_002 via context.shared_data.
"""
from behave import given, when, then
from pages.home_page import HomePage
from pages.account_overview_page import AccountOverviewPage


@given("the user has a registered account from TC_002")
def step_has_registered_account(context):
    assert "username" in context.shared_data, (
        "No registered account found. Ensure TC_002 ran before TC_005 "
        "in the same behave session."
    )
    print(f"\n  [TC_005] Using account: {context.shared_data['username']}")


@when("the user navigates to the ParaBank homepage")
def step_navigate_to_homepage(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate_to_home()


@when("the user enters their registered username and password")
def step_enter_registered_credentials(context):
    username = context.shared_data["username"]
    password = context.shared_data["password"]
    context.home_page.enter_username(username)
    context.home_page.enter_password(password)
    print(f"  [TC_005] Entering credentials for: {username}")


@when("the user clicks the Login button")
def step_click_login_button(context):
    context.home_page.click_login()


@then("the user should be logged in successfully")
def step_logged_in_successfully(context):
    assert context.home_page.is_logged_in(), (
        "Expected the welcome panel to be visible after login, "
        "but the user does not appear to be logged in."
    )
    context.home_page.take_screenshot("TC005_login_success")
    print("  [TC_005] Login successful — Welcome panel is visible")


@then("the account overview page should be displayed")
def step_account_overview_displayed(context):
    context.account_page = AccountOverviewPage(context.page)
    assert context.account_page.is_overview_displayed(), (
        "Expected 'Accounts Overview' heading to be visible after login"
    )
    title = context.account_page.get_page_title()
    print(f"  [TC_005] Account overview displayed — Title: '{title}'")
