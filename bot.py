import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print(f"✅ Bot connecté : {bot.user}")

@bot.command(help="Vérifie si le bot répond")
async def ping(ctx):
    await ctx.send("🏓 Pong !")

@bot.command(help="Répète un message")
async def say(ctx, *, message):
    await ctx.send(message)

@bot.command(help="Donne toutes les info de l'utilisateur")
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f"User Info - {member}", color=discord.Color.blue())
    embed.add_field(name="Username", value=str(member), inline=True)
    embed.add_field(name="ID", value=member.id, inline=True)
    embed.add_field(name="Bot?", value=member.bot, inline=True)
    embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d"), inline=True)
    embed.add_field(name="Created Account", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
    await ctx.send(embed=embed)

@bot.command(help="liste toutes les commandes")
async def help(ctx):
    help = discord.Embed(
        title="📖 Aide - Commandes",
        color=discord.Color.green()
    )

    for command in bot.commands:
        help.add_field(
            name=f"!{command.name}",
            value=command.help or "Pas de description",
            inline=False
        )

    await ctx.send(embed=help)

bot.run(TOKEN)
