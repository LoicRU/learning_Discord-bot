# Discord Bot in Python 🤖

This project is a **Discord bot written in Python** using `discord.py`.
It is designed to help you learn how to create, configure, and extend a Discord bot with custom commands and a custom help system.

The bot token is stored securely in a `.env` file so it is **never exposed in the code**.

---

## ✨ Features

* **Custom `!help` command** (default Discord help removed)
* **!ping** → Checks if the bot is responding
* **!say [message]** → Makes the bot repeat a message
* **!userinfo [@user]** → Displays detailed information about a user
* Uses **Discord Intents** (Message Content enabled)
* Secure token management with **python-dotenv**

---

## 🧠 Commands Overview

| Command             | Description                                                   |
| ------------------- | ------------------------------------------------------------- |
| `!ping`             | Replies with `🏓 Pong !`                                      |
| `!say <message>`    | Repeats the provided message                                  |
| `!userinfo [@user]` | Shows user info (ID, bot status, join date, account creation) |
| `!help`             | Displays all available commands with descriptions             |

---

## 📦 Requirements

* **Python 3.12+**
* `pip`
* `venv` (recommended)

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate the virtual environment

**Linux / macOS**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

---

### 4️⃣ Install dependencies

```bash
pip install discord.py python-dotenv
```

---

### 5️⃣ Create a `.env` file

Create a file named `.env` in the project root:

```env
TOKEN=your_discord_bot_token_here
```

⚠️ **Never share your token**

---

## 🤖 Discord Bot Setup

1. Go to the **[Discord Developer Portal](https://discord.com/developers/applications)**
2. Create a new application
3. Add a bot to the application
4. Copy the **Bot Token** into your `.env` file
5. Enable **Message Content Intent** under *Privileged Gateway Intents*
6. Invite the bot to your server

---

## ▶️ Running the Bot

With the virtual environment activated:

```bash
python bot.py
```

If everything works correctly, you will see:

```
✅ Bot connecté : YourBotName#1234
```

The bot will now be online on your server 🎉

---

## 🛠 Custom Help System

The default Discord help command is disabled and replaced with a custom embed-based help command:

```python
bot.remove_command("help")
```

The `!help` command automatically lists:

* All available commands
* Their descriptions (defined with `help="..."`)

This makes the bot easier to use and more user-friendly.

---

## 📌 Notes

* You can easily add new commands using `@bot.command()`
* Descriptions automatically appear in `!help`
* This project is ideal for learning **discord.py basics**

