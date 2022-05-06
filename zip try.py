from zipfile import ZipFile
from .App import link



with ZipFile(f'/home/mike/Downloads/{link}_', 'r') as zipObj:
   # Extract all the contents of zip file in different directory
   zipObj.extractall(f'/home/mike/Downloads/{link}/{link}_{i}')
   print('done')
