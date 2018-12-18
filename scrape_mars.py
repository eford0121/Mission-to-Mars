import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup
from splinter import Browser
import requests
from splinter.exceptions import ElementDoesNotExist

def scrape():
    #Executable path
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    #dictionary to store data
    mars_data = {}


    #############Nasa News##################
    #Use splinter module to visit Nasa news
    url= 'https://mars.nasa.gov/news/'
    browser.visit(url)
    #html object
    html=browser.html
    #Parse through HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    #Latest headline and blurb
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find("div",class_="article_teaser_body").text
    #enter into mars_data
    mars_data["news story"] = (news_title,news_p)
    #Print valuesp
    print(news_title)
    print(news_p)

    ############### Featured Image ################

    #Url #2
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    #Click on appropriate link
    button = browser.find_by_id("full_image")
    button.click()
    #Click on second appropriate link
    time.sleep(5)
    browser.click_link_by_partial_text("more info")
   
    #html and Beautiful Soup 
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #Obtain image source
    image = soup.find("img", class_= 'main_image').get('src')
    #Put it all together
    featured_image_url = f'https://www.jpl.nasa.gov{image}'
    #enter into mars_data 
    mars_data["featured image"] = (featured_image_url)
    #print url
    print(featured_image_url)

    ############ Mars Weather #####################
    #Url 3
    url_3 ="https://twitter.com/marswxreport?lang=en"
    browser.visit(url_3)
    #Beautiful soup object
    html=browser.html
    soup = BeautifulSoup(html, 'html.parser')
    #scraping what I need
    mars_weather= soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    #enter into mars_data
    mars_data["mars weather"] = (mars_weather)
    #print weather
    print(mars_weather)

    ######### Mars Facts ############

    #url 4
    url_4 = "https://space-facts.com/mars/"
    browser.visit(url_4)

    #obtain table data
    table = pd.read_html(url_4)[0]
    #Rename columns
    renamed_table = table.rename(columns= {0 : "Mars Profile",
                      1: "Value"})
    #Make an HTML object
    mars_html = renamed_table.to_html()
    #removed /n
    mars_html = mars_html.replace('\n', ' ')
    #save to mars_data
    mars_data["Mars Facts"] = (mars_html)

    ############ Mars Hemispheres ##########
    #url_5
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)
    #Cerberus
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    cerberus_title = soup.find("h2", class_='title').text
    browser.click_link_by_partial_href('http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg')
    cerberus_url = (str(browser.url))
    #back to main page
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)
    #Schiaparelli
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    schiaparelli_title = soup.find("h2", class_='title').text
    browser.click_link_by_partial_href('http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg')
    schiaparelli_url = (str(browser.url))
    #back to main page
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)
    #Syrtis Major 
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    syrtis_title = soup.find("h2", class_='title').text
    browser.click_link_by_partial_href('http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg')
    syrtis_url = (str(browser.url))
    #back to main page
    url_5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_5)
    #Valles Marineris
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    valles_title = soup.find("h2", class_='title').text
    browser.click_link_by_partial_href('http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg')
    valles_url = (str(browser.url))

    #hemisphere_image_urls
    hemisphere_image_urls=[
    {"title" : cerberus_title, "img_url": cerberus_url},
    {"title" : schiaparelli_title, "img_url": schiaparelli_url},
    {"title" :syrtis_title, "img_url": syrtis_url},
    {"title" : valles_title, "img_url": valles_url}]

    #put into mars_data
    mars_data["Mars Hemispheres"] = (hemisphere_image_urls)


    return(mars_data)

print(scrape())







    



    





    





    





