import inserter
import pandas as pd
from selenium import webdriver
import logging

# Initialize logging file
logging.basicConfig(filename='imdb.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# path to webdriver
wb_path = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=wb_path)


def perform_insertion(data):
    """
    @param data: pandas DataFrame
    @return: None
    Performs all the steps of finding movie, opening movie card and rating movie for each movie passed in the file.
    """
    inserter.login_phase(driver)   # Step 1 - logging in
    for index, row in data.iterrows():
        movie_title = row['title']         # make sure DataFrame you are passing in has column named 'title'
        rate = str(int(row['rating']))     # make sure DataFrame you are passing in has column named 'rating'
        inserter.searching_phase(driver, movie_title)   # Step 2 - searching for a certain movie
        inserter.picking_movie_phase(driver, movie_title)   # Step 3 - picking the right movie card
        if inserter.rate_the_movie(driver, movie_title, rate):   # Step 4 - rating the movie
            print(f'Successfully update rating for {movie_title} with rating: {rate}')


if __name__ == '__main__':
    print('Please type path to the data file.')
    filename = input()
    df = pd.read_pickle(filename)
    perform_insertion(df)









