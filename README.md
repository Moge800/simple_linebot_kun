# Simple LINE Bot Kun / シンプルLINE Botくん

[English](#english) | [日本語](#japanese)

---

## English

### Overview
Simple LINE Bot Kun is a lightweight Python library for sending messages through the LINE Bot API. It provides an easy-to-use wrapper around the LINE Bot SDK with built-in retry logic, logging, and debug modes.

### Features
- Simple message sending to LINE Bot
- Debug mode for testing without actual message delivery
- Automatic retry with configurable settings
- Comprehensive logging
- Multiple message sending support
- Message validation

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Moge800/simple_linebot_kun.git
cd simple_linebot_kun
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Setup

1. Copy the token template file:
```bash
cp hidden_key_template.py hidden_key.py
```

2. Edit `hidden_key.py` and set your LINE Bot Channel Access Token:
```python
TOKEN = "YOUR_LINE_BOT_CHANNEL_ACCESS_TOKEN_HERE"
```

You can obtain the Channel Access Token from the [LINE Developers Console](https://developers.line.biz/).

### Usage

#### Basic Usage with LineBotWrapper (Recommended)

```python
from line_send import LineBotWrapper

# Initialize the wrapper
bot = LineBotWrapper()

# Send a message in debug mode (won't actually send)
bot.send_message("Hello, World!", debug=True)

# Send a message for real
bot.send_message("Hello, World!", debug=False)

# Send multiple messages
messages = ["Message 1", "Message 2", "Message 3"]
results = bot.send_multiple(messages, debug=False)
```

#### Advanced Usage with LineBotSender

```python
from linebot_kun import LineBotSender

# Initialize with custom token
bot = LineBotSender("your_custom_token")

# Send message with custom retry count
success = bot.send_message("Hello!", dry_run=False, retry_count=5)

# Send multiple messages
messages = ["Message 1", "Message 2"]
results = bot.send_multiple_messages(messages, dry_run=False)
```

#### Legacy Function (Deprecated)

```python
from line_send import send_main

# Legacy function for backward compatibility
success = send_main("Hello!", debug=False)
```

### Configuration

You can customize the behavior by modifying `linebot_kun_config.py`:

- `LOG_CONFIG`: Logging settings
- `MESSAGE_CONFIG`: Message length limits and retry settings
- `API_CONFIG`: API timeout and retry settings
- `DEBUG_CONFIG`: Debug mode defaults

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Japanese

### 概要
Simple LINE Bot Kun は、LINE Bot API を通じてメッセージを送信するための軽量な Python ライブラリです。LINE Bot SDK の使いやすいラッパーを提供し、リトライ機能、ログ機能、デバッグモードが組み込まれています。

### 機能
- LINE Bot への簡単なメッセージ送信
- 実際の送信を行わないデバッグモード
- 設定可能な自動リトライ機能
- 包括的なログ機能
- 複数メッセージ送信対応
- メッセージ検証機能

### インストール

1. このリポジトリをクローン:
```bash
git clone https://github.com/Moge800/simple_linebot_kun.git
cd simple_linebot_kun
```

2. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

### セットアップ

1. トークンテンプレートファイルをコピー:
```bash
cp hidden_key_template.py hidden_key.py
```

2. `hidden_key.py` を編集して、LINE Bot Channel Access Token を設定:
```python
TOKEN = "YOUR_LINE_BOT_CHANNEL_ACCESS_TOKEN_HERE"
```

Channel Access Token は [LINE Developers Console](https://developers.line.biz/) から取得できます。

### 使用方法

#### LineBotWrapper を使用した基本的な使い方（推奨）

```python
from line_send import LineBotWrapper

# ラッパーを初期化
bot = LineBotWrapper()

# デバッグモードでメッセージ送信（実際には送信されません）
bot.send_message("こんにちは、世界！", debug=True)

# 実際にメッセージ送信
bot.send_message("こんにちは、世界！", debug=False)

# 複数メッセージの送信
messages = ["メッセージ1", "メッセージ2", "メッセージ3"]
results = bot.send_multiple(messages, debug=False)
```

#### LineBotSender を使用した高度な使い方

```python
from linebot_kun import LineBotSender

# カスタムトークンで初期化
bot = LineBotSender("your_custom_token")

# カスタムリトライ回数でメッセージ送信
success = bot.send_message("こんにちは！", dry_run=False, retry_count=5)

# 複数メッセージの送信
messages = ["メッセージ1", "メッセージ2"]
results = bot.send_multiple_messages(messages, dry_run=False)
```

#### 旧式関数（非推奨）

```python
from line_send import send_main

# 後方互換性のための旧式関数
success = send_main("こんにちは！", debug=False)
```

### 設定

`linebot_kun_config.py` を編集することで動作をカスタマイズできます：

- `LOG_CONFIG`: ログ設定
- `MESSAGE_CONFIG`: メッセージ長制限とリトライ設定
- `API_CONFIG`: API タイムアウトとリトライ設定
- `DEBUG_CONFIG`: デバッグモードのデフォルト設定

### ライセンス

このプロジェクトは MIT ライセンスの下でライセンスされています。詳細は [LICENSE](LICENSE) ファイルを参照してください。