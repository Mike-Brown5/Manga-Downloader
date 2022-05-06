from selenium import webdriver
from zipfile import ZipFile
import time
path = "./Crome_driver/chromedriver"

driver = webdriver.Chrome(path)

link = input("Enter ur link for the manga: ")
Flink = link[:33]
link = link[33:]

driver.get(f"{Flink}{link}")

print(Flink)
print(link)

q = int(input("enter the last chapter you have: "))

i = q + 1

try:
    while True:

        downlaod = driver.find_element_by_xpath(f'//a[contains(@href,"https://images.mangafreak.net/downloads/{link}_{i}")]')
        downlaod.click()
        with ZipFile(f'/home/mike/Downloads/{link}_{i}.zip', 'r') as zipObj:
        # Extract all the contents of zip file in different directory
            zipObj.extractall(f'/home/mike/Downloads/Manga/{link}/{link}_{i}')
        i = i + 1

        time.sleep(5)
except:
    downlaod.quit()
