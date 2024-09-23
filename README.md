# セキュリティのアレまとめ

## これは何？
[セキュリティのアレ](https://www.tsujileaks.com/) という情報セキュリティ系ポッドキャストがあります。  
ポッドキャストは2011年から続いており、長い歴史の中、「あれ？この話題って第何回で話したっけ？」といった形で振り返りたくなることがあります。また、過去の回を聴くことで、当時の反応にも触れることができます。  
そこで、ポッドキャスト内で語られる話題・用語を個人的にまとめてみました。

次の URL にて公開しています。  
[https://are.bocchi-megane.dev - セキュリティのアレまとめ](https://are.bocchi-megane.dev)

このサイトを作成するにあたって、mtaka 氏による [ゆる言語学ラジオ用語集](https://yurugengo.mtakagishi.com) を参考にしました。  
ゆる言語学ラジオ用語集は、[MIT ライセンスにて公開](https://github.com/mtakagishi/yurugengo) されています。  

## 構成
Sphinx を使って HTML ドキュメントを生成し、GitHub Pages で公開しています。

- Sphinx は Python 製のドキュメント生成ツールです
- 記事は reST 記法（reStrictiredText 記法）で記述します

## インストール
Python については省略します。

```
# Windows
.\install.ps1

# Linux
./install.sh
```

## ドキュメント生成（ビルド）
ビルドを行うと、docs ディレクトリに HTML ドキュメントが生成されます。

### 単純生成
次のコマンドを実行します。
```
# Windows
.\make.bat html

# Linux
make html
```

### 自動リロード
プレビュー見ながら編集したいときは次のコマンドを実行します。自動的にブラウザが立ち上がり、ドキュメントを閲覧できます。

http://localhost:8000 にアクセスするとドキュメントを閲覧できます。

```
# Windows
.\make.bat preview
```

### 放送回一覧リストの更新
放送回一覧ページ（podcast_list.rst）は [generate_podcast_list.py](generate_podcast_list.py) によって生成しています。  
新しい放送回があれば [generate_podcast_list.py](generate_podcast_list.py) を実行することで、自動的に一覧が更新されます。  
CSVファイル [セキュリティのアレ_放送回リスト.csv](./_static/セキュリティのアレ_放送回リスト.csv) をもとに、テンプレートファイル [podcast_list.rst.template](./podcasts/podcast_list.rst.template) に表を挿入しています。

### ライブラリアップデート
```
pip-review --auto
pip freeze > requirements.txt
```
