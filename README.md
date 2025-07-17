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
pip install python-telegram-bot==20.0b0 Pillow
```

### Configuration
- Replace the bot token in `main.py` with your own:
  ```python
  ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
  ```

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
- `README.md` — This file

## Credits
- Built with [python-telegram-bot](https://python-telegram-bot.org/)
- Image processing by [Pillow](https://python-pillow.org/)

---

Enjoy your retro photobooth experience! 🎬 