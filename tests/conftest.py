# все что касается настройки браузера например мы выносим в отдельный файл

import pytest
from selene import browser
from selenium import webdriver

# scope - прописываем чтобы фикстура вызывалась для функции (каждого теста) autouse - чтобы вызывалась всегда автоматически

pytest.fixture(scope='function', autouse=True)


def browser_management():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    # browser.config.driver_name = 'chrome'
    # browser.config.driver_options = webdriver.ChromeOptions()

    driver_options = webdriver.firefox
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    yield  # передает управление тесту

    browser.quit()


"""Пример перехода на селен из селениума"""
@pytest.fixture()
def driver():
    driver_options = webdriver.ChromeOptions()
    driver_options.add.argument('--headless')
    driver = webdriver.Chrome(
        service=ChromeService(executable_path=ChromeDriverManager().install()),
        options=driver_options,
    )
    yield driver
    driver.quit()

@pytest.fixture()
def browser(driver):

    yield Browser(Config(driver=driver))

