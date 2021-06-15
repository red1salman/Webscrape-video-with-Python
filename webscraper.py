from selenium import webdriver

url = 'https://www.youtube.com/c/JacobGeller/videos'
browser = webdriver.Chrome("/home/redwan/Projects/Webscrape with Python/chromedriver")
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()

