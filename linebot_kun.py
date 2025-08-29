"""
LINE Bot メッセージ送信クラス
"""

import logging
import time
from typing import Optional, List, Union
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import hidden_key
import linebot_kun_config as config


class LineBotSender:
    """LINE Bot メッセージ送信クラス"""

    def __init__(self, token: Optional[str] = None):
        """
        LineBotSenderクラスの初期化

        Args:
            token: LINE Bot Channel Access Token
        """
        self.token = token or hidden_key.TOKEN
        self._api = None
        self._setup_logging()

    def _setup_logging(self) -> None:
        """ログ設定の初期化"""
        logging.basicConfig(
            level=getattr(logging, config.LOG_CONFIG["level"]),
            format=config.LOG_CONFIG["format"],
            filename=config.LOG_CONFIG["filename"],
        )
        self.logger = logging.getLogger(__name__)

    @property
    def api(self) -> LineBotApi:
        """LINE Bot APIインスタンスを取得（遅延初期化）"""
        if self._api is None:
            if not self.token:
                raise ValueError("TOKEN が設定されていません")
            self._api = LineBotApi(self.token)
        return self._api

    def validate_message(self, message: str) -> bool:
        """
        メッセージの妥当性をチェック

        Args:
            message: 送信するメッセージ

        Returns:
            bool: メッセージが妥当かどうか
        """
        if not message or not message.strip():
            self.logger.warning("空のメッセージが指定されました")
            return False

        if len(message) > config.MESSAGE_CONFIG["max_message_length"]:
            self.logger.warning(f"メッセージが長すぎます: {len(message)} 文字")
            return False

        return True

    def send_message(self, message: str, dry_run: bool = True, retry_count: Optional[int] = None) -> bool:
        """
        メッセージを送信

        Args:
            message: 送信するメッセージ
            dry_run: True の場合は実際に送信しない（デバッグモード）
            retry_count: リトライ回数（Noneの場合は設定値を使用）

        Returns:
            bool: 送信成功かどうか
        """
        if not self.validate_message(message):
            return False

        if dry_run:
            self.logger.info(f"DRY RUN - 送信予定メッセージ: {message}")
            print(f"DRY RUN - NotSend: {message}")
            return True

        retry_count = retry_count or config.MESSAGE_CONFIG["retry_count"]

        for attempt in range(retry_count + 1):
            try:
                text_message = TextSendMessage(text=message)
                self.api.broadcast(messages=text_message)

                self.logger.info(f"メッセージ送信成功: {message}")
                print(f"MsgSend: {message}\nCHANNEL: {self.token}")
                return True

            except LineBotApiError as e:
                self.logger.error(f"LINE Bot API エラー (試行 {attempt + 1}): {e}")
                if attempt < retry_count:
                    time.sleep(config.MESSAGE_CONFIG["retry_delay"])
                    continue
                else:
                    print(f"送信に失敗しました: {e}")
                    return False

            except Exception as e:
                self.logger.error(f"予期しないエラー: {e}")
                print(f"送信エラー: {e}")
                return False

        return False

    def send_multiple_messages(self, messages: List[str], dry_run: bool = True) -> List[bool]:
        """
        複数のメッセージを送信

        Args:
            messages: 送信するメッセージのリスト
            dry_run: True の場合は実際に送信しない

        Returns:
            List[bool]: 各メッセージの送信結果
        """
        results = []
        for i, message in enumerate(messages):
            self.logger.info(f"メッセージ {i + 1}/{len(messages)} を送信中")
            result = self.send_message(message, dry_run)
            results.append(result)

            # 連続送信時の間隔調整
            if not dry_run and i < len(messages) - 1:
                time.sleep(1)

        return results


# 下位互換性のための関数
def send_message(send_message: str = "", send: bool = False, token: str = "") -> bool:
    """
    下位互換性のための関数（非推奨）

    Args:
        send_message: 送信するメッセージ
        send: True の場合は実際に送信
        token: LINE Bot Channel Access Token

    Returns:
        bool: 送信成功かどうか
    """
    if token == "":
        print("tokenを指定して?")
        return False

    if send_message == "":
        print("send_messageが空っぽだよ?")
        return False

    bot = LineBotSender(token)
    return bot.send_message(send_message, dry_run=not send)


if __name__ == "__main__":
    # テスト実行
    bot = LineBotSender()
    bot.send_message("python配信テスト", dry_run=True)
