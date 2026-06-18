"""
Behave environment hooks - manages browser lifecycle across all scenarios.
"""
import os
from datetime import datetime
from playwright.sync_api import sync_playwright


def before_all(context):
    """
    Suite-level setup: launch the browser once and initialize shared state.
    shared_data persists across all scenarios so TC_002 credentials
    can be consumed by TC_005.
    """
    os.makedirs("screenshots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    context.playwright = sync_playwright().start()
    # Run headless in CI environments, headed locally
    is_ci = os.environ.get("CI", "false").lower() == "true"
    context.browser = context.playwright.chromium.launch(
        headless=is_ci,
        slow_mo=0 if is_ci else 50,
    )
    # Shared dictionary that persists across scenarios within the same run.
    context.shared_data = {}

    print("\n" + "=" * 55)
    print("  ParaBank Automation Suite - Starting")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)


def before_scenario(context, scenario):
    """Open a fresh browser page before every scenario."""
    context.page = context.browser.new_page(viewport={"width": 1280, "height": 720})
    print(f"\n>> Running: [{scenario.tags[0] if scenario.tags else ''}] {scenario.name}")


def after_scenario(context, scenario):
    """
    Capture a screenshot on failure and close the page after every scenario.
    """
    status_icon = "[PASS]" if scenario.status.name == "passed" else "[FAIL]"
    print(f"{status_icon} Finished: {scenario.name} - {scenario.status.name.upper()}")

    if scenario.status.name == "failed":
        safe_name = scenario.name.replace(" ", "_").replace("/", "_")[:60]
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"screenshots/FAIL_{safe_name}_{ts}.png"
        try:
            context.page.screenshot(path=screenshot_path, full_page=True)
            print(f"  [Screenshot] Saved on failure: {screenshot_path}")
        except Exception as e:
            print(f"  [Screenshot] Could not save: {e}")

    context.page.close()


def after_all(context):
    """Shut down the browser and Playwright after the full suite."""
    context.browser.close()
    context.playwright.stop()
    print("\n" + "=" * 55)
    print("  ParaBank Automation Suite - Completed")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55 + "\n")
