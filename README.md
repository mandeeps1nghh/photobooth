# Telegram Photobooth Strip Bot

A Telegram bot that creates a retro photobooth filmstrip from user-submitted photos! Users send 3 photos, and the bot returns a stylish vertical filmstrip with film holes, grayscale effect, and a restart button for easy retakes.

## Features
- 📸 Collects 3 photos from each user
- 🎞️ Generates a vertical photobooth strip with film holes and white borders
- 🖤 Converts photos to black & white for a retro look
- 🔄 Inline "Restart" button to start over at any time
- 🧹 Automatically cleans up temporary files

## Demo
1. Start the bot with `/start`
2. Send 3 photos, one by one
3. Receive your custom photobooth strip as an image
4. Use the "🔄 Restart" button to make a new strip

## Setup & Installation

### Prerequisites
- Python 3.8+
- Telegram Bot Token ([Get one from BotFather](https://t.me/BotFather))

### Install dependencies
```bash
pip install -r requirements.txt
```

### Configuration: Using Environment Variables

1. **Create a `.env` file in your project directory:**
   ```env
   BOT_TOKEN=your-telegram-bot-token-here
   ```
2. **(Optional) Set the environment variable manually:**
   - **Windows:**
     ```cmd
     set BOT_TOKEN=your-telegram-bot-token-here
     python main.py
     ```
   - **Linux/Mac:**
     ```bash
     export BOT_TOKEN=your-telegram-bot-token-here
     python main.py
     ```

### Code automatically loads the token from `.env` using [python-dotenv](https://pypi.org/project/python-dotenv/).

### Run the bot
```bash
python main.py
```

## Usage
- `/start` — Begin a new photobooth session
- Send 3 photos, one at a time
- Receive your filmstrip
- Press "🔄 Restart" to start over

## File Structure
- `main.py` — Main bot logic
- `requirements.txt` — Python dependencies
- `README.md` — This file

## Credits
- Built with [python-telegram-bot](https://python-telegram-bot.org/)
- Image processing by [Pillow](https://python-pillow.org/)
- Environment variable support by [python-dotenv](https://pypi.org/project/python-dotenv/)

---

Enjoy your retro photobooth experience! 🎬 
