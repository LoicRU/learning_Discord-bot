# 🤖 Discord Bot in Python

This project is a **Discord bot written in Python** using the `discord.py` library.
It is designed to help you learn how to create, configure, and extend a Discord bot with **custom commands** and a **custom embed-based help system**.

The bot token is stored securely in a `.env` file so it is **never exposed in the source code**.

---

## ✨ Features

* ❌ Default `!help` command removed
* 📖 **Custom `!help` command** using embeds
* 🏓 **!ping** → Checks if the bot is responding
* 🗣 **!say [message]** → Makes the bot repeat a message
* 👤 **!userinfo [@user]** → Displays user information
* 🧮 **!calc [number] [operator] [number]** → Simple calculator
* 🔐 Secure token management with **python-dotenv**
* ⚙️ Uses **Discord Intents** (Message Content enabled)

---

## 🧠 Available Commands

| Command                         | Description                     |
| ------------------------------- | ------------------------------- |
| `!ping`                         | Checks if the bot is responding |
| `!say <message>`                | Repeats the provided message    |
| `!userinfo [@user]`             | Displays user information       |
| `!calc <num1> <+ - * /> <num2>` | Performs a simple calculation   |
| `!help`                         | Lists all available commands    |

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

Create a `.env` file in the project root:

```env
TOKEN=your_discord_bot_token_here
```

⚠️ **Never share your Discord bot token**

---

## 🤖 Discord Bot Setup

1. Go to the **[Discord Developer Portal](https://discord.com/developers/applications)**
2. Create a new application
3. Add a bot to the application
4. Copy the **Bot Token**
5. Enable **Message Content Intent**
6. Invite the bot to your server

---

## ▶️ Running the Bot

With the virtual environment activated:

```bash
python bot.py
```

If everything works correctly, you will see:

```
✅ Bot connected : YourBotName#1234
```

The bot is now online 🎉

---

## 📖 Custom Help System

The default `!help` command is removed:

```python
bot.remove_command("help")
```

It is replaced with a **custom embed-based help command** that:

* Lists all available commands
* Displays their descriptions (`help="..."`)
* Automatically updates when new commands are added

---

## 🧮 Calculator Command

Examples:

```text
!calc 5 + 3
!calc 10 / 2
!calc 4 * 6
```

Error handling:

* ❌ Division by zero
* ❌ Invalid operator

---

## 📌 Notes

* New commands can easily be added using `@bot.command()`
* Command descriptions automatically appear in `!help`
* Ideal project for learning:

  * `discord.py`
  * embeds
  * intents
  * secure token management

