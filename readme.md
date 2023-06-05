# monitor_pc_resource.py 使い方

## 前提

windows環境で動作させることを想定しています

## 環境設定

```bat
:: 仮想環境作成
python -m venv --upgrade-deps .env
:: 仮想環境アクティベート
.env\Scripts\activate
:: 必要パッケージインストール
pip install -r requirements.txt
```

## 実行方法

```bat
python monitor_pc_resource.py
```