"""
Step definitions for TC_001 - Launch Application.
Verifies that the ParaBank website opens and the homepage loads correctly.
"""
from behave import given, when, then
from pages.home_page import HomePage


@given("the browser is available")
def step_browser_available(context):
    context.home_page = HomePage(context.page)


@when("I navigate to the ParaBank URL")
def step_navigate_to_parabank(context):
    context.home_page.navigate_to_home()


@then("the ParaBank homepage should load successfully")
def step_homepage_loaded(context):
    title = context.home_page.get_page_title()
    assert title, "Page title should not be empty after navigation"
    context.home_page.take_screenshot("TC001_homepage_loaded")
    print(f"\n  [TC_001] Page loaded - Title: '{title}'")


@then('the page title should contain "{text}"')
def step_page_title_contains(context, text):
    title = context.home_page.get_page_title()
    assert text in title, (
        f"Expected page title to contain '{text}', but got: '{title}'"
    )
    print(f"  [TC_001] Title verification passed: '{title}'")


@then("the login panel should be visible")
def step_login_panel_visible(context):
    assert context.home_page.is_login_panel_visible(), (
        "Login panel should be visible on the ParaBank homepage"
    )
    print("  [TC_001] Login panel is visible - Homepage loaded successfully")
