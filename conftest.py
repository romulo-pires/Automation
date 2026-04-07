import pytest
from playwright.sync_api import sync_playwright
from pages.saucedemo_login_page import LoginPage
from pages.saucedemo_shop_page import ShopPage

@pytest.fixture
def api_request():
    with sync_playwright() as p:
        request = p.request.new_context(
            base_url="https://reqres.in",
            extra_http_headers={
                "x-api-key": "reqres_9f169b9a457f46b682e1270adf87e76d"
            }
        )
        yield request

@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)
    shop_page = ShopPage(page)

    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    shop_page.check_loaded()

    return page
