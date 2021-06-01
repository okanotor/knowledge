# 色々メモ (Python)

## 作業開始時の環境構築

```
# 作業ディレクトリを作成
mkdir /path/to/dir

# 作業ディレクトリに移動
cd /path/to/dir

# 必要パッケージをリスト化
touch requirements.txt
# requirements.txt に必要パッケージを記入

# 仮想環境構築
python -m venv venv
# or py -m venv venv

# 仮想環境有効化
. venv/bin/activate
# for windows : .\venv\Scripts\activate

# pip 最新化
python -m pip install --upgrade pip

# パッケージインストール
pip install -r requirements.txt
```
