import os

from telegram.ext import Application, CommandHandler, MessageHandler, filters

from handlers import help_command, message_reply, start_command


def main() -> None:
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("Set TELEGRAM_BOT_TOKEN in your environment first.")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_reply))

    app.run_polling()


if __name__ == "__main__":
    main()
