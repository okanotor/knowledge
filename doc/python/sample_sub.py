# import
# ロガー作成のため、logging モジュールは必ず読み込む。
from logging import getLogger, NullHandler

# ロガーの作成
# 呼出元からロガーを受け取らなかった場合に備えて、モジュール内に NullHandler を使用するロガーを作成しておく。
__default_logger = getLogger(__name__)
__default_logger.addHandler(NullHandler())

# モジュール内で定義する関数
# 上位からロガーを受け付けるようにする。
# ロガーを渡せないケースも考え、キーワード引数で受け付けるようにする。
def func0(*, logger=None):
    logger = logger or __default_logger
