# Talkomatic Discord Bot

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Discord Developer Portal](#discord-developer-portal)
  - [Bot Installation](#bot-installation)
  - [Inviting the Bot to Your Server](#inviting-the-bot-to-your-server)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Talkomatic Discord Bot is a Python-based bot that integrates with the Talkomatic platform to provide real-time information about chat rooms and user activity directly in your Discord server. This bot allows users to easily monitor and access Talkomatic statistics without leaving Discord.

## Features

- 🔄 Real-time status updates showing the number of active rooms and users
- 📊 `/stats` command to display overall Talkomatic statistics
- 🏠 `/rooms` command to list detailed information about each active room
- 🚀 Automatic updates every 10 seconds

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed on your system
- pip (Python package manager)
- A Discord account
- Basic knowledge of using command-line interfaces
- A Talkomatic account (for API access)

## Setup

### Discord Developer Portal

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your application a name (e.g., "Talkomatic Bot").
3. Navigate to the "Bot" tab in the left sidebar.
4. Click "Add Bot" and confirm by clicking "Yes, do it!"
5. Under the bot's username, you'll see a "Token" section. Click "Copy" to copy your bot token. Keep this token secret!

### Bot Installation

1. Clone this repository or download the source code:
   ```
   git clone https://github.com/MohdYahyaMahmodi/talkomaticbot.git
   cd talkomaticbot
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Inviting the Bot to Your Server

1. In the Discord Developer Portal, go to the "OAuth2" tab, then "URL Generator".
2. In the "Scopes" section, select "bot" and "applications.commands".
3. In the "Bot Permissions" section, select the following permissions:
   - Read Messages/View Channels
   - Send Messages
   - Embed Links
   - Use Slash Commands
4. Copy the generated URL at the bottom of the page.
5. Open this URL in a new browser tab.
6. Select the server you want to add the bot to and click "Authorize".
7. Complete the captcha if prompted.

## Configuration

1. Open the `bot.py` file in a text editor.
2. Replace `'YOUR_BOT_TOKEN'` with the bot token you copied from the Discord Developer Portal:
   ```python
   TOKEN = 'your_actual_bot_token_here'
   ```
3. Verify that the `API_URL` is correct:
   ```python
   API_URL = 'https://talkomatic.co/rooms'
   ```

## Running the Bot

To start the bot, run the following command in your terminal:

```
python bot.py
```

If everything is set up correctly, you should see a message saying that your bot has connected to Discord.

## Usage

Once the bot is running and added to your Discord server, you can use the following commands:

- `/stats` - Displays overall statistics about Talkomatic rooms and users
- `/rooms` - Shows detailed information about each active Talkomatic room

The bot will also automatically update its status with the current number of rooms and users every 10 seconds.

## Troubleshooting

If you encounter any issues, try the following:

1. Ensure your bot token is correct and hasn't been regenerated.
2. Check that the Talkomatic API is accessible and the URL is correct.
3. Verify that your bot has the necessary permissions in your Discord server.
4. Make sure you're using Python 3.8 or higher.
5. Check the console output for any error messages.

If problems persist, please open an issue on the GitHub repository.

## Contributing

Contributions to the Talkomatic Discord Bot are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the existing coding style.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any questions or support, please open an issue in the GitHub repository or contact the maintainers directly.

Happy chatting with Talkomatic and Discord! 🎉
