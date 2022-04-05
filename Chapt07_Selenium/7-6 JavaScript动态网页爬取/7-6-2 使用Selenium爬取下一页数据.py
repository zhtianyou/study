from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://www.nba.com/stats/players/traditional/?sort=PTS&dir=-1"
driver = webdriver.Chrome("//Users/youwin/PycharmProjects/chromedriver")
driver.implicitly_wait(10)
driver.get(url)

pages_remaining = True
page_num = 1
while pages_remaining:
    soup = BeautifulSoup(driver.page_source, "lxml")
    table = soup.select_one(".stats-table-pagination__next > table")
    df = pd.read_html(str(table))
    df[0].to_csv("ALL_players_stats" + str(page_num) + ".csv")
    print("存储页面：", page_num)

