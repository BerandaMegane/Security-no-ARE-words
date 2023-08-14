# 公式
import datetime
import re
import time

# サードパーティ
from bs4 import BeautifulSoup
import requests

"""
ポッドキャスト公式ページから放送回一覧を作成するためのスクリプト
（メンテナンスはしていません）
"""

def are_search():
    are_list = list()
    
    end_page = 22
    for page in range(1, end_page+1):
        url = "https://www.tsujileaks.com/?cat=3&paged=%d" % page
        response = requests.get(url)
        are_list.extend(are_page_search(response))
    
    return are_list

def are_page_search(response):
    are_list = list()

    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('div', class_="post")
    for post in posts:

        # 日付のタイムゾーン
        JST = datetime.timezone(datetime.timedelta(hours=9), "JST")

        # title
        storytitle = post.find("h2", class_="storytitle")
        title = storytitle.getText()
        # 放送回
        num = int(title.split("回")[0][1:])
        # URL
        url = storytitle.find("a")["href"]
        # 公開日
        published = post.find("b", class_="published")["title"]
        try:
            published = datetime.datetime.fromisoformat(published)
        except:
            published = datetime.datetime(1900, 1, 1, tzinfo=JST)
        # 収録日
        try:
            pattern = r'(\d{4})年(\d{2})月(\d{2})日'
            match_text = post.find("p", string=re.compile(pattern))
            match = re.search(pattern, match_text.getText())
            if match:
                year = int(match.group(1))
                month = int(match.group(2))
                day = int(match.group(3))
                
                recorded = datetime.datetime(year, month, day, tzinfo=JST)
        except:
            recorded = datetime.datetime(1900, 1, 1, tzinfo=JST)
        
        are = {
            "num": num,
            "title": title,
            "url": url,
            "published": published,
            "recorded": recorded,
        }
        # print(are)
        are_list.append(are)
    return are_list

def output(are_list):
    print("num",",", "title",",", "published",",", "recorded",",", "url")
    for are in are_list:
        print(are["num"],",", are["title"],",", are["published"].strftime("%Y-%m-%d %H:%M"),",", are["recorded"].strftime("%Y-%m-%d", ),",", are["url"])

if __name__ == "__main__":
    are_list = are_search()
    output(are_list)
