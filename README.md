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

## Python, uv インストール
Python のインストールについては省略します。

uv 参考: https://docs.astral.sh/uv/getting-started/installation/

```
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 依存ライブラリのインストール

### Windows (uv インストール済みの場合)
```powershell
# venv 構築・ライブラリのインストール
uv sync
# 仮想環境のアクティベート
.\.venv\Scripts\Activate.ps1
# Sphinx ビルド（docsディレクトリに生成）
.\make.bat html
```

### Windows (Python のみの場合)
```powershell
# 仮想環境の構築
python -m venv .venv
# 仮想環境のアクティベート
.\.venv\Scripts\Activate.ps1
# ライブラリのインストール
pip install -r requirements.txt
# Sphinx ビルド（docsディレクトリに生成）
.\make.bat html
```

### Linux (uv インストール済みの場合)
```bash
# venv 構築・ライブラリのインストール
uv sync
# 仮想環境のアクティベート
source .venv/bin/activate
# Sphinx ビルド（docsディレクトリに生成）
make html
```

### Linux (Python のみの場合)
```bash
#!/usr/bin/env bash

# 仮想環境の構築
python -m venv .venv
# 仮想環境のアクティベート
source .venv/bin/activate
# ライブラリのインストール
pip install -r requirements.txt
# Sphinx ビルド（docsディレクトリに生成）
make html
```

## ドキュメント生成（ビルド）
ビルドを行うと、docs ディレクトリに HTML ドキュメントが生成されます。

### 単純生成
次のコマンドを実行します。
```
# Windows
.\venv\Scripts\Activate.ps1
.\make.bat html

# Linux
source venv/bin/activate
make html
```

### 自動リロード
プレビュー見ながら編集したいときは次のコマンドを実行します。自動的にブラウザが立ち上がり、ドキュメントを閲覧できます。

http://localhost:8000 にアクセスするとドキュメントを閲覧できます。

```
# Windows
.\venv\Scripts\Activate.ps1
.\make.bat preview
```

### 放送回一覧リストの更新
放送回一覧ページ（podcast_list.rst）は [generate_podcast_list.py](generate_podcast_list.py) によって生成しています。  
新しい放送回があれば [generate_podcast_list.py](generate_podcast_list.py) を実行することで、自動的に一覧が更新されます。  
CSVファイル [セキュリティのアレ_放送回リスト.csv](./source/_static/セキュリティのアレ_放送回リスト.csv) をもとに、テンプレートファイル [podcast_list.rst.template](./source/podcasts/podcast_list.rst.template) に表を挿入しています。

### ライブラリアップデート
```
pip-review --auto
pip freeze > requirements.txt
```
