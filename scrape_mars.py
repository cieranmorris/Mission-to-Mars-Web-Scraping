#import dependencies for set up
from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
import pymongo
import pandas as pd
import datetime as dt

def scrape():
    #Set up splinter path and browser
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless = True)

    #indicate URL for scraping
    url = "https://redplanetscience.com"
    browser.visit(url)


    #Find the latest News Article and it's associated Paragraph Text
    #HTML object
    html = browser.html
        
    #Parse HTML with Beautiful Soup
    soup = bs(html, "html.parser")

    #Use find element to locate latest title
    article_title = browser.find_by_css(".content_title")[0].text
    
    #Use find element to locate paragraph text of this article
    paragraph_text = browser.find_by_css(".article_teaser_body")[0].text


    #Scrape for Mars Space Featured Image
    #Create URL and browser
    mars_image_url = "https://spaceimages-mars.com"
    browser.visit(mars_image_url)


    #HTML object
    mars_image_html = browser.html

    #Parse HTML with Beautiful Soup
    mars_image_soup = bs(mars_image_html, "html.parser")

    #Retrieve information for image link
    featured_mars_image = mars_image_soup.find("a", class_ = "showimg fancybox-thumbs")["href"]


    #Declare url under featured_image_url variable and save 
    featured_image_url = f"https://spaceimages-mars.com/{featured_mars_image}"



    #import URL for Mars Facts webpage
    mars_facts_url = "https://galaxyfacts-mars.com"

    #Use 'read_html' function to read tables into Jupyter Notebook
    tables = pd.read_html(mars_facts_url)


    #Select dataframe using indexing on the table
    mars_facts_df = tables[0]


    #Drop first row in DataFrame
    header_reset = mars_facts_df.iloc[0]
    mars_facts_df = mars_facts_df[1:]   


    #Pass new header into DataFrame to clean it
    mars_facts_df.columns = header_reset

    mars_facts_table = mars_facts_df.to_html()


    #Mars Hemispheres Scraping
    mars_hemispheres_url = "https://marshemispheres.com"
    browser.visit(mars_hemispheres_url)


    #HTML Object
    hemispheres_html = browser.html

    #Parse with Beautiful Soup
    hemispheres_soup = bs(hemispheres_html, "html.parser")


    #look for links in order to access full resolution hemisphere images
    hemispheres_links = hemispheres_soup.find_all("div", class_ = "")


    #find anchor links and place into a links list for future for loop
    hemispheres_image_links = []




    #For loop to search for Hemisphere title and full resolution image
    links = browser.find_by_css("a.itemLink img")

    print(links)

    for i in range(len(links)):
        img_hemisphere = {}
        
        browser.find_by_css("a.product-item img")[i].click()
        
        img = browser.links.find_by_text("Sample").first
        

        print(img["href"])
        
        img_hemisphere["img_url"] = img["href"]
        
        img_hemisphere["title"] = browser.find_by_css("h2.title").text
        
        hemispheres_image_links.append(img_hemisphere)
        
        browser.back()


    #Put scraped items into single dictionary
    scrape_dictionary = {

        "article_title": article_title,
        "paragraph_text": paragraph_text,
        "featured_image": featured_image_url,
        "mars_facts": mars_facts_table,
        "hemisphere_links": hemispheres_image_links,
        "scrape_date": dt.datetime.now()

    }

    browser.quit()

    return scrape_dictionary

