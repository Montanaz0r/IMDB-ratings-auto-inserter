import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def login_phase(driver):
    """
    :params: driver
    :returns: None
    taking care of opening main page and waiting for user in order to log in
    """
    driver.get("https://www.imdb.com/")
    try:
        user = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                               "#imdbHeader > div.ipc-page-"
                                                                               "content-container.ipc-page-"
                                                                               "content-container--center."
                                                                               "navbar__inner > "
                                                                               "div._3cMNCrSVkxQhCkVs1JLIib.navbar__"
                                                                               "user.sc-kgoBCf.iTQkiJ > div > "
                                                                               "label.ipc-button.ipc-button--"
                                                                               "single-padding.ipc-button--default-"
                                                                               "height.ipc-button--core-baseAlt.ipc-"
                                                                               "button--theme-baseAlt.ipc-button--"
                                                                               "on-textPrimary.ipc-text-button.navbar__"
                                                                               "flyout__text-button-after-mobile."
                                                                               "navbar__user-menu-toggle__button "
                                                                               "> div > span")))

        print(f"Logged in as: {user.text}")
    except TimeoutException:
        print('Timeout exception - you have not logged in, please run the script again')
        driver.close()


def searching_phase(driver, movie_title):
    searching_bar = driver.find_element(By.CSS_SELECTOR, '#suggestion-search')
    searching_bar.click()
    searching_bar.send_keys(movie_title)
    searching_bar.send_keys(Keys.ENTER)


def picking_movie_phase(driver, movie_title):
    try:
        movie_page = driver.find_element_by_link_text(movie_title)
    except NoSuchElementException:
        print(f'Could not find any movie that matches search for: {movie_title}')

    else:
        movie_page.click()


