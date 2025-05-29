import time
import sys
import signal
import webbrowser


class SiteDaemon:  # создаем класс демона 'SiteDaemon'
    def __init__(self):
        self.running = True
        signal.signal(signal.SIGTERM, self.handle_signal)
        signal.signal(signal.SIGINT, self.handle_signal)

    def handle_signal(self, signum, frame):
        self.running = False

    def run(self):  # функция для запуска демона и выполнения описанных действий
        # while self.running:  # выполняется постоянно, пока не происходит ошибка
        try:
            # !!!!! добавляем адреса сайтов (в кавычках и через запятую. В конце точку не ставить) !!!!!
            url_site = ["https://gde.ru/cabinet-login"]

        # for i in range(len(url_site)):  # перебор сайтов, указанных в 'url_site'
            URL_address = url_site[0]  # берем первый адрес сайта в списке 'url_site'
            webbrowser.open(URL_address, new=0)  # открываем ссылку в браузере в новой вкладке
            # выводим в текст в IDLE о работе функции
            print(f"Начало работы скрипта в {time.strftime('%a %d.%m.%Y %H:%M:%S')}. Переход на сайт: \"{url_site}\"")
            time.sleep(5)  # ждем 5 секунд
        # i += 1  # берем следующий адрес сайта (второй, третий...)
        except Exception as e:  # описание ошибки, если она возникает
            print(f"Error: {e}", file=sys.stderr)
            time.sleep(10)


if __name__ == "__main__":  # запуск скрипта
    daemon = SiteDaemon()  # создаем экземпляр класса демона 'SiteDaemon()'
    daemon.run()  # запускаем демона, который выполняет функцию 'def run'
