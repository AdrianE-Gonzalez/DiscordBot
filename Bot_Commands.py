import discord
from discord.ext import commands
from dotenv import load_dotenv

#Bot Commands
def Run_Bot_Commands(bot):

    #User Commands
    @bot.command(name='hi')
    async def say_hi(ctx):
        await ctx.send('Sup')

    #Admin Commands
    @bot.command(name='create_category')
    @commands.has_role('admin')
    async def create_channel(ctx, channel_name):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_category_channel(channel_name)
            Category= discord.utils.get(guild.categories,name=channel_name)
            await guild.create_text_channel(channel_name+ " Text Chat", category=Category)
            await guild.create_voice_channel(channel_name+" Voice Chat", category=Category)
