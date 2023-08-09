from qaguru_hm5.conditions import match
from tests.test_demoqa import function_one, function_two

function_one()
function_two()

from selene import browser, have, be


def test_complete_todo():
    browser.config.base_url = 'https://todomvc.com/examples/emberjs'
    browser.open('/')  # задается через относительный путь конфиг.бэйс_урл

    browser.open('/')

    browser.element('#new-todo')  # поиск 1 элемента по селектору
    browser.all('#todo-list>li')  # поиск всех элементов по селектору

    browser.element('#new-todo').element('#new-todo2')  # находит эл-ты внутри эл-та

    browser.element('#new-todo').hover()  # навести мышку на эл-т

    browser.element('#new-todo').press()  # нажимает кнопки по ключу

    browser.element('#new-todo').type("a")  # напечатать а в элемент

    browser.all('#todo-list>li').should(conditions)  # проверки выполняются с помощью шуд

    browser.all('#todo-list>li').with_(
        timeout=browser.config.timeout * 2,
    ).should(have.size(3))

    browser.all('#todo-list>li').should(be.blank)

    # если мы хотим объединить модули то создаем файл матч.пай и импортируем его в код
    # теперь у нас один метод вместо хэв и би
    match.blank
    match.size()
