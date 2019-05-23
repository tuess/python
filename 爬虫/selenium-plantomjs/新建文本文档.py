from selenium import webdriver

#Edge驱动不匹配···
driver = webdriver.Edge("F:\\Python\\msedgedriver.exe")
driver.get("https://www.baidu.com")

input = driver.find_element_by_css_selector('#kw')
input.send_keys("照片")

button = driver.find_element_by_css_selector('#su')
button.click()
