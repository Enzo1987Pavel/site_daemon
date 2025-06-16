import signal
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


class SiteDaemon_N555:  # Создаем класс демона 'SiteDaemon'
    def __init__(self):
        self.running = True
        signal.signal(signal.SIGTERM, self.handle_signal)
        signal.signal(signal.SIGINT, self.handle_signal)

    def handle_signal(self, signum, frame):
        self.running = False

    def run(self):  # Функция для запуска демона и выполнения описанных действий
        try:

            # !!!!! Добавляем адрес сайта с объявлением (в кавычках. В конце точку не ставить) !!!!!
            URL_address = "https://n555.ru/"  # Берем данный адрес сайта и переходим на него
            webbrowser.open(URL_address, new=1)  # Открываем ссылку в браузере в новой вкладке

            # Выводим в текст в IDLE о работе функции
            print(f"Начало работы скрипта в -= {time.strftime('%a %d.%m.%Y %H:%M:%S')} =-. Переход на сайт: \"{URL_address}\"")

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

            driver.get("https://n555.ru/users/login/")

            input_email = driver.find_element(By.ID, "sender-email")
            input_email.send_keys("zuclij@dark2web.art")  # Можно поменять текст, который в кавычках

            input_user_pass = driver.find_element(By.ID, "user-pass")
            input_user_pass.send_keys("pzCLz?!%w$sf{66S")  # Можно поменять текст, который в кавычках

            button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
            button.click()


            # Открываем сайт
            driver.get("https://n555.ru/add/")

            # # НОМЕР ТЕЛЕФОНА
            # input_field_phone = driver.find_element(By.ID, "AInfoForm_phone")
            # input_field_phone.send_keys("+7 (999) 123-45-67")  # Можно поменять текст, который в кавычках

            # ЗАГОЛОВОК ОБЪЯВЛЕНИЯ
            input_field_title = driver.find_element(By.ID, "msgTitle")
            input_field_title.send_keys("Продаю спортинвентарь")  # Можно поменять текст, который в кавычках

            # # КАТЕГОРИЯ (основная)
            # menu_item_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//ul[@id='section-menu']//li[contains(text(), 'Спорт и фитнес')]")))  # !!!!!!!!!!!!!!
            # menu_item_1.click()
            # selected_text = driver.find_element(By.CSS_SELECTOR, "#section-button .ui-selectmenu-text").text
            # # Выбор категории_2
            # menu_item_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//ul[@id='ui-id-17-menu']//li[contains(text(), 'Спорттовары')]")))  # !!!!!!!!!!!!!!
            # menu_item_2.click()
            # selected_text = driver.find_element(By.CSS_SELECTOR, "#ui-id-17-button .ui-selectmenu-text").text
            # # Выбор категории_3
            # menu_item_3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//ul[@id='ui-id-26-menu']//li[contains(text(), 'Тренажеры')]")))  # !!!!!!!!!!!!!!
            # menu_item_3.click()
            # selected_text = driver.find_element(By.CSS_SELECTOR, "#ui-id-26-button .ui-selectmenu-text").text
            #
            # # РЕГИОН
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Region-button"))).click()
            # region_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Region-menu")))
            #
            # # Ищем нужную область в меню
            # try:
            #     region_option = region_menu.find_element(By.XPATH, ".//li[text()='Московская область и Москва']")
            #     region_option.click()
            # except:
            #     # Если не нашли по точному тексту, пробуем другой вариант (частичное совпадение)
            #     region_option = region_menu.find_element(By.XPATH, ".//li[contains(text(), 'Московск')]")
            #     region_option.click()
            # # Проверка, что выбрано в меню
            # selected_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            #     (By.CSS_SELECTOR, "#Region-button .ui-selectmenu-text"))).text
            #
            # # ГОРОД
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Geo-button"))).click()
            # city_menu = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Geo-menu")))
            # # Ожидание и выбор "Королёв"
            # city_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            #     (By.XPATH, "//ul[@id='Geo-menu']//li[contains(., 'Королёв')]")))
            # city_option.click()
            # # Проверка выбора
            # selected_text_city = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            #     (By.CSS_SELECTOR, "#Geo-button .ui-selectmenu-text"))).text
            #
            # # ПОЛНОЕ ОПИСАНИЕ (Сделать описание товара/услуги/вакансии более подробным (лучше > 100 символов))
            # input_field_desc = driver.find_element(By.ID, "AInfoForm_content")
            # input_field_desc.send_keys("Продам тренажер в отличном качестве. ТОЛЬКО WhatsApp (8-968-XXX-XX-XX)!!!\n"
            #                            "САМОВЫВОЗ!\nДокументы и чеки в наличии.")  # Можно поменять текст, который в кавычках
            #
            # # ЦЕНА ТОВАРА (Максимальное число символов - 11)
            # input_field_price = driver.find_element(By.ID, "AInfoForm_price")
            # input_field_price.send_keys("2900")  # Можно поменять текст, который в кавычках
            #
            # # СОГЛАСИЕ НА ТОРГ ПО ЦЕНЕ
            # # (Устанавливаем состояние чекбокса: в конце строки '.checked = false;' --> true - согласен, false - не согласен)
            # # (Обновляем связанное скрытое поле --> вторая строка '.value = "1";' --> согласен = 1, не согласен = 0)
            # # _____ПРИМЕЧАНИЕ____
            # # 'true' и 'false' - обязательно с МАЛЕНЬКОЙ БУКВЫ и ___БЕЗ__КАВЫЧЕК___!!
            # # В значении '.value = "X" - цифры "1" и "0" ОБЯЗТЕЛЬНО ___В__КАВЫЧКАХ___!!!
            # # ВАЖНО!!! в конце каждой строки кода (где нет символов //) ОБЯЗАТЕЛЬНЫЙ ЗНАК ___ТОЧКА С ЗАПЯТОЙ___ (;)!!!
            # driver.execute_script("""
            #     // Устанавливаем состояние чекбокса
            #     document.getElementById("AInfoForm_torg").checked = false;
            #     // Обновляем связанное скрытое поле
            #     document.getElementById("ytAInfoForm_torg").value = "0";
            #     // Триггерим события изменения
            #     const event = new Event("change", { bubbles: true });
            #     document.getElementById("AInfoForm_torg").dispatchEvent(event);
            # """)
            # time.sleep(0.5)  # чуток ждем, чтобы успели все события на форме сработать
            #
            # # АДРЕС (Максимальное число символов - 80)
            # input_field_address = driver.find_element(By.ID, "AInfoForm_address")
            # input_field_address.send_keys("ул. Орджоникидзе, д. 1")  # Можно поменять текст, который в кавычках
            #
            # # СОГЛАСИЕ НА ОБРАБОТКУ ПД
            # # (Обновляем скрытое поле --> часть кода и в конце '.value = "X";' --> согласен = 1, не согласен = 0)
            # # _____ПРИМЕЧАНИЕ____
            # # В значении '.value ="X" - цифры "1" и "0" ОБЯЗТЕЛЬНО ___В__КАВЫЧКАХ___!!!
            # # ВАЖНО!!! в конце каждой строки кода (где нет символов //) ОБЯЗАТЕЛЬНЫЙ ЗНАК ___ТОЧКА С ЗАПЯТОЙ___ (;)!!!
            # driver.execute_script("""
            #     document.getElementById("AInfoForm_is_agree").checked = true;
            #     // Триггерим события для обновления состояния
            #     const event = new Event("change", { bubbles: true });
            #     document.getElementById('AInfoForm_is_agree').dispatchEvent(event);
            #     // Обновляем скрытое поле
            #     document.getElementById("ytAInfoForm_is_agree").value = "0";
            # """)
            time.sleep(0.5)  # чуток ждем, чтобы успели все события на форме сработать

            # Выводим в текст в IDLE о работе функции
            print(f"Окончание работы скрипта в -= {time.strftime('%a %d.%m.%Y %H:%M:%S')} =-")

            while True:  # не закрываем браузер автоматически
                time.sleep(1)

        except Exception as e:  # описание ошибки, если она возникает
            print(f"Error: {e}", file=sys.stderr)
            time.sleep(10)


if __name__ == "__main__":  # запуск скрипта
    daemon = SiteDaemon_N555()  # создаем экземпляр класса демона 'SiteDaemon_N555()'
    daemon.run()  # запускаем демона, который выполняет функцию 'def run'

