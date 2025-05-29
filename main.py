import time
import sys
import signal
import webbrowser
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver import ActionChains


driver = webdriver.Edge()
# class SiteDaemon:  # создаем класс демона 'SiteDaemon'
#     def __init__(self):
#         self.running = True
#         signal.signal(signal.SIGTERM, self.handle_signal)
#         signal.signal(signal.SIGINT, self.handle_signal)
#
#     def handle_signal(self, signum, frame):
#         self.running = False
#
#     def run(self):  # функция для запуска демона и выполнения описанных действий
try:
    # выводим в текст в IDLE о работе функции
    print(f"Начало работы скрипта в {time.strftime('%a %d.%m.%Y %H:%M:%S')}.")

    url_site = "https://gde.ru/post"  # добавляем адрес сайта (В КАВЫЧКАХ), в конце знак '/' - не ставить!
    URL_address = url_site  # берем первый адрес сайта в списке 'url_site'
    webbrowser.open(URL_address, new=0)  # открываем ссылку в браузере в новой вкладке

    response = requests.get(url_site)  # Получаем страницу, на которой хотим заполнить формы
    soup = BeautifulSoup(response.text, "html.parser")
    time.sleep(2)

    # form = soup.find("form", {"id": "post_form"})  # Находим форму объявления
    time.sleep(2)

    # Ищем поля по id и вносим данные для отправки. Формат: {"имя_поля (его id): "значение, вносимое в поле"}
    data = {
        "AInfoForm_phone": "+7 (999) 123-45-67",
        "AInfoForm_title": "KHKFGKLJFJLJJG",

        # "section-button":
        #     {"aria-expanded": "true"},
        # "section-button":
        #     {"aria-activedescendant": "ui-id-14"},
        # "section-button":
        #     {"aria-expanded": "false"},
    }
    time.sleep(2)

    ActionChains(driver).move_to_element(ui-id-14).click().perform()
    response = requests.post(url_site, data=data)  # Отправляем POST-запрос для размещения объявления
    print(response.text)  # вывод результата размещения объявления
    time.sleep(2)  # даем серверу "отдохнуть" и загрузить элементы

except Exception as e:  # описание ошибки, если она возникает
    print(f"Error: {e}", file=sys.stderr)
    time.sleep(10)
#
# if __name__ == "__main__":  # запуск скрипта
#     daemon = SiteDaemon()  # создаем экземпляр класса демона 'SiteDaemon()'
#     daemon.run()  # запускаем демона, который выполняет функцию 'def run'
