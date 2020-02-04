import inserter
import pandas as pd
from selenium import webdriver

# loading file with movie ratings as DataFrame from file
df = pd.read_pickle('ratings.pkl')

# path to webdriver
wb_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=wb_path)

inserter.login_phase(driver)
