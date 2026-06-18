"""
Step definitions for TC_003 — Mandatory Field Validation.
Submits an empty form and asserts all required field errors appear.
"""
from behave import when, then
from pages.register_page import RegisterPage


@when("the user submits the registration form without filling any fields")
def step_submit_empty_form(context):
    context.register_page = RegisterPage(context.page)
    context.register_page.submit_form()
    context.register_page.take_screenshot("TC003_empty_form_submitted")


@then("validation error messages should be displayed for required fields")
def step_validation_errors_displayed(context):
    errors = context.register_page.get_validation_errors()
    assert len(errors) > 0, (
        "At least one validation error should appear when the form is submitted empty"
    )
    print(f"\n  [TC_003] {len(errors)} validation error(s) displayed:")
    for err in errors:
        print(f"    - {err.strip()}")


@then("the error for first name should be shown")
def step_error_first_name(context):
    errors = context.register_page.get_validation_errors()
    assert any("first name" in e.lower() for e in errors), (
        f"Expected 'First name is required.' error. Errors found: {errors}"
    )


@then("the error for last name should be shown")
def step_error_last_name(context):
    errors = context.register_page.get_validation_errors()
    assert any("last name" in e.lower() for e in errors), (
        f"Expected 'Last name is required.' error. Errors found: {errors}"
    )


@then("the error for address should be shown")
def step_error_address(context):
    errors = context.register_page.get_validation_errors()
    assert any("address" in e.lower() for e in errors), (
        f"Expected 'Address is required.' error. Errors found: {errors}"
    )


@then("the error for city should be shown")
def step_error_city(context):
    errors = context.register_page.get_validation_errors()
    assert any("city" in e.lower() for e in errors), (
        f"Expected 'City is required.' error. Errors found: {errors}"
    )


@then("the error for state should be shown")
def step_error_state(context):
    errors = context.register_page.get_validation_errors()
    assert any("state" in e.lower() for e in errors), (
        f"Expected 'State is required.' error. Errors found: {errors}"
    )


@then("the error for zip code should be shown")
def step_error_zip(context):
    errors = context.register_page.get_validation_errors()
    assert any("zip" in e.lower() for e in errors), (
        f"Expected 'Zip Code is required.' error. Errors found: {errors}"
    )


@then("the error for SSN should be shown")
def step_error_ssn(context):
    errors = context.register_page.get_validation_errors()
    assert any("social security" in e.lower() or "ssn" in e.lower() for e in errors), (
        f"Expected SSN required error. Errors found: {errors}"
    )


@then("the error for username should be shown")
def step_error_username(context):
    errors = context.register_page.get_validation_errors()
    assert any("username" in e.lower() for e in errors), (
        f"Expected 'Username is required.' error. Errors found: {errors}"
    )


@then("the error for password should be shown")
def step_error_password(context):
    errors = context.register_page.get_validation_errors()
    assert any("password" in e.lower() for e in errors), (
        f"Expected 'Password is required.' error. Errors found: {errors}"
    )
