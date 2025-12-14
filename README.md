# Discord Bot in Python

This project is a **Discord bot** written in Python, designed to help learn how to create and manage a Discord bot.  
The bot’s token is secured in a `.env` file so it is not exposed in the code.  

---

## Features  

* Responds to the `!ping` command with `🏓 Pong!`  
* Token configuration via a `.env` file  
* Uses **Discord Intents** to read message content  
* Easy to extend with new commands  

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

4. Install the dependencies:

```bash
pip install discord.py python-dotenv
```

5. Create a `.env` file in the project folder with your Discord token:

```env
TOKEN=your_token_here
```

---

## Bot Configuration on Discord

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)  
2. Create an application  
3. Add a bot  
4. Copy the **TOKEN** into the `.env` file  
5. Enable **Privileged Gateway Intents** if needed (Message Content Intent)  

---

## Running the Bot

In your terminal, with the virtual environment activated:  

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

* `!ping` → The bot responds with `🏓 Pong!`  
> You can easily add new commands in `bot.py`.  
