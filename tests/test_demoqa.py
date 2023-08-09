from selene import be, have, browser
import pytest


def test1():

    browser.open('/automation-practice-form')
    # вводим имя, фамилию и имейл
    browser.element('[id="firstName"]').should(be.blank).type('Klim')
    browser.element('[id="lastName"]').should(be.blank).type('Trotsenko')
    browser.element('[id="userEmail"]').should(be.blank).type('123@123.ru')
    # выбираем пол
    browser.element('[for="gender-radio-1"]').click()
    # вводим номер телефона
    browser.element('[id="userNumber"]').should(be.blank).type('89876543210').press_tab()#.press_enter()
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks for submitting the form"))

