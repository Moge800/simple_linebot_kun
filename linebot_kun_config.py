"""
LINE Bot 設定ファイル
GitHubにコミット可能な一般的な設定項目
"""

from typing import Dict, Any

# ログ設定
LOG_CONFIG: Dict[str, Any] = {
    "level": "INFO",
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "filename": "linebot.log",
}

# メッセージ送信設定
MESSAGE_CONFIG: Dict[str, Any] = {"max_message_length": 5000, "retry_count": 3, "retry_delay": 1.0}

# API設定
API_CONFIG: Dict[str, Any] = {"timeout": 30, "max_retries": 3, "backoff_factor": 0.3}

# デバッグ設定
DEBUG_CONFIG: Dict[str, Any] = {"default_dry_run": True, "verbose_logging": False, "save_sent_messages": True}
