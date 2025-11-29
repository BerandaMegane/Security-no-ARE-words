# 仮想環境の構築
uv init
uv venv
# ライブラリのインストール
uv add -r requirements.txt
# 仮想環境のアクティベート
.\venv\Scripts\Activate.ps1
# Sphinx ビルド（docsディレクトリに生成）
.\make.bat html
