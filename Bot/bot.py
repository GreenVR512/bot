import discord
from discord.ext import commands
import asyncio
import threading

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

channel_to_send = None  # Will be set when bot is ready

BAD_WORDS = [
    "fuck", "shit", "bitch", "asshole", "bastard", "dick", "piss", "cunt", "slut",
    "nigga", "nigger", "whore", "faggot", "damn", "crap", "twat", "cock", "prick",
    "retard", "motherfucker", "bullshit", "douche", "dumbass"
]

@bot.event
async def on_ready():
    global channel_to_send
    print(f"✅ Logged in as {bot.user}")
    
    # Replace with your Discord channel ID
    channel_id = 1351691682890121288
    channel_to_send = bot.get_channel(channel_id)
    
    if channel_to_send:
        print("💬 Terminal chat ready! Type messages below.")
        threading.Thread(target=terminal_chat_loop, daemon=True).start()
    else:
        print("⚠️ Could not find the channel. Check the ID.")

def terminal_chat_loop():
    while True:
        msg = input()
        if msg.strip() == "":
            continue
        asyncio.run_coroutine_threadsafe(send_terminal_message(msg), bot.loop)

async def send_terminal_message(msg):
    if channel_to_send:
        await channel_to_send.send(f"[Terminal] {msg}")
    else:
        print("⚠️ Channel not set.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    msg_lower = message.content.lower()
    if any(bad_word in msg_lower for bad_word in BAD_WORDS):
        try:
            await message.delete()
            await message.channel.send(
                f"⚠️ {message.author.mention}, that language isn't allowed.",
                delete_after=5
            )
        except discord.Forbidden:
            print("❌ Missing permission to delete messages.")
    else:
        await bot.process_commands(message)

# 🔑 Put your token below
bot.run("MTM1OTMxNTgyNzI3NDQyMDMzNg.Gdj6di.FdXQuVkQ0pMZMDagiB5_YaNgFnsGTLW4eOocLs")
