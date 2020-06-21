from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Chrome('./chromedriver') as driver:
    driver.get("https://books.goalkicker.com/")
    eles = driver.find_elements_by_xpath("//a[@target='_blank']")
    eles.pop(0)
    for i in eles:
        i.click()
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        driver.switch_to_window(driver.window_handles[1])
        driver.find_element_by_class_name('download').click()
        driver.close()
        driver.switch_to_window(driver.window_handles[0])