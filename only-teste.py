from playwright.sync_api import Page, sync_playwright, expect
import pytest


@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # ou True
        yield browser.new_page()
        browser.close()


@pytest.mark.only_browser("chromium")
def test_title(page: Page):
    page.goto('https://654d989d8dc67b1663b13dd0--funny-maamoul-f2c3db.netlify.app/')
    assert page.title() == 'Michelle Sweets'


@pytest.mark.only_browser("chromium")
def test_list_items(page: Page):
    page.goto('https://654d989d8dc67b1663b13dd0--funny-maamoul-f2c3db.netlify.app/')
    expect(page.locator('section:has-text("Quem Somos")'))


@pytest.mark.only_browser("chromium")
def test_title3(page: Page):
    page.goto('https://654d989d8dc67b1663b13dd0--funny-maamoul-f2c3db.netlify.app/')
    assert page.title() == 'Michelle Sweets'
