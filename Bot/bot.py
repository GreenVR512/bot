import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot.run(os.getenv("MTM1OTMxNTgyNzI3NDQyMDMzNg.GWC-16.PPvjzRDu5gk8oGhzpfBPAWbvoU7_9sBZIICa1c"))
