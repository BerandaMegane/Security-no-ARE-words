# 公式
import csv
import datetime
import email
import re
import sys

# サードパーティ
import feedparser
import pprint
from bs4 import BeautifulSoup
import requests

"""
tsujileaks.com の RSS を読み込み、
更新があれば放送回リスト（CSV形式, input_csv_path）を更新する。

放送回リストを元に
reStructuredText形式のテーブル（list-table形式）の文字列を生成し、
テンプレートファイル（reST形式, template_rest_path）へ埋め込み、
放送回一覧ページ（reST形式, output_rest_path）に書き込む。
"""

input_csv_path = "./source/_static/セキュリティのアレ_放送回リスト_自動更新.csv"
template_rest_path = "./source/podcasts/podcast_list.rst.template"
output_rest_path = "./source/podcasts/podcast_list.rst"


def write_file(reader, temp_reader, writer):
    """テンプレートファイルに放送回一覧を書き込む"""

    # テーブル挿入位置 list-table ディレクティブを探す
    while "list-table" not in (temp_line:=temp_reader.readline()) :
        writer.write(temp_line)
    
    writer.write(temp_line)  # list-table ディレクティブ
    
    # テーブル挿入位置を見つけた場合は、空白行まで飛ばす
    while (temp_line:=temp_reader.readline()).strip() != "":
        writer.write(temp_line)

    # 前後に空白行と list-table 形式の表を挿入する          
    writer.write("\n")
    writer.write("   * - ID\n")
    writer.write("     - タイトル\n")
    writer.write("     - 公開日\n")
    write_table(reader, writer)
    writer.write("\n")

    # URLの参照を書き込む
    write_url_ref(reader, writer)
    writer.write("\n")

    # 通常部分はそのまま書き込む
    for temp_line in temp_reader:
        writer.write(temp_line)
    
def write_table(reader, writer):
    reader.seek(0)
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        writer.write("   * - %s\n"    % (row["id"]))
        writer.write("     - `%s <%s>`_ \n" % (row["title"], row["url"]))
        writer.write("     - %s\n"    % (row["published_datetime"]))

def write_url_long_ref(reader, writer):
    """次のような長い形式でURL参照を貼り付ける
    .. _第193回 そろそろ秋を意識していきたい！スペシャル！: https://www.tsujileaks.com/?p=1595
    """
    reader.seek(0)
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        writer.write(".. _%s: %s\n" % (row["title"], row["url"]))

def write_url_short_ref(reader, writer):
    """次のような短い形式でURL参照を貼り付ける
    .. _S3#193: https://www.tsujileaks.com/?p=1595
    """
    reader.seek(0)
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        writer.write(".. _%s: %s\n" % (row["id"], row["url"]))

def write_url_ref(reader, writer):
    """次のような形式でURL参照を貼り付ける
    .. _第193回 そろそろ秋を意識していきたい！スペシャル！: https://www.tsujileaks.com/?p=1595
    .. _S3#193: https://www.tsujileaks.com/?p=1595
    """
    reader.seek(0)
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        writer.write(".. _%s: %s\n" % (row["title"], row["url"]))
        writer.write(".. _%s: %s\n" % (row["id"], row["url"]))

def parse_RFC2822_datetime(date_str_rfc2822: str):
    """RFC2822形式をパースする"""
    timetuple = email.utils.parsedate_tz(date_str_rfc2822)
    timedelta = datetime.timedelta(hours=9)
    JST = datetime.timezone(timedelta, "JST")
    date = datetime.datetime(*timetuple[:7], tzinfo=JST) + timedelta
    return date

def search_new_podcasts():
    # tsujileaks.com の RSS フィードを読み込み、最新のポッドキャスト情報を取得する
    rss = feedparser.parse("https://www.tsujileaks.com/?feed=rss2")
    new_podcasts = list()
    
    cnt = 0
    for entry in rss.entries:
        # 直近の数回を調べる
        cnt += 1
        # if cnt >= 2:
        #     break
        
        # tsujileaks.com の URL 取得
        url = entry.link
        # ポッドキャストの情報を取得
        podcast_info = fetch_podcast_info(url)
        # 格納
        new_podcasts.append(podcast_info)

    # print("新規ポッドキャスト一覧")
    # pprint.pprint(new_podcasts)
    return new_podcasts


def fetch_podcast_info(are_url):
    """
    指定されたURLからポッドキャストの情報を取得する
    """

    response = requests.get(are_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('div', class_="post")
    post = posts[0]  # 最初のポストを取得

    # 日付のタイムゾーン
    JST = datetime.timezone(datetime.timedelta(hours=9), "JST")

    # タイトル title
    storytitle = post.find("h2", class_="storytitle")
    title = storytitle.getText()
    
    # 放送回 num
    num = int(title.split("回")[0][1:])

    # 公開日 published_datetime
    published = post.find("b", class_="published")["title"]
    try:
        published = datetime.datetime.fromisoformat(published)
    except:
        published = datetime.datetime(1900, 1, 1, tzinfo=JST)
    
    # 収録日 recorded_date
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
    
    # ポッドキャスト音声 audio_url
    try:        
        audio = post.find("a", class_="powerpress_link_d").get("href")
    except:
        audio = ""

    # ポッドキャスト画像 image_url
    try:
        image = post.find("img").get("src")
    except:
        image = ""

    return {
        "season": 3,
        "id": "S3#%d" % num,
        "num": num,
        "title": title,
        "url": are_url,
        "published_datetime": published,
        "recorded_date": recorded,
        "audio_url": audio,
        "image_url": image
    }    

def update_podcast_csv(csv_path, new_podcasts):
    with open(csv_path, "r", encoding="utf-8") as csv:
        # 最初の行はヘッダ
        header = csv.readline()

        # 残りはデータ
        data_lines = csv.readlines()
        # CSVに記録された最新回
        first_data = data_lines[0]

        # 更新場所の特定
        update_index = 0
        for i in range(len(new_podcasts)-1, 0, -1):
            # print(first_data, new_podcasts[i]["ID"])
            if new_podcasts[i]["id"] in first_data:
                update_index = i

        # 足りない回を追加する
        append_cnt = 0
        for new_podcast in reversed(new_podcasts[:update_index]):
            append_cnt += 1
            print("new podcast append", new_podcast, file=sys.stderr)
            data = "%d,%d,%s,%s,%s,%s,%s,%s,%s\n" % (
                new_podcast["season"],
                new_podcast["num"],
                new_podcast["id"],
                new_podcast["title"],
                new_podcast["published_datetime"].isoformat(timespec="minutes"),
                new_podcast["recorded_date"].isoformat(),
                new_podcast["url"],
                new_podcast["audio_url"],
                new_podcast["image_url"],
            )
            data_lines.insert(0, data)

    with open(csv_path, "w", encoding="utf-8") as csv:
        csv.write(header)
        csv.writelines(data_lines)
    
    return append_cnt

def main():
    # 更新があれば CSV へ追加する
    new_podcasts = search_new_podcasts()
    append_cnt = update_podcast_csv(input_csv_path, new_podcasts)

    # CSVファイル
    with open(input_csv_path, "r", encoding="utf-8") as input_csv:
        # テンプレート用reSTファイル
        with open(template_rest_path, "r", encoding="utf-8") as template_rest:
            # 出力用reSTファイル
            with open(output_rest_path, "w", encoding="utf-8") as output_rest:
                # テンプレートファイルに放送回一覧を書き込む
                write_file(input_csv, template_rest, output_rest)    
    print(append_cnt)
    
if __name__ == "__main__":
    main()
