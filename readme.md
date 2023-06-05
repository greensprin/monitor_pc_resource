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

# batfile/run_typeperf.bat 説明

typeperfを使えばいろいろデータを取得できるので、そちらのほうが簡単でよさそう

## カウンターの取得

typeperfはカウンターという要素を指定して各種データを取得する
ただし、最初はそのカウンターにどういう物があるかがわからない

そんなときのために、以下のコマンドでどういうカウンターがあるかを取得できる

```bat
typeperf -q
```

また、ある程度カウンターの名前がわかっている場合は、以下のようにすることで結果を絞ることもできる

```bat
:: processor に絞ってカウンターを取得
typeperf -q "processor"
```

## データ取得

以下ではCPU使用率[%]、メモリ空き容量[MByte]、ディスク使用率[%]を取得する
1秒に1回取得し、Ctrl+Cが押されるまで続く

```bat
typeperf "\Processor Information(_Total)\% Processor Time" "\Memory\Available MBytes" "\PhysicalDisk(_Total)\% Disk Time"
```

### ファイルでカウンターを管理する
表示させたいカウンターをファイルで管理することもできる
typeperf_target.txtに表示させたいカウンターを1行に1つ書いて読み込ませる

```bat
typeperf -cf typeperf_target.txt
```

typeperf_target.txtは以下のように記載する

```txt
\Processor Information(_Total)\% Processor Time
\Memory\Available MBytes
\PhysicalDisk(_Total)\% Disk Time
```

### その他参考情報
取得する秒数を変更したり、取得する回数を変更したりすることもできる。
以下の公式サイトを確認すれば、どのようなオプションがあるかがわかるので、詳しく知りたい場合は以下を参照。
https://learn.microsoft.com/ja-jp/windows-server/administration/windows-commands/typeperf