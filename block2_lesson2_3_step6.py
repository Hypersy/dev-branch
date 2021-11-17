from selenium import webdriver
import time
import os 
import math

try: 
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    button = browser.find_element_by_css_selector("div .trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x): 
       return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element_by_id('input_value').text
    y = calc(x_element)

    #driver.execute_script("window.scrollBy(0, 100);")
    inter = browser.find_element_by_id("answer")
    inter.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn") .click()

    assert True

    time.sleep(3)


finally:
    time.sleep(10)
    driver.quit()


