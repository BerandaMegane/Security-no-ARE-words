# 公式
import csv
import datetime
import email
import re
import sys

# サードパーティ
import feedparser

"""
tsujileaks.com の RSS を読み込み、更新がアレば放送回リストを更新する。

放送回リスト（CSV形式）を読み込み、
reStructuredText形式のテーブル（list-table形式）の文字列を生成し、
放送回一覧ページ（reST形式）に書き込む。
"""

in_csv_path = "./source/_static/セキュリティのアレ_放送回リスト.csv"
temp_rest_path = "./source/podcasts/podcast_list.rst.template"
out_rest_path = "./source/podcasts/podcast_list.rst"


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
        writer.write("   * - %s\n"    % (row["ID"]))
        writer.write("     - `%s <%s>`_ \n" % (row["タイトル"], row["URL"]))
        writer.write("     - %s\n"    % (row["公開日"]))

def write_url_long_ref(reader, writer):
    """次のような長い形式でURL参照を貼り付ける
    .. _第193回 そろそろ秋を意識していきたい！スペシャル！: https://www.tsujileaks.com/?p=1595
    """
    reader.seek(0)
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        writer.write(".. _%s: %s\n" % (row["タイトル"], row["URL"]))

def write_url_short_ref(reader, writer):
    """次のような短い形式でURL参照を貼り付ける
    .. _S3#193: https://www.tsujileaks.com/?p=1595
    """
    reader.seek(0)
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        writer.write(".. _%s: %s\n" % (row["ID"], row["URL"]))

def write_url_ref(reader, writer):
    """次のような形式でURL参照を貼り付ける
    .. _第193回 そろそろ秋を意識していきたい！スペシャル！: https://www.tsujileaks.com/?p=1595
    .. _S3#193: https://www.tsujileaks.com/?p=1595
    """
    reader.seek(0)
    csv_reader = csv.DictReader(reader)
    for row in csv_reader:
        writer.write(".. _%s: %s\n" % (row["タイトル"], row["URL"]))
        writer.write(".. _%s: %s\n" % (row["ID"], row["URL"]))

def parse_RFC2822_datetime(date_str_rfc2822: str):
    """RFC2822形式をパースする"""
    timetuple = email.utils.parsedate_tz(date_str_rfc2822)
    JST = datetime.timezone(datetime.timedelta(hours=9), "JST")
    date = datetime.datetime(*timetuple[:7], tzinfo=JST)
    return date

def searchNewPodcasts():
    rss = feedparser.parse("https://www.tsujileaks.com/?feed=rss2")

    new_podcasts = list()
    
    cnt = 0
    for entry in rss.entries:
        # 直近の数回を調べる
        cnt += 1
        if cnt > 5:
            break
        
        # pprint.pprint(entry)

        title = entry.title
        match = re.search(r'\d+', title)
        podcast_id = "S3#" + match.group()
        url = entry.link
        published_dt = parse_RFC2822_datetime(entry.published)

        # print(podcast_id, title, published_dt, url)
        new_podcasts.append({
            "ID": podcast_id,
            "タイトル": title,
            "公開日": published_dt.strftime(r"%Y月%m月%d日"),
            "URL": url,
        })

        # pprint.pprint(new_podcasts)
    
    return new_podcasts

def updatePodcastCSV(csv_path, new_podcasts):
    with open(csv_path, "r", encoding="utf-8") as csv:
        # 最初の行はヘッダ
        header = csv.readline()

        # 残りはデータ
        data_lines = csv.readlines()
        first_data = data_lines[0]

        # 更新場所の特定
        update_index = 0
        for i in range(len(new_podcasts)-1, 0, -1):
            # print(first_data, new_podcasts[i]["ID"])
            if new_podcasts[i]["ID"] in first_data:
                update_index = i

        # 足りない回を追加する
        append_cnt = 0
        for new_podcast in reversed(new_podcasts[:update_index]):
            append_cnt += 1
            print("new podcast append", new_podcast)
            data = "%s,%s,%s,%s\n" % (new_podcast["ID"], new_podcast["タイトル"], new_podcast["公開日"], new_podcast["URL"])
            data_lines.insert(0, data)

    with open(csv_path, "w", encoding="utf-8") as csv:
        csv.write(header)
        csv.writelines(data_lines)
    
    return append_cnt

def main():
    # 更新があれば CSV へ追加する
    new_podcasts = searchNewPodcasts()
    append_cnt = updatePodcastCSV(in_csv_path, new_podcasts)

    # CSVファイル
    reader = open(in_csv_path, "r", encoding="utf-8")

    # テンプレート用reSTファイル
    temp_reader = open(temp_rest_path, "r", encoding="utf-8")

    # 出力用reSTファイル
    writer = open(out_rest_path, "w", encoding="utf-8")

    write_file(reader, temp_reader, writer)

    reader.close()
    temp_reader.close()
    writer.close()
    
    sys.exit(append_cnt)
        
if __name__ == "__main__":
    main()
