#!/usr/bin/env bash

# 仮想環境の構築
uv venv
# ライブラリのインストール
uv sync
# 仮想環境のアクティベート
source venv/bin/activate
# Sphinx ビルド（docsディレクトリに生成）
make html
