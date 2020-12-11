import os
import time
import random

os.system('git pull')
os.system('python app.py')
os.system('git add data.json')
os.system('git commit -m "trigger"')
os.system('git push -u origin master')