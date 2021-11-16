#!/usr/bin/env python
import os
import logging

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


driver_to_use = 'geckodriver'
driver_path = os.path.abspath(driver_to_use)
driver = webdriver.Firefox(executable_path=driver_path)
driver.maximize_window()


def mail_yandex_login(url):
    """
    :param url: https://mail.yandex.ru
    :return: None
    """
    delay = 10
    try:
        driver.get('https://mail.yandex.ru')

        WebDriverWait(driver, delay).until(
            ec.presence_of_element_located(
                (By.CLASS_NAME, 'HeadBanner-Button-Enter')
            )
        )
        login_button = driver.find_element(By.CLASS_NAME, 'HeadBanner-Button-Enter')
        login_button.send_keys(Keys.ENTER)

        WebDriverWait(driver, delay).until(
            ec.presence_of_element_located(
                (By.ID, 'passp-field-login')
            )
        )
        login_input_area = driver.find_element(By.ID, 'passp-field-login')
        login_input_area.clear()
        login_input_area.send_keys('qa.testing2021')
        login_input_area.send_keys(Keys.ENTER)

        WebDriverWait(driver, delay).until(
            ec.presence_of_element_located(
                (By.ID, 'passp-field-passwd')
            )
        )
        password_input_area = driver.find_element(By.ID, 'passp-field-passwd')
        password_input_area.clear()
        password_input_area.send_keys('qa.testing20212021')
        password_input_area.send_keys(Keys.ENTER)

        WebDriverWait(driver, delay).until(
            ec.presence_of_element_located(
                (By.XPATH, '//button[@data-t="button:pseudo"]')
            )
        )
        skip = driver.find_element(By.XPATH, '//button[@data-t="button:pseudo"]')
        skip.send_keys(Keys.ENTER)

    except TimeoutException as time_ex:
        logging.error(time_ex)

    except Exception as ex:
        logging.error(f'Got en exception: {ex}')


if __name__ == '__main__':
    mail_yandex_login('https://mail.yandex.ru')
