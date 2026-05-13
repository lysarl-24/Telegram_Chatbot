from telegram import Update
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name if update.effective_user else "friend"
    await update.message.reply_text(
        f"Hello {user_name}! I am your chatbot. Type /help to see what I can do."
    )
