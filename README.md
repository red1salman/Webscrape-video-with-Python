# Webscrape-video-with-Python

A simple webscrape that takes the xpath of a youtube video from the webpage elements and opens the video on a browser. 

A simple web scrape that takes the xpath of a youtube video from the webpage elements and opens the video on a browser. 

The project was done on VMware ubuntu virtual machine. The python script is written in a virtual environment named "env". 

We import WebDriver from Selenium. Selenium is an automation tool and Selenium Webdriver tool is used for automating web application to verify that it works as expected or not. For the webdriver to work it needs the chromedriver which is implemented as a WebDriver remote server that instructs the browser what to do by exposing Chrome's internal automation proxy interface. 

 

Problem with using selenium for webscraping: If the website that is being scraped has some sort of javascript protection then that will prevent doing a direct http request. Better to go with a headless browser.
