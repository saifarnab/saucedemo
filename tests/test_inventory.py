import pytest
from login import Login
from inventory import Inventory


@pytest.fixture
def driver():
    inventory_page = Inventory()
    driver = inventory_page.config_driver()
    yield driver
    driver.quit()


def test_total_products(driver):
    login_page = Login()
    login_page.login(driver, login_page.correct_username, login_page.correct_password)
    inventory_page = Inventory()
    product_count = inventory_page._products_count(driver)

    # Assertion: after success, check if redirected to inventory page
    assert True if product_count == inventory_page.page_product_count else False
