#Client Events
import discord
from discord.ext import commands
from dotenv import load_dotenv

def Run_Client_Events(client):
    #Changes new Members Nickname and Changes Role as Specified
    @client.event
    async def on_member_join(member):
        nick=member.name+' Sheep'
        await member.edit(nick=nick)
        await member.edit(roles=list[Scrub])
