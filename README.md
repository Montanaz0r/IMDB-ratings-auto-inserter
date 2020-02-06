# IMDB-ratings-auto-inserter
A Python script that enables auto-inserting movie ratings into the IMDB profile.

## Table of contents:

* [Usage](#Usage)
* [Requirements](#Requirements)
* [Brief description](#Brief-description)
* [Quick Tutorial](#quick-tutorial)
* [Contact](#Contact)

## Usage:
1. ``` https://github.com/Montanaz0r/IMDB-ratings-auto-inserter.git ```
2.  ```pip install -r requirements.txt ```
3.  ```python main.py ```

## Requirements:
The environment I was working with while doing this project was, a bit, messy you can find necessary packages below:

pandas==1.0.0   
selenium==3.141.0   
ChromeWebdriver (link: https://selenium-python.readthedocs.io/installation.html#downloading-python-bindings-for-selenium)

## Brief description:

The inserter was built in Python 3.8 and it is using Selenium with Chrome Webdriver to insert ratings. 
You can pass your data as a pickle file. I have used the script to push in Filmweb ratings, which I have scraped previously.
In a quick tutorial section, you can find more useful information regarding potential usage.

## Quick Tutorial

**1. Preparing Data**

Save your data as a .pkl file (this can be generated with Pandas). **Make sure that the column name with your movies is named *title*
and ratings are in column named *rating* (you do not need to change datatype in this column, script will automatically convert
all ratings to strings).**

There is a file named: ratings4.pkl in my respository. You can use this data to play/test the script.

**2. Run main.py**

The script will ask you to input the path to your data file (if you store your data in the same directory, you can just pass the filename).
Afterward, the script will automatically initiate Chromediver by opening *imdb.com* main page.

**3. Login phase**

The script will be running and waiting for you to pass credentials manually into the IMDB page that was opened for you. 
After you log yourself in the script will immediately start searching movies and inserting your ratings. 
You will no longer have to take any actions. Go and grab some :coffee: :coffee: :coffee:

With each successful insertion, the script will be printing out information. Just like this:

```Successfully update rating for Reign of the Supermen with rating: 8```   
```Successfully update rating for The Death of Superman with rating: 8```  
```Successfully update rating for Atomic Blonde with rating: 3```

**4. Logs**

In some cases, there is a variation between movie titles on IMBd and other services. Therefore, the script might not be able to find
certain titles, even though, there is additional functionality that tries to match titles that do not entirely overlap.
After the script is no longer running you can access ***imdb.log*** file which was automatically created for you, and check 
which titles or ratings were not inserted into your IMDb account.

## Contact

Feel free to send me feedback at montana102@gmail.com
