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


class SiteDaemonN555:  # Создаем класс демона 'SiteDaemonN555'
    def __init__(self):
        self.running = True

    @staticmethod
    def run():  # Функция для запуска демона и выполнения описанных действий
        try:

            #  Указать названия региона и города, рубрики и подрубрики, цену, телефон, адрес, описание
            login_value = 'zuclij@dark2web.art'  # твой логин
            password_value = 'pzCLz?!%w$sf{66S'  # твой пароль

            title_value = 'Продам спортинвентарь'

            region_value = 'Московская область'
            city_value = 'Королев'

            rubrika_value = 'Хобби и отдых'
            rubrika_1_value = 'Спорт и отдых'
            rubrika_2_value = 'Фитнес и тренажёры'

            prise_value = '2900'
            phone_number_value = '79991234567'  # вводить номер телефона ТОЛЬКО с 'семерки' (7)

            timer_value = '2'
            #  Конец ввода переменных

            url_address = "https://n555.ru/"  # Берем данный адрес сайта и переходим на него
            webbrowser.open(url_address, new=1)  # Открываем ссылку в браузере в новой вкладке

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
            #  Автоматом входим на сайт
            driver.get("https://n555.ru/users/login/")

            input_email = driver.find_element(By.ID, "sender-email")
            input_email.send_keys(f"{login_value}")

            time.sleep(0.2)  # чуток ждем, чтобы успели все события на форме сработать

            input_user_pass = driver.find_element(By.ID, "user-pass")
            input_user_pass.send_keys(f"{password_value}")

            time.sleep(0.2)  # чуток ждем, чтобы успели все события на форме сработать

            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Войти')]")))
            login_button.click()
            #  Зашли на сайт

            time.sleep(0.5)  # чуток ждем, чтобы успели все события на форме сработать

            # Открываем сайт
            driver.get("https://n555.ru/add/")

            # ЗАГОЛОВОК ОБЪЯВЛЕНИЯ
            input_field_title = driver.find_element(By.ID, "msgTitle")
            input_field_title.send_keys(f"{title_value}")

            time.sleep(0.5)  # чуток ждем, чтобы успели все события на форме сработать

            # РЕГИОН
            # Находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, "div.multiselect").click()
            # Выбираем нужное название региона (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{region_value}']").click()

            time.sleep(float(timer_value))  # чуток ждем, чтобы успели все события на форме сработать

            # ГОРОД
            # Находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, "div.multiselect").click()
            # Выбираем нужное название города (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{city_value}']").click()

            time.sleep(0.5)  # чуток ждем, чтобы успели все события на форме сработать

            # РУБРИКА
            # Находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, "div.multiselect").click()
            # Выбираем нужное название рубрики (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{rubrika_value}']").click()

            time.sleep(float(timer_value))  # чуток ждем, чтобы успели все события на форме сработать

            # Находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, "div.multiselect").click()
            # Выбираем нужное название подрубрики (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{rubrika_1_value}']").click()

            time.sleep(2)  # чуток ждем, чтобы успели все события на форме сработать

            # Находим и кликаем на выпадающий список
            driver.find_element(By.CSS_SELECTOR, "div.multiselect").click()
            # Выбираем нужное название под-подрубрики (должно быть как на сайте) !!!!!!!!!!!!!!!!
            driver.find_element(By.XPATH, f"//option[text()='{rubrika_2_value}']").click()

            # Находим поле с ценой товара
            prise = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='f_39']")))
            # Вводим цену товара
            prise.send_keys(f"{prise_value}")

            # Находим поле с указанием номера телефона
            phone_number = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='f_14']")))
            # Вводим цену товара
            phone_number.send_keys(f"{phone_number_value}")





            time.sleep(0.5)  # чуток ждем, чтобы успели все события на форме сработать

            # Выводим в текст в IDLE о работе функции
            print(f"Окончание работы скрипта в -= {time.strftime('%a %d.%m.%Y %H:%M:%S')} =-")

        except Exception as e:  # описание ошибки, если она возникает
            print(f"Error: {e}", file=sys.stderr)
            time.sleep(10)


if __name__ == "__main__":  # запуск скрипта
    daemon = SiteDaemonN555()  # создаем экземпляр класса демона 'SiteDaemonN555()'
    daemon.run()  # запускаем демона, который выполняет функцию 'def run'
