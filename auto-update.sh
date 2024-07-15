#!/usr/bin/env bash

echo "Security-no-ARE 新規ポッドキャストがあれば自動更新するスクリプト"

# 仮想環境のアクティベート
source venv/bin/activate

# ポッドキャスト更新の検出
python generate_podcast_list.py

if [ $? -eq 0 ]
then
    echo "新規ポッドキャストはありません"
    exit 0
else
    echo "新規ポッドキャストが見つかりました"
    make html

    # GitHub Push => GitHub Action で自動デプロイ
    git add ./source
    git add ./docs
    git commit -m "auto commit"
    git push origin main
fi
