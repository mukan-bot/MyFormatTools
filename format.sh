#!/bin/bash

TARGET_DIR=${1:-.}

#Pythonの環境にisort, blackがインストールされていない場合はインストール
if ! type "isort" > /dev/null; then
    echo "isort is not installed. Installing isort..."
    pip install isort
fi

if ! type "black" > /dev/null; then
    echo "black is not installed. Installing black..."
    pip install black
fi

# isortでインポート順を整える
echo "Running isort on $TARGET_DIR"
isort $TARGET_DIR

# Blackでコードをフォーマット
echo "Running Black on $TARGET_DIR"
black $TARGET_DIR

# `assign` のカスタムフォーマットを適用
echo "Applying custom formatting for pandas assign"
python add_format.py $TARGET_DIR

echo "Formatting completed."
