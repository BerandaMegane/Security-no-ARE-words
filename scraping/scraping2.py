# 公式
import datetime
import re
import time

# サードパーティ
from bs4 import BeautifulSoup
import requests

"""
@ITのページから放送回一覧を作成するためのスクリプト
（メンテナンスはしていません）
"""

def are_search():
    are_list = list()
    
    # 取得
    url = "https://atmarkit.itmedia.co.jp/ait/series/2517/index.html"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    # soup.prettify("utf-8")

    posts = soup.find_all("div", class_="colBoxIndex")
    for post in posts:

        # 日付のタイムゾーン
        JST = datetime.timezone(datetime.timedelta(hours=9), "JST")

        # title
        try:
            titlebox = post.find(class_="colBoxTitle").find("h3")
            title = titlebox.find("a").getText()
        except:
            title = "are"
            pass
        # URL
        try:
            url = titlebox.find("a")["href"]
        except:
            url = "http://are"
        # 公開日
        try:
            published = post.find("time")["datatime"]
        except:
            published = datetime.datetime(1900, 1, 1, tzinfo=JST)
        
        are = {
            "title": title,
            "url": url,
            "published": published,
        }
        # print(are)
        are_list.append(are)
        
    return are_list


def output(are_list):
    print("title",",", "published",",", "url")
    for are in are_list:
        print(are["title"],",", are["published"],",", are["url"])

if __name__ == "__main__":
    # are_search()
    are_list = are_search()
    output(are_list)
