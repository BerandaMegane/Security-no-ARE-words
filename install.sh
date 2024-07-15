#!/usr/bin/env bash

# 仮想環境の構築
python -m venv venv
# 仮想環境のアクティベート
source venv/bin/activate
# ライブラリのインストール
pip install -r requirements.txt
# Sphinx ビルド（docsディレクトリに生成）
./make.bat html
