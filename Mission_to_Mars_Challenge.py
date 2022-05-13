# %%
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.firefox import GeckoDriverManager

# %%
# Set up Splinter
executable_path = {'executable_path': GeckoDriverManager().install()}
browser = Browser('firefox', **executable_path, headless=False)

# %%
# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)

# %%
# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')

# %%
# Scrape the Title
title = html_soup.find('h2').text
title

# %%
# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)

# %%
url = 'http://quotes.toscrape.com/'
browser.visit(url)

# %%
for x in range(1, 6):
   html = browser.html
   quote_soup = soup(html, 'html.parser')
   quotes = quote_soup.find_all('span', class_='text')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
   browser.links.find_by_partial_text('Next').click()

# %%
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from requests_html import HTMLSession
session = HTMLSession()

# %%
# Set up Splinter
executable_path = {'executable_path': GeckoDriverManager().install()}
browser = Browser('firefox', **executable_path, headless=False)

# %%
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# %%
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')

# %%
slide_elem.find('div', class_='content_title')

# %%
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# %%
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# %%
# Visit URL
url = 'https://spaceimages-mars.com'
response = session.get(url)
browser.visit(url)

# %%
# Parse the resulting html with soup
html = browser.html
img_soup = soup(response.content, 'html.parser')

# %%
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# %%
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# %%
import pandas as pd

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

# %%
browser.quit

# %%
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set the executable path and initialize Splinter
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# Set up Splinter
executable_path = {'executable_path': EdgeChromiumDriverManager().install()}
browser = Browser('edge', **executable_path, headless=False)

### Visit the NASA Mars News Site
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p
### JPL Space Images Featured Image
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup
# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url
### Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df
df.to_html()

# %%
# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
### Hemispheres
# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/'

browser.visit(url)


# %%
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []



# %%
# 3. Write code to retrieve the image urls and titles for each hemisphere.
for x in range(0,4):
    img_link_loc = browser.find_by_tag('h3')[x]
    img_link_loc.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    img_url_rel = img_soup.find('img', class_='wide-image').get('src')
    # Use the base URL to create an absolute URL
    img_url = f'https://astrogeology.usgs.gov/{img_url_rel}'
    img_title = img_soup.find('h2', class_='title').text
    
    hemisphere_image_urls.append({'img': img_url_rel, 'title': img_title})
    
    browser.back()

# %%
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# %%
# 5. Quit the browser
browser.quit()

# %%



