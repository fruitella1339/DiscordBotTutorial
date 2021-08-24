from discord.ext.commands import Bot

import os

bot = Bot(command_prefix="!") # creating bot object

# Creating "ON READY" EVENT
@bot.event
async def on_ready():
    print(f" > {bot.user} successfully connected")

# Loading COGS here
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run("token here") # starting a bot