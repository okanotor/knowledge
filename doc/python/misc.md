# 色々メモ (Python)

## vscode のターミナルで venv を使えるようにする

- デフォルトの設定だと、アクティベート用スクリプトの実行がポリシーに制限されているため、venv が使えない。
- アクティベート用スクリプトの実行前に `Set-ExecutionPolicy` コマンドでポリシーを変更すれば実行できるようになる。
- 但し、毎回上記コマンドを実行するのは面倒なので、vscode の設定で、vscode 起動時にポリシーを変更するように対応。

```json
{
    "terminal.integrated.env.windows": {
        "PSExecutionPolicyPreference": "RemoteSigned"
    }
}
```

### 参考URL

- [【Windows版Visual Studio Code】Pythonのvenvを楽に使う方法](https://zenn.dev/nekocodex/articles/eb3403961ad9b966ff6e)

---

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
# for windows : .\venv\Scripts\Activate.ps1

# pip 最新化
python -m pip install --upgrade pip

# パッケージインストール
pip install -r requirements.txt
```
