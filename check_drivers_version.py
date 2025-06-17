from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Инициализация драйвера с явным созданием Service
service = Service(ChromeDriverManager().install())  # pip install --upgrade webdriver-manager
# driver = webdriver.Chrome(service=service)

options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Путь к Chrome
driver = webdriver.Chrome(options=options, service=service)

# Проверка capabilities (добавлена обработка возможных ошибок)
try:
    print("Браузер:", driver.capabilities['browserName'])
    print("Версия Chrome:", driver.capabilities['browserVersion'])
    print("Версия ChromeDriver:", driver.capabilities['chrome']['chromedriverVersion'])
except KeyError as e:
    print(f"Ошибка доступа к данным: {e}")

# Пример работы с реальным элементом (для проверки)
driver.get("https://gde.ru")
title = driver.find_element(By.TAG_NAME, "h1").text
print("Заголовок страницы:", title)

# Корректное закрытие
driver.quit()