from selenium import webdriver
from zipfile import ZipFile
import time
path = "./Crome_driver/chromedriver"
try:
    driver = webdriver.Chrome(path)

    link = input("Enter ur link for the manga: ")
    Flink = link[:33]
    link = link[33:]

    driver.get(f"{Flink}{link}")

    print(Flink)
    print(link)
except:
    print("You can download chrome driver from here https://chromedriver.chromium.org/downloads")
    quit()
q = int(input("enter the last chapter you have: "))

i = q + 1

try:
    while True:

        download = driver.find_element_by_xpath(f'//a[contains(@href,"https://images.mangafreak.net/downloads/{link}_{i}")]')
        download.click()

        print("Downloading......")
        time.sleep(8)
        with ZipFile(f'/home/mike/Downloads/{link}_{i}.zip', 'r') as zipObj:
        # Extract all the contents of zip file in different directory
            zipObj.extractall(f'/home/mike/Downloads/Manga/{link}/{link}_{i}')
        i = i + 1
        print(f"Done: {link}_{i}")
except:
    download.quit()
