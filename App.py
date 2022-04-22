from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
path = "./Crome_driver/chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://w13.mangafreak.net/Manga/Solo_Leveling")

i = 8

while True:

    downlaod = driver.find_element_by_xpath(f'//a[contains(@href,"https://images.mangafreak.net/downloads/Solo_Leveling_{i}")]')
    downlaod.click()
    i = i + 1

    time.sleep(10)

