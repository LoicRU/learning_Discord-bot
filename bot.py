import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot connecté : {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong !")

# Utiliser la variable TOKEN
bot.run(TOKEN)
