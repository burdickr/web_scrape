from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)


def scrape():
    # returns title and paragraph for news 
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title = soup.find("div", class_='content_title').get_text()
    news_body = soup.find("div", class_='article_teaser_body').get_text()
    # featured image
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    featured_image = soup.find_all('img')[3]["src"]
    featured_image_url = ("https://www.jpl.nasa.gov" + featured_image)
    # mars weather
    url3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url3)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    weather = soup.find("p", class_='tweet-text').get_text()
    # returns table from space facts 
    url4 = "https://space-facts.com/mars/"
    browser.visit(url4)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    space_facts = soup.find("tbody").get_text()
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    # hemisphere info 
    url5 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url5)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    hemispheres = []
    image_urls = []
    # loop to find hemisphere names
    for hemisphere in soup.find_all('h3'):
        hemispheres.append(hemisphere.get_text())
    # loop to find image urls 
    for hemisphere in hemispheres:
        browser.click_link_by_partial_text(hemisphere)
        html = browser.html
        soup = BeautifulSoup(html)
        div = soup.find('div', class_='downloads')
        list_ = div.find('li')
        img_url = list_.a['href']
        image_urls.append(img_url)
        browser.back()
    hemisphere_image_urls = dict(zip(hemispheres, image_urls))
    h_1_title = list(hemisphere_image_urls.keys())[0]
    h_2_title = list(hemisphere_image_urls.keys())[1]
    h_3_title = list(hemisphere_image_urls.keys())[2]
    h_4_title = list(hemisphere_image_urls.keys())[3]
    h_1_img = list(hemisphere_image_urls.values())[0]
    h_2_img = list(hemisphere_image_urls.values())[1]
    h_3_img = list(hemisphere_image_urls.values())[2]
    h_4_img = list(hemisphere_image_urls.values())[3]
    mars_data = {"news_title": news_title,
             "news_body": news_body,
             "featured_image_url": featured_image_url,
             "weather": weather,
             "space_facts": space_facts,
             "h_1_title": h_1_title, 
             "h_2_title": h_2_title,
             "h_3_title": h_3_title,
             "h_4_title": h_4_title,
             "h_1_img": h_1_img,
             "h_2_img": h_2_img,
             "h_3_img": h_3_img,
             "h_4_img": h_4_img
                }
    return mars_data