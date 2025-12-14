# Discord Bot in Python

This project is a **Discord bot** written in Python, designed to help you learn how to create and manage a Discord bot.

The bot token is stored securely in a `.env` file so it is not exposed in the code.

---

## Current Features

* **!ping** → The bot replies with `🏓 Pong!`
* **!say [message]** → The bot repeats the message you write
* **!userinfo [@user]** → Shows information about a member (username, ID, whether the user is a bot, date they joined the server, and account creation date)
* Token configuration through a `.env` file
* Uses **Discord Intents** to read message content

---

## Installation

### Prerequisites

* Python 3.12 or higher
* `pip`
* `virtualenv` (recommended)

### Steps

1. Clone this repository:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. Create a virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

```bash
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

4. Install dependencies:

```bash
pip install discord.py python-dotenv
```

5. Create a `.env` file in the project folder with your Discord bot token:

```env
TOKEN=your_token_here
```

---

## Bot Configuration on Discord

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Create a new application
3. Add a bot to the application
4. Copy the **TOKEN** into your `.env` file
5. Enable **Privileged Gateway Intents** if needed (Message Content Intent)

---

## Running the Bot

With the virtual environment activated, run:

```bash
python bot.py
```

If everything is correct, you will see in the terminal:

```
✅ Bot connected: MyPythonBot#1234
```

And the bot will be online on your Discord server.

---

## Available Commands

* `!ping` → Bot replies with `🏓 Pong!`
* `!say [message]` → Bot repeats the message
* `!userinfo [@user]` → Displays information about a member

> You can easily add more commands in `bot.py`.
