from telegram import Update
from telegram.ext import ContextTypes


QUESTION_ANSWERS = {
    "what is your name": "I am your Telegram assistant bot.",
    "how are you": "I am doing great and ready to help you.",
    "who made you": "I was created by my developer.",
}


async def message_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (update.message.text or "").strip().lower()

    if text in QUESTION_ANSWERS:
        await update.message.reply_text(QUESTION_ANSWERS[text])
        return

    await update.message.reply_text(
        "I am not sure about that yet. Try one of: 'what is your name', 'how are you'."
    )
