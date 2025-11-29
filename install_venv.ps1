# 仮想環境の構築
python -m venv venv
# 仮想環境のアクティベート
.\venv\Scripts\Activate.ps1
# ライブラリのインストール
pip install -r requirements.txt
# Sphinx ビルド（docsディレクトリに生成）
.\make.bat html
