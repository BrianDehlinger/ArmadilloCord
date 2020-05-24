# bot.py
import os
import discord
import random


TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD = 'Armadillo Adventure'

client = discord.Client()
users = dict()
zion = ["Zion - Angel's Landing", "Zion - The Subway"]
national_parks = zion

creatures = ['Savage Literer', 'Tree Cutter', 'Climate Change Denier', 'Magical Chainsaw']

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send('Hello')

    if message.content == 'register':        
        if message.author in users:
            await message.channel.send("You're already part of the Naturists!")
        else:
            users[message.author] = {"current_location": None}
            await message.channel.send(f"Welcome to the Naturists {message.author}!")

    if message.content == '#EXPLORE':
        author = message.author 
        users[author]["current_location"] = random.choice(national_parks)
        creature = random.choice(creatures)
        await message.channel.send(f"You are now in {users[author]['current_location']}")
        await message.channel.send(f"You are faced with a {creature}")

client.run(TOKEN)
