import pytest
from playwright.sync_api import sync_playwright

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