#Login to Twitter using Selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')

#Data needed to login
numbers_list = []
#Create a Chrome driver
driver = webdriver.Chrome(chrome_options=chrome_options)


i = 000
while i < 1000:
  numbers_list.append(i)
  i += 1


for x in numbers_list:
  print(x)
  driver.get(f"https://www.kiwiplates.nz/create/?combination={x}&vt=1")
  element = driver.find_element_by_xpath("//*[@id='gatsby-focus-wrapper']/div/div/div[2]/div[4]/div/div/div[2]/div[1]/div/div[1]/div/div[3]")
  if element.text == 'Your Combination is Available!':
    print(f"{x}: {element.text}")