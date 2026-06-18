"""
Step definitions for TC_004 - Duplicate Username Validation.
Registers a user successfully, then tries the same username again
and asserts the 'already exists' error is shown.
"""
from behave import when, then
from pages.register_page import RegisterPage
from utils.test_data import generate_user_data


@when("the user registers successfully with a unique username")
def step_register_unique_user(context):
    context.register_page = RegisterPage(context.page)
    user_data = generate_user_data("prasanth")
    # Store the username so the next step can reuse it
    context.duplicate_username = user_data["username"]
    context.duplicate_password = user_data["password"]
    context.register_page.fill_form(user_data)
    context.register_page.submit_form()
    print(f"\n  [TC_004] First registration: {context.duplicate_username}")
    # Verify first registration succeeded before testing duplicate
    msg = context.register_page.get_success_message()
    assert "created" in msg.lower() or "Welcome" in msg, (
        f"First registration should succeed. Got: {msg}"
    )


@when("the user clicks the Register link again")
def step_click_register_again(context):
    context.register_page = RegisterPage(context.page)
    context.register_page.navigate_to_register()


@when("the user attempts to register with the same username")
def step_register_duplicate(context):
    context.register_page = RegisterPage(context.page)
    duplicate_data = generate_user_data("prasanth")
    # Override with the already-registered username
    duplicate_data["username"] = context.duplicate_username
    duplicate_data["password"] = context.duplicate_password
    context.register_page.fill_form(duplicate_data)
    context.register_page.submit_form()
    context.register_page.take_screenshot("TC004_duplicate_username_attempt")
    print(f"  [TC_004] Attempted duplicate registration: {context.duplicate_username}")


@then("the system should display a username already exists error")
def step_username_exists_error(context):
    errors = context.register_page.get_validation_errors()
    has_duplicate_error = any(
        "already" in e.lower() or "exists" in e.lower() for e in errors
    )
    assert has_duplicate_error, (
        f"Expected 'username already exists' error. Errors found: {errors}"
    )
    print(f"  [TC_004] Duplicate username error correctly shown: "
          f"{[e for e in errors if 'already' in e.lower() or 'exists' in e.lower()]}")
