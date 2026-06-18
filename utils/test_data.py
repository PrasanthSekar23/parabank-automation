"""
Test data factory - generates dynamic user data to ensure uniqueness per run.
"""
import time


def generate_user_data(base_username: str = "prasanth") -> dict:
    """
    Build a dictionary of valid registration data.
    Username is suffixed with the current epoch timestamp to ensure
    uniqueness across repeated test runs on the shared ParaBank demo site.

    Args:
        base_username: Prefix for the generated username. Default: 'prasanth'.

    Returns:
        dict with keys matching RegisterPage.fill_form() expectations.
    """
    timestamp = int(time.time())
    return {
        "first_name": "Prasanth",
        "last_name": "Sekar",
        "address": "123 Automation Drive",
        "city": "Chennai",
        "state": "TN",
        "zip_code": "600001",
        "phone": "9876543210",
        "ssn": "123-45-6789",
        "username": f"{base_username}_{timestamp}",
        "password": "password123",
    }
