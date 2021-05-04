# Mission to Mars Web Scraping 

## Background Information

This project encompassed the creation of a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

* Initial scraping was completed using programming dependencies including Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* Website design utitiles HTML with Bootstrap templates.

### NASA Mars News Title and Paragraph Text

* One website of interest to scrape and collect information regarding the Mission to Mars was the [Mars News Site](https://redplanetscience.com/). Importantly, the latest News Title and Paragraph Text were scraped and saved to variables for application in the Flask and MongoDB database.

### JPL Mars Space Images - Featured Image

* Current images of the surface of Mars are available for visualization through the [Featured Space Image site](https://spaceimages-mars.com). Using Splinter to navigate the site and BeautifulSoup to parse the data, the current full sized `.jpg` Featured Mars Image was scraped and it's complete URL link was saved into a variable for future application.

### Mars Facts

* The [Mars Facts webpage](https://galaxyfacts-mars.com) uses a data table to present Mars facts including Diameter, Mass, and Surface Temperature. Pandas was used to scrape this table and convert it to an HTML table string, which is then displayed on the landing page of the newly generated HTML website.

### Mars Hemispheres

* High resolution images of each pf Mars' hemispheres are located on the [Mars hemispheres astrogeology site](https://marshemispheres.com/) Each full resolution image was scraped and prepared to be loaded into the MongoDB database in the following steps. Both the URLs for the full resolution image and the titles of each hemisphere were stored in a Python dictionary and then appended to a list to easily transfer to the HTML webpage.

## MongoDB and Flask Application

Once the data was scraped and prepped in variables and lists, MongoDB and Flask were used to create a new HTML page that displays all of the information that was contained in the original URLs. 

* The original Jupyter notebook was turned into a Python script (`scrape_mars.py`) using the `scrape` function, which combines all of the scraping code from above and returns one complete Python dictionary.

* A Flask route `/scrape` was also created to call to the `scrape_mars.py` script for the scraped data. The return value for this requests was stored in Mongo as a Python dictionary.

* Finally, a root route `/` was generated to query the Mongo database and pass the mars data into the HTML template and display the data.

* The `index.html` file was generated to take the mars data dictionary and display all of the data in the appropriate HTML elements.
- - -

### Copyright

Trilogy Education Services © 2021. All Rights Reserved.
