import inserter
import pandas as pd
from selenium import webdriver

# loading file with movie ratings as DataFrame from file
df = pd.read_pickle('ratings2.pkl')

# path to webdriver
wb_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=wb_path)

movie_title = 'Reign of the Supermen'

inserter.login_phase(driver)
inserter.searching_phase(driver, movie_title)
inserter.picking_movie_phase(driver, movie_title)