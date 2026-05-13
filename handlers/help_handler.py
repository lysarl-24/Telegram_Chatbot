from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Show help\n\n"
        "You can also ask simple questions like 'What is your name?'"
    )
