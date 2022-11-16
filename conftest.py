import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or edge")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "edge":
        browser = webdriver.Edge()
    else:
        raise pytest.UsageError('--browser_name should be chrome or edge')
    print(f'\nStart [{browser_name}] browser for test...')

    yield browser

    print(f'\nQuit [{browser_name}] browser...')
    browser.quit()
