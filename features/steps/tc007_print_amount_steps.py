"""
Step definitions for TC_007 - Automation Prints Displayed Amount.
Captures the account balance and prints it to execution logs.
"""
from behave import when, then
from pages.account_overview_page import AccountOverviewPage


@when("the automation captures the displayed account balance")
def step_capture_balance(context):
    context.account_page = AccountOverviewPage(context.page)
    context.captured_balances = context.account_page.print_balances()
    context.account_page.take_screenshot("TC007_balance_printed")


@then("the balance amount should be printed to the execution logs")
def step_balance_printed_to_logs(context):
    assert hasattr(context, "captured_balances"), (
        "Balance capture step must run before this assertion"
    )
    assert context.captured_balances is not None, (
        "Captured balances should not be None"
    )
    print(f"  [TC_007] Balance successfully printed to logs. "
          f"Accounts captured: {len(context.captured_balances)}")


@then("the printed balance should not be empty")
def step_printed_balance_not_empty(context):
    balances = context.captured_balances
    assert len(balances) > 0, (
        "Printed balance list should not be empty - "
        "at least one account must be present"
    )
    for acc in balances:
        assert acc["balance"], (
            f"Balance field should not be empty for account: {acc['account_id']}"
        )
    print(f"  [TC_007] All {len(balances)} account balance(s) confirmed non-empty")
