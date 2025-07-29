import sys
import time
import webbrowser
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# -----------------------------------------------------
# -------- ЗАГРУЖАТЬ ФОТОГРАФИИ САМОМТОЯТЕЛЬНО --------
# -----------------------------------------------------


class SiteDaemon_RUDOS:  # Создаем класс демона 'SiteDaemon_RUDOS'
    def __init__(self):
        self.running = True

    @staticmethod
    def run():  # Функция для запуска демона и выполнения описанных действий
        try:
            #  Начало ввода переменных
            #  Названия региона и города, рубрики и подрубрики, цену, телефон, адрес, описание (все должны быть в кавычках!!!)
            login_value = 'ciklak@ligue-games.art'  # твой логин
            password_value = 'nn^f8TR4Hr'  # твой пароль

            title_value = 'Продам спортинвентарь'  # заголовок объявления

            rubrika_value = 'Хобби и отдых'  # главная категория
            rubrika_1_value = 'Спорт и отдых'  # вторая категория
            rubrika_2_value = 'Фитнес и тренажёры'  # третья категория

            prise_value = '2900'  # цена продажи

            # Если ОПИСАНИЕ ОБЪЯВЛЕНИЯ не влазит в одну строчку, то нажимай ENTER и автоматически перенесется на новую строку
            desc_value = 'Продам тренажер в отличном качестве. ТОЛЬКО WhatsApp!!!\n' \
                         'САМОВЫВОЗ!\nДокументы и чеки в наличии.'

            region_value = 'Московская область'  # регион продажи
            city_value = 'Королев'  # город продажи

            # user_value = "Твое имя или имя из профиля"  # максимум 24 символа
            # phone_number_value = '9991234567'  # вводи свой номер телефона БЕЗ 'семерки' (7)

            address_value = f'Россия, {region_value}, {city_value}, улица Мичурина, 27/1'  # указывать в таком формате (без сокращений)

            timer_value = '1.2'  # (в секундах) если не успевают загрузиться формы, то УВЕЛИЧЬ данное значение (это ожидание загрузки сайта)
            #  Конец ввода переменных

            url_address = "https://rudos.ru/"  # Вносим в переменную 'url_address' адрес сайта
            # webbrowser.open(url_address, new=1)  # Открываем ссылку в браузере в новой вкладке

            # Выводим в текст в IDLE о работе функции
            print(f"Начало работы скрипта в -= {time.strftime('%a %d.%m.%Y %H:%M:%S')} =-. "
                  f"Переход на сайт: \"{url_address}\"")

            # Путь к папке профиля
            profile_path = os.path.join(os.getenv('APPDATA'), 'Local', 'Google', 'Chrome', 'User Data', 'SeleniumProfile')

            # Настройки Chrome
            options = Options()
            options.add_argument(f"user-data-dir={profile_path}")  # Используем конкретный профиль
            options.add_argument("--start-maximized")  # Открыть развернутым окно браузера
            options.add_experimental_option("detach", True)  # Не закрывать браузер после выполнения

            # Создаем драйвер
            driver = webdriver.Chrome(options=options)

            # Будем находить поля по ID, имени, XPath или CSS-селектору
            driver.get("https://rudos.ru/registr/enter/")

            # ВВОД ЛОГИНА
            input_email = driver.find_element(By.NAME, "email")
            input_email.send_keys(f"{login_value}")

            time.sleep(0.2)  # чуток ждем, чтобы на форме успели сработать все события

            # ВВОД ПАРОЛЯ
            input_user_pass = driver.find_element(By.NAME, "password_user")
            input_user_pass.send_keys(f"{password_value}")

            # СНИМАЕМ ГАЛОЧКУ "ЗАПОМНИТЬ МЕНЯ"
            checkbox_remember = driver.find_element(By.ID, "memory_authoriz")
            if checkbox_remember.is_selected():  # проверяем, отмечен ли чекбокс
                checkbox_remember.click()  # cнимаем галочку

            time.sleep(15)  # ждем, чтобы ты мог ввести код (captcha). Если не успеваешь или медленная скорость соедиения - увеличь значение в скобках!

            # ОТКРЫВАЕМ СТРАНИЦУ С ДОБАВЛЕНИЕМ НОВОГО ОБЪЯВЛЕНИЯ
            url_address_adv = "https://rudos.ru/newadv/"
            driver.get(f"{url_address_adv}")
            print(f"Переход на страницу объявления в -= {time.strftime('%a %d.%m.%Y %H:%M:%S')} =-")

            # ЗАГОЛОВОК ОБЪЯВЛЕНИЯ
            input_field_title = driver.find_element(By.NAME, "name_adv")
            input_field_title.send_keys(f"{title_value}")

            # КАТЕГОРИЯ
            # находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, ".jq-selectbox__select").click()
            # Выбираем нужное название рубрики (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{rubrika_value}']").click()

            time.sleep(float(timer_value))  # чуток ждем, чтобы на форме успели сработать все события

            # ВТОРАЯ КАТЕГОРИЯ
            # находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, ".jq-selectbox__select").click()
            # Выбираем нужное название подрубрики (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{rubrika_1_value}']").click()

            time.sleep(float(timer_value))  # чуток ждем, чтобы на форме успели сработать все события

            # ТРЕТЬЯ КАТЕГОРИЯ
            # находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, ".jq-selectbox__select").click()
            # Выбираем нужное название под-подрубрики (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{rubrika_2_value}']").click()

            # ЦЕНА ТОВАРА
            prise = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "cost")))
            # Вводим цену товара
            prise.send_keys(f"{prise_value}")

            # ТЕКСТ ОБЪЯВЛЕНИЯ (максимум 4000 символов !!!)
            input_field_title = driver.find_element(By.NAME, "text_adv")
            input_field_title.send_keys(f"{desc_value}")

            # РЕГИОН
            # находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, ".jq-selectbox__select").click()
            # Выбираем нужное название региона (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{region_value}']").click()

            time.sleep(float(timer_value))  # чуток ждем, чтобы на форме успели сработать все события

            # ГОРОД
            # находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, ".jq-selectbox__select").click()
            # Выбираем нужное название города (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{city_value}']").click()

            time.sleep(0.5)  # чуток ждем, чтобы на форме успели сработать все события

            # # ВАШЕ ИМЯ (имя пользователя автоматически берется из профиля, но можно поменять)
            # name_user = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "name_user")))
            # # Вводим имя продавца
            # name_user.send_keys(f"{user_value}")
            #
            # # НОМЕР ТЕЛЕФОНА
            # phone_number = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "phone")))
            # # Вводим номер телефона
            # phone_number.send_keys(f"{phone_number_value}")

            # МЕСТО ОКАЗАНИЯ УСЛУГ (откроется карта)
            map_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Место оказания услуг')]")))
            map_button.click()

            # АДРЕС СДЕЛКИ
            address = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "address")))
            # Вводим адрес
            address.send_keys(f"{address_value}")

            time.sleep(0.5)  # чуток ждем, чтобы на форме успели сработать все события

            # Выводим в текст в IDLE о работе функции
            print(f"Окончание работы скрипта в -= {time.strftime('%a %d.%m.%Y %H:%M:%S')} =-")

        except Exception as e:  # описание ошибки, если она возникает
            print(f"Error: {e}", file=sys.stderr)
            time.sleep(10)


if __name__ == "__main__":  # запуск скрипта
    daemon = SiteDaemon_RUDOS()  # создаем экземпляр класса демона 'SiteDaemon_RUDOS()'
    daemon.run()  # запускаем демона, который выполняет функцию 'def run'
