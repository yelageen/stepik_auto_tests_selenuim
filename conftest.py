import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.edge.options   import Options as edgeOptions

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None, help='Choose browser: chrome or edge')
    parser.addoption('--language'    , action='store', default=None, help='Choose language: ru or en-gb')

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    if language != 'ru' and language != 'en-gb':
        raise pytest.UsageError(f'--language should be ru or en-gb: [{language}]')

    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        options = chromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'edge':
        options = edgeOptions()
        options.add_argument(f'--lang={language}')
        browser = webdriver.Edge(options=options)
    else:
        raise pytest.UsageError(f'--browser_name should be chrome or edge: [{browser_name}]')

    print(f'\nStart [{browser_name}] browser for test on [{language}] language...')
    yield browser
    print(f'\nQuit [{browser_name}] browser...')

    browser.quit()
