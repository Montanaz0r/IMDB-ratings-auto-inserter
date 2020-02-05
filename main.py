import inserter
import pandas as pd
from selenium import webdriver
import logging

# Initialize logging file
logging.basicConfig(filename='imdb.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# loading file with movie ratings as DataFrame from file
# df = pd.read_pickle('ratings4.pkl')

# path to webdriver
wb_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=wb_path)


def perform_insertion(data):
    inserter.login_phase(driver)
    for index, row in data.iterrows():
        movie_title = row['title']
        rate = str(int(row['rating']))
        inserter.searching_phase(driver, movie_title)
        inserter.picking_movie_phase(driver, movie_title)
        if inserter.rate_the_movie(driver, movie_title, rate):
            print(f'Successfully update rating for {movie_title} with rating: {rate}')
            row['scraped'] = 'Yes'
    data.to_csv('ratings_updated.csv')


if __name__ == '__main__':
    print('Please type path to the data file.')
    filename = input()
    df = pd.read_pickle(filename)
    perform_insertion(df)









