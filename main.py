import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
from os import environ
import asyncio
import random
from typing import Optional

load_dotenv()

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def pong(ctx):
    await ctx.send("Ping!")

@bot.command()
async def foo(ctx):
    await ctx.send("Bar!")

@bot.command()
async def about(ctx):
    await ctx.reply("Hello, This is Wump a Friendly Python Discord Bot!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pinging...")
    latency = bot.latency * 1000
    await ctx.reply(f"The bots latency is: {latency:.2f}ms'")

@bot.command()
async def bye(ctx):
    await ctx.send("Goodbye in 3 seconds...", delete_after=3.0)

@bot.command()
async def guess(ctx, guess: Optional[int] = None):
    def is_correct(message):
        return message.author == ctx.author and message.content.isdigit()
    answer = random.randint(1,10)
    if not guess:
        await ctx.send("Guess a number between 1 and 10. ")
        try:
            guess = await bot.wait_for("message", check=is_correct, timeout=5.0)
            guess = guess.content
        except asyncio.TimeoutError:
            return await ctx.send(f"Sorry, you took too long it was {answer}. ")
    if int(guess) == answer:
        await ctx.reply("You are right!") 
    else:
        await ctx.reply(f"Oops. It is actualy {answer}.") 

@bot.command()
async def hello(ctx):
    await ctx.send("Hello, world! \n Nice to meet you.")          

@bot.command()
async def headortails(ctx, answer):
    if random.choice(["heads", "tails"])  == answer:
        await ctx.reply("Congratulations!")
    else:
        await ctx.reply("Sorry you lost")

bot.run(environ.get("DISCORD_TOKEN"))
