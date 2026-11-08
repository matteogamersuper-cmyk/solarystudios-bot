
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready() -> None:
    await bot.tree.sync()
    print(f"Connesso come {bot.user}")
    print("Slash Commands sincronizzati!")


@bot.tree.command(name="ping", description="Controlla se il bot è online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Pong! Bot Online :white_check_mark:"
    )


@bot.tree.command(name="website", description="Mostra il sito web")
async def website(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Website: http://node12.zampto.net:31504/"
    )


@bot.tree.command(name="info", description="Mostra informazioni sul bot")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message(
        "Info:\nCreato Da matteogamer254\nLinguaggio Utilizzato: Python"
    )


@bot.tree.command(name="serviceslist", description="Mostra la lista dei servizi")
async def serviceslist(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**Services List**\n"
        "❌ Comando in Arrivo\n"
        "-# Controlla il Canale Annunci per vedere quando il comando sarà disponibile"
    )


def main() -> None:
    token = os.getenv("DISCORD_TOKEN")

    if not token:
        raise RuntimeError("Aggiungi DISCORD_TOKEN al file .env.")

    bot.run(token)


if __name__ == "__main__":
    main()
