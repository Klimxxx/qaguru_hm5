from selene import be, have, browser


def test1():
    browser.open('/automation-practice-form')

    # вводим имя, фамилию и имейл
    browser.element('[id="firstName"]').should(be.blank).type('Klim')
    browser.element('[id="lastName"]').should(be.blank).type('Trotsenko')
    browser.element('[id="userEmail"]').should(be.blank).type('123@123.ru')
    # выбираем пол
    browser.element('[for="gender-radio-1"]').click()
    # вводим номер телефона
    browser.element('[id="userNumber"]').should(be.blank).type('89876543210')
    # нажимаем на поле выбора даты дня рождения
    browser.element('#dateOfBirthInput').click()
    # выбираем год
    browser.element('[class^=react-datepicker__year-select]').click().element('[value="1989"]').click()
    # выбираем месяц
    browser.element('.react-datepicker__month-select').click().element('[value="0"]').click()
    # выбираем день
    browser.element('[aria-label = "Choose Monday, January 2nd, 1989"]').click()
    # подтверждаем номер телефон
    browser.element('[id="userNumber"]').press_enter()
    # проверяем успешность регистрации
    browser.element('#example-modal-sizes-title-lg').should(have.text("Thanks for submitting the form"))
    browser.element('.modal-body').should(
        have.text("Klim Trotsenko" and "123@123.ru" and "Male" and "8987654321" and "02 January,1989"))
