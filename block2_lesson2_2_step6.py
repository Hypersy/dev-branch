from math import sin
from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html" 
    driver = webdriver.Chrome()
    driver.get(link)

    def calc(x): 
       return str(math.log(abs(12*math.sin(int(x)))))

    x_element = driver.find_element_by_id('input_value').text
    y = calc(x_element)

    driver.execute_script("window.scrollBy(0, 100);")
    inter = driver.find_element_by_id("answer")
    inter.send_keys(y)
    
    button = driver.find_element_by_css_selector("#robotCheckbox") .click()
    button = driver.find_element_by_css_selector("#robotsRule") .click()
    button = driver.find_element_by_css_selector("button.btn") .click()
    assert True

    time.sleep(3)


finally:
    time.sleep(10)
    driver.quit()
    #Спасибо!