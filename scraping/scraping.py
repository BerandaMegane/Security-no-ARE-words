# 公式
import datetime
import json
import re

# サードパーティ
from bs4 import BeautifulSoup
import requests

"""
ポッドキャスト公式ページから放送回一覧を作成するためのスクリプト
（メンテナンスはしていません）
"""

def are_search():
    are_list = list()
    
    end_page = 30
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

        # print(post)

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
                
                recorded = datetime.date(year, month, day)
        except:
            recorded = datetime.date(1900, 1, 1)
        
        # ポッドキャスト音声
        try:        
            audio = post.find("a", class_="powerpress_link_d").get("href")
        except:
            audio = ""

        # ポッドキャスト画像
        try:
            image = post.find("img").get("src")
        except:
            image = ""

        # 放送回の情報を辞書に格納
        are = {
            "num": num,
            "title": title,
            "url": url,
            "published_datetime": published,
            "recorded_date": recorded,
            "audio_url": audio,
            "image_url": image
        }
        # print(are)
        are_list.append(are)
    return are_list

# シンプルな CSV 出力
def output_csv(are_list, filename):
    with open(filename, "w", encoding="utf-8") as f:
        # ヘッダー
        f.write("num,title,published_datetime,recorded_date,url,audio_url,image_url\n")
        for are in are_list:
            f.write(
                str(are["num"]) + "," +
                are["title"] + "," +
                are["published_datetime"].isoformat(timespec="minutes") + "," +
                are["recorded_date"].isoformat() + "," +
                are["url"] + "," +
                are["audio_url"] + "," +
                are["image_url"] + "\n"
            )

# エクセル向け CSV 出力
def output_csv_excel(are_list, filename):
    with open(filename, "w", encoding="utf-8-sig") as f:
        # ヘッダー
        f.write("num,title,published_datetime,recorded_date,url,audio_url,image_url\n")
        for are in are_list:
            f.write(
                str(are["num"]) + "," +
                '"' + are["title"].replace('"', '""') + '",' +
                '"' + are["published_datetime"].strftime("%Y-%m-%d %H:%M") + '",' +
                '"' + are["recorded_date"].isoformat() + '",' +
                '"' + are["url"] + '",' +
                '"' + are["audio_url"] + '",' +
                '"' + are["image_url"] + '"\n'
            )

# JSON 出力
def output_json(are_list, filename):
    for are in are_list:
        # datetimeをISOフォーマットの文字列に変換
        are["published_datetime"] = are["published_datetime"].isoformat(timespec="minutes")
        are["recorded_date"] = are["recorded_date"].isoformat()
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(are_list, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    are_list = are_search()
    today = datetime.date.today().isoformat()
    output_csv(are_list, "scraping_" + today + "_simple.csv")
    output_csv_excel(are_list, "scraping_" + today + "_excel.csv")
    output_json(are_list, "scraping_" + today + ".json")
