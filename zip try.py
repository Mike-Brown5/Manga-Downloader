from zipfile import ZipFile
import os

link = input("Enter ur link for the manga: ")

link = link[33:]


q = int(input("enter the last chapter you have: "))

i = q + 1
try:
    while True:
        with ZipFile(f'/home/mike/Downloads/{link}_{i}.zip', 'r') as zipObj:
        # Extract all the contents of zip file in different directory
            zipObj.extractall(f'/home/mike/Downloads/Manga/{link}/{link}_{i}')
            print('done')
            i = i +1
except:
    print("Exiting program due to an error")