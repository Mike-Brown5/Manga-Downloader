from selenium import webdriver
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
        i = i + 1

        time.sleep(5)
except:
    downlaod.quit()

export