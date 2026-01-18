import pytest

from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function", autouse=False)
def driver():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()  #Здесь ИИ подсказал, что надо завершить работы playwright,
                    # ибо второй тест не запускается после первого из-за того, что асинхронный контекст уже активен
