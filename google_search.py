#!/usr/bin/env python
import logging
import os

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


def google_search_result(url):
    """
    :param url: https://google.com
    :return: None
    """
    delay = 10
    try:
        driver.get(url=url)
        WebDriverWait(driver, delay).until(
            ec.presence_of_element_located(
                (By.CLASS_NAME, 'gLFyf')
            )
        )
        search_bar = driver.find_element(By.CLASS_NAME, 'gLFyf')
        search_bar.clear()
        search_bar.send_keys('купить кофемашину bork c804')
        search_bar.send_keys(Keys.ENTER)
        # For more results in mvideo.ru website we can use line 32 call
        # search_bar.send_keys('site:mvideo.ru & intext:купить кофемашину bork c804')
    except TimeoutException as time_ex:
        logging.error(time_ex)
    except Exception as ex:
        logging.error(f'Got en exception: {ex}')


if __name__ == '__main__':
    google_search_result('https://google.com')
