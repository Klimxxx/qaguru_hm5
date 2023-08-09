from selene import be, have, browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.driver_name = 'firefox'


def test1():

    browser.config.timeout = 10
    # для работы следующей строчки необходима установка селениум 4.5.0
    browser.config.hold_driver_at_exit = True
    browser.open('/')

    # вводим имя, фамилию и имейл
    browser.element('[id="firstName"]').should(be.blank).type('Klim')
    browser.element('[id="lastName"]').should(be.blank).type('Trotsenko')
    browser.element('[id="userEmail"]').should(be.blank).type('123@123.ru')
    # выбираем пол
    browser.element('[for="gender-radio-1"]').click()
    # вводим номер телефона
    browser.element('[id="userNumber"]').should(be.blank).type('89876543210').press_tab().press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks for submitting the form"))

