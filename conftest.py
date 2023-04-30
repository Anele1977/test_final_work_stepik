import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# import settings_test as st


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru/en/ua etc...")


@pytest.fixture
def lang(request):
    browser_language = request.config.getoption("language")
    return browser_language


@pytest.fixture(scope="function")
def browser(request, lang):
    options = Options()
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(8)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.implicitly_wait(8)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()