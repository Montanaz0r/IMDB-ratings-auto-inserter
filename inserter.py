import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def login_phase(driver):
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