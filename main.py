import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from os import environ

load_dotenv()

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

bot.run(environ.get("DISCORD_TOKEN"))
