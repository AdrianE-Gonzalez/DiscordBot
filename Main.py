
#Imports Needed For Bot 
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import Bot_Commands
import Client_Events


#Gets the Tokens Saved for Bot on the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Variables Used to Access Bot and Client
client = discord.Client()
bot = commands.Bot(command_prefix='!')


#Client Events
Client_Events.Run_Client_Events(client)

#Bot Commands
Bot_Commands.Run_Bot_Commands(bot)

bot.run(TOKEN)