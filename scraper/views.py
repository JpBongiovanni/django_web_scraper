# from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
import json
from decouple import config
import pandas as pd
from pandas import read_json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN") or config("GOOGLE_CHROME_BIN")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=r'C:/selenium_drivers/chromedriver.exe' or os.environ.get("CHROMEDRIVER_PATH") or config('CHROMEDRIVER_PATH'), chrome_options=options)


def index(request):
    os.environ['PATH'] += r"C:/selenium_drivers/chromedriver"

    # options = Options()
    # options.headless = True
    # driver = webdriver.Chrome(options=options)
    # options.add_argument("headless")

    driver.get("https://www.speedrun.com/smrpg")

    get_stats = driver.find_element(By.XPATH, '//a[@href="/smrpg/gamestats"]')
    get_stats.click()
    # driver.implicitly_wait(3)
    matches = driver.find_elements(By.CLASS_NAME, "row")

    all_text = []
    split_text = []

    stat_title = []
    stat_value = []

    for match in matches:
        all_text.append(match.text)

    for text in all_text:
        split_text.append(text.split("\n"))

    slice_text = split_text[2:]

    for idx in slice_text:
        stat_title.append(idx[0])
        stat_value.append(idx[1])

    stat_dict = {}
    for key in stat_title:
        for value in stat_value:
            stat_dict[key] = value
            stat_value.remove(value)
            break

    stat_dict = json.dumps(stat_dict)
    load_stats = json.loads(stat_dict)

    # df = pd.DataFrame({'Stats': stat_title, 'Stat Value': stat_value})

    # df = df.to_dict()

    return JsonResponse(load_stats, safe=False)
