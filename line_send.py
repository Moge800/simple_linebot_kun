"""
LINE Bot メッセージ送信ラッパー
"""

from typing import Optional, List
import linebot_kun
import hidden_key


class LineBotWrapper:
    """LINE Bot 送信のラッパークラス"""

    def __init__(self, token: Optional[str] = None):
        """
        LineBotWrapperの初期化

        Args:
            token: LINE Bot Channel Access Token
        """
        self.bot = linebot_kun.LineBotSender(token or hidden_key.TOKEN)

    def send_message(self, message: str, debug: bool = True, retry_count: Optional[int] = None) -> bool:
        """
        メッセージを送信

        Args:
            message: 送信するメッセージ
            debug: True の場合はデバッグモード（実際に送信しない）
            retry_count: リトライ回数

        Returns:
            bool: 送信成功かどうか
        """
        try:
            return self.bot.send_message(message=message, dry_run=debug, retry_count=retry_count)
        except Exception as e:
            print(f"送信エラー: {e}")
            return False

    def send_multiple(self, messages: List[str], debug: bool = True) -> List[bool]:
        """
        複数のメッセージを送信

        Args:
            messages: 送信するメッセージのリスト
            debug: True の場合はデバッグモード

        Returns:
            List[bool]: 各メッセージの送信結果
        """
        return self.bot.send_multiple_messages(messages, dry_run=debug)


# 下位互換性のための関数
def send_main(send_msg: str, debug: bool = True, token: str = hidden_key.TOKEN) -> bool:
    """
    下位互換性のための関数（非推奨）

    Args:
        send_msg: 送信するメッセージ
        debug: True の場合はデバッグモード
        token: LINE Bot Channel Access Token

    Returns:
        bool: 送信成功かどうか
    """
    wrapper = LineBotWrapper(token)
    return wrapper.send_message(send_msg, debug)


if __name__ == "__main__":
    # テスト実行
    wrapper = LineBotWrapper()
    wrapper.send_message("YEAH!", debug=True)
