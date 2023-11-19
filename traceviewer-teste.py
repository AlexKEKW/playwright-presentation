import time

from playwright.sync_api import Page, sync_playwright, Playwright
import pytest


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True)
    page = context.new_page()
    page.goto("https://654d989d8dc67b1663b13dd0--funny-maamoul-f2c3db.netlify.app/")
    time.sleep(5)
    page.get_by_role("link", name="Contato").click()
    page.get_by_placeholder("Digite seu nome completo").click()
    page.get_by_placeholder("Digite seu nome completo").fill("Teste da Silva Júnior")
    page.get_by_placeholder("Digite seu melhor email").click()
    page.get_by_placeholder("Digite seu melhor email").fill("teste@gmail.com")
    page.get_by_placeholder("Digite seu telefone").click()
    page.get_by_placeholder("Digite seu telefone").fill("8198002-8922")
    page.locator("#radio-sim").check()
    page.get_by_placeholder("Digite sua mensagem").click()
    page.get_by_placeholder("Digite sua mensagem").fill("testando preenchimento automático")
    page.get_by_role("button", name="Submit").click()
    context.tracing.stop(path="trace.zip")  # https://trace.playwright.dev/

    time.sleep(5)
    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
