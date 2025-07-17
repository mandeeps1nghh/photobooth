from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, ContextTypes, CallbackQueryHandler
from PIL import Image, ImageDraw, ImageFont, ImageOps
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


user_photos = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat:
        user_photos[update.effective_chat.id] = []
    if update.message:
        await update.message.reply_text("📸 Send me 3 photos to make your photobooth strip!")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat or not update.message or not update.message.photo:
        return
    chat_id = update.effective_chat.id
    if chat_id not in user_photos:
        user_photos[chat_id] = []

    # Download photo
    photo = await update.message.photo[-1].get_file()
    path = f"photo_{chat_id}_{len(user_photos[chat_id])}.jpg"
    await photo.download_to_drive(path)
    user_photos[chat_id].append(path)

    if len(user_photos[chat_id]) < 3:
        await update.message.reply_text(f"✅ Photo {len(user_photos[chat_id])} received. Please send the next one.")
    else:
        await update.message.reply_text("✨ All photos received. Creating your photobooth strip...")
        strip_path = create_strip(user_photos[chat_id])
        restart_markup = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔄 Restart", callback_data="restart")]
        ])
        with open(strip_path, "rb") as f:
            await update.message.reply_photo(
                photo=f,
                caption="📸 Here’s your photobooth strip!",
                reply_markup=restart_markup
            )

        # Cleanup
        for p in user_photos[chat_id]:
            os.remove(p)
        os.remove(strip_path)
        del user_photos[chat_id]

async def handle_done(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat or not update.message:
        return
    chat_id = update.effective_chat.id

    if chat_id not in user_photos or len(user_photos[chat_id]) < 1:
        await update.message.reply_text("Please send at least 1 photo before finishing.")
        return

    strip_path = create_strip(user_photos[chat_id])
    with open(strip_path, 'rb') as strip:
        await update.message.reply_photo(
            strip,
            caption="Here's your filmstrip! 🎞️",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 Restart", callback_data="restart")]
            ])
        )

    # Clear photos to avoid re-use
    user_photos[chat_id] = []
    if os.path.exists(strip_path):
        os.remove(strip_path)

async def handle_restart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if not query or not query.message:
        return
    await query.answer()

    chat_id = query.message.chat.id
    user_photos[chat_id] = []

    # Use context.bot.send_message to reply to the user
    await context.bot.send_message(
        chat_id=chat_id,
        text="Let's start over! 📸\nPlease send your photos one by one."
    )

def create_strip(photo_paths):
    # Image settings
    photo_size = (400, 400)
    spacing = 30
    film_hole_radius = 10
    holes_per_side = 8
    strip_width = photo_size[0] + 120
    strip_height = (photo_size[1] + spacing) * len(photo_paths) + 60

    strip = Image.new('RGB', (strip_width, strip_height), color='black')
    draw = ImageDraw.Draw(strip)

    # Draw film holes
    hole_spacing = strip_height // (holes_per_side + 1)
    for i in range(holes_per_side):
        y = (i + 1) * hole_spacing
        for x in [20, strip_width - 30]:
            draw.ellipse(
                (x, y, x + film_hole_radius * 2, y + film_hole_radius * 2),
                fill="white"
            )

    y_offset = 30
    for path in photo_paths:
        img = Image.open(path).convert("L").resize(photo_size)
        img = ImageOps.expand(img, border=5, fill='white')
        strip.paste(img, ((strip_width - img.width) // 2, y_offset))
        y_offset += img.height + spacing

    output_path = "filmstrip_output.png"
    strip.save(output_path)
    return output_path

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.add_handler(CommandHandler("done", handle_done))
    app.add_handler(CallbackQueryHandler(handle_restart, pattern="^restart$"))
    app.run_polling()
