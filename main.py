import os

import discord
from dotenv import load_dotenv
from discord.ext import commands


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    print(f"Connesso come {bot.user}")


def main() -> None:
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("Aggiungi DISCORD_TOKEN al file .env.")

    bot.run(token)

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong! Bot Online :white_check_mark:")

@bot.command(name="website")
async def website(ctx):
    await ctx.send("Website: http://node12.zampto.net:31504/")

@bot.command(name="info")
async def info(ctx):
    await ctx.send("Info:\nCreato Da matteogamer254\nLinguaggio Utilizzato: Python")

@bot.command(name="serviceslist")
async def serviceslist(ctx):
    await ctx.send("**Services List**")
    await ctx.send("❌ Comando in Arrivo")
    await ctx.send("-# Controlla il Canale Annunci per vedere quando il comando sarà disponibile")
    

if __name__ == "__main__":
    main()