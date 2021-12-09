# import
# デバッグ情報出力のため、logging モジュールは必ず読み込む。
# ロガー情報の読み込みのため、json モジュールも必ず読み込む。
from logging import getLogger
import logging.config
import json

# ロガーの設定
# 設定情報は logging_config.json に納めておき、使い回しできるようにしておく。
# 簡単なスクリプトであれば、使う設定は root で。
# exe 化して定期実行するなら、ファイル出力する設定に変える。
with open('./logging_config.json') as ins:
    logging.config.dictConfig(json.load(ins))

logger = getLogger(__name__)

# main 関数
# 本処理はこの中に書いていく
def main():
    pass

# main呼び出し
if __name__ == '__main__':
    main
