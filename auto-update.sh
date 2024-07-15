#!/usr/bin/env bash

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

    git add ./source
    git add ./docs
fi
