"""
Step definitions for TC_002 — Registration with Valid Details.
Creates a new account and stores credentials in shared_data for TC_005 reuse.
"""
from behave import given, when, then
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utils.test_data import generate_user_data


@given("the user is on the ParaBank homepage")
def step_user_on_homepage(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate_to_home()


@when("the user clicks the Register link")
def step_click_register_link(context):
    if not hasattr(context, "home_page"):
        context.home_page = HomePage(context.page)
    context.home_page.click_register()
    context.register_page = RegisterPage(context.page)


@when("the user fills all required fields with valid details")
def step_fill_valid_details(context):
    user_data = generate_user_data("prasanth")
    context.shared_data["username"] = user_data["username"]
    context.shared_data["password"] = user_data["password"]
    context.register_page.fill_form(user_data)
    print(f"\n  [TC_002] Registering with username: {user_data['username']}")


@when("the user submits the registration form")
def step_submit_registration_form(context):
    context.register_page.submit_form()


@then("the account should be created successfully")
def step_account_created(context):
    success_msg = context.register_page.get_success_message()
    assert "created" in success_msg.lower() or "Welcome" in success_msg, (
        f"Expected success message after registration, but got:\n{success_msg}"
    )
    context.register_page.take_screenshot("TC002_registration_success")


@then("a welcome message should be displayed")
def step_welcome_message_displayed(context):
    msg = context.register_page.get_success_message()
    assert msg, "Welcome message should not be empty after successful registration"
    print(f"  [TC_002] Registration successful. Username stored: "
          f"{context.shared_data.get('username')}")
