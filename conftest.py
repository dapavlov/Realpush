import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser:")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument("user-data-dir=selenium")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        fp.set_preference("network.cookie.cookieBehavior", 2)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    elif browser_name == "opera":
        options = Options()
        options.binary_location = r'C:\Users\mi\AppData\Local\Programs\Opera\65.0.3467.72'
        options.add_argument("--start-maximized")
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        options.add_argument("user-data-dir=selenium")
        print("\nstart opera browser for test..")
        browser = webdriver.Opera(options=options)
    else:
        raise pytest.UsageError("Unknown browser")
    yield browser
    print("\nquit browser..")
    browser.quit()
