# 公式
import csv

"""
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
    write_url_long_ref(reader, writer)
    writer.write("\n")
    write_url_short_ref(reader, writer)
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

def main():
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

if __name__ == "__main__":
    main()
