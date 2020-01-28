import discord
import asyncio
import datetime
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('등장!')

@bot.command()
async def 핑(ctx):
    await ctx.send('당신의 핑 정보 : {0}초'.format(bot.latency))  
@bot.command()
async def 명령어(ctx):
    embed = discord.Embed(colour = 0x00f000)
    embed.add_field(name='핑', value='!핑 - 사용자의 핑 정보를 알려줍니다', inline=False)
    embed.add_field(name='프로필', value='!프로필 - 사용자의 프로필 정보를 알려줍니다', inline=False)
    await ctx.send(embed=embed)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name='Admin : Kener#0001', type=discord.ActivityType.playing))
@bot.command()
async def 프로필(ctx, member: discord.Member):
    embed = discord.Embed(color = 0x00f000)
    embed.add_field(name='이름', value=member, inline=False)
    await ctx.send(embed=embed)

bot.run('NjcxMzQ0MjMxNjAzNzY1Mjc4.Xi7kDw.x5mCYRFxsKTP7i4JKGmDiYbwaNI') 