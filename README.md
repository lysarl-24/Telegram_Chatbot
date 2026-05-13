# Telegram Chatbot Project

A clean starter structure for a Python Telegram chatbot with separate folders for greeting and question-answer content.

## Project Structure

```text
Telegram_Chatbot/
+- bot.py
+- .gitignore
+- README.md
+- handlers/
¦  +- __init__.py
¦  +- start_handler.py
¦  +- help_handler.py
¦  +- message_handler.py
+- content/
¦  +- greetings/
¦  ¦  +- greetings.json
¦  +- qa/
¦     +- questions_answers.json
+- docs/
   +- INTRODUCTION.md
```

## Files Overview

- `bot.py`: Main entry point, registers command/message handlers.
- `handlers/start_handler.py`: `/start` greeting behavior.
- `handlers/help_handler.py`: `/help` command output.
- `handlers/message_handler.py`: Basic question and answer logic.
- `content/greetings/greetings.json`: Greeting text collection.
- `content/qa/questions_answers.json`: Question-answer dataset.
- `docs/INTRODUCTION.md`: Intro and project goals.

## Setup

1. Create and activate virtual environment.
2. Install dependency:

```bash
pip install python-telegram-bot
```

3. Set your bot token:

```powershell
$env:TELEGRAM_BOT_TOKEN="your_token_here"
```

4. Run the bot:

```bash
python bot.py
```

## Next Improvement Ideas

- Load greetings and Q&A from JSON in handlers (dynamic content).
- Add `config.py` for centralized settings.
- Add logging and error handler.
- Add unit tests for message matching.
