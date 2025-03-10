import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.presences = True  # Nécessaire pour voir les membres hors ligne

bot = commands.Bot(command_prefix='!', intents=intents)

# Configuration
SERVER_ID = 123  # Remplacez par l'ID de votre serveur
EXCLUDED_IDS = [123, 123, 123,]  # IDs à exclure
MESSAGE_CONTENT = "Your message"  # Message to send

has_executed = False  # For start one time

@bot.event
async def on_ready():
    global has_executed
    print(f'Log into bot {bot.user}')

    if not has_executed:
        has_executed = True
        guild = bot.get_guild(SERVER_ID)
        
        if not guild:
            print("Can't find the server")
            return

        print(f"Starting DM Message on {guild.name}...")
        
        for member in guild.members:
            try:
                if member.bot or member.id in EXCLUDED_IDS:
                    continue
                
                await send_dm(member)
                print(f"Message send to {member.display_name}")
                await asyncio.sleep(1)  # Anti-spam
                
            except Exception as e:
                print(f"Error with {member.display_name}: {str(e)}")

async def send_dm(member):
    try:
        await member.send(MESSAGE_CONTENT)
    except:
        raise

# Replace "TOKEN" with your bot token.
bot.run('TOKEN')
