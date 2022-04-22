from selenium import webdriver
import time
path = "./Crome_driver/chromedriver"

driver = webdriver.Chrome(path)

driver.get("https://w13.mangafreak.net/Manga/Solo_Leveling")

i = 8

while True:

    downlaod = driver.find_element_by_xpath(f'//a[contains(@href,"https://images.mangafreak.net/downloads/Solo_Leveling_{i}")]')
    downlaod.click()
    i = i + 1

    time.sleep(5)

