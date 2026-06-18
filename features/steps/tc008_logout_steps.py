"""
Step definitions for TC_008 - Logout.
Clicks the log out link and verifies the login panel reappears.
"""
from behave import when, then
from pages.home_page import HomePage


@when("the user clicks the Log Out button")
def step_click_logout(context):
    context.home_page = HomePage(context.page)
    context.home_page.click_logout()
    context.home_page.take_screenshot("TC008_after_logout")
    print("\n  [TC_008] Logout clicked - waiting for redirect")


@then("the user should be redirected to the homepage")
def step_redirected_to_homepage(context):
    current_url = context.home_page.get_current_url()
    assert "index" in current_url or "parabank" in current_url, (
        f"Expected redirect to homepage after logout, but URL is: {current_url}"
    )
    print(f"  [TC_008] Redirected to: {current_url}")


@then("the login panel should be visible again")
def step_login_panel_visible_again(context):
    assert context.home_page.is_login_panel_visible(), (
        "Login panel should be visible after logout, indicating the "
        "user session has been terminated"
    )
    print("  [TC_008] Login panel visible - Logout successful")
