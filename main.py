import os
import time
import discord
from socket import timeout
from unicodedata import name
from discord.ext import commands

# bot initial settings
prefix = '!'
intents = discord.Intents.default()
bot = commands.Bot(command_prefix = prefix, intents=intents)

# bot status
@bot.event
async def on_ready():
  print("로그인 중입니다.")
  print(f"봇 = {bot.user.name}으로 연결 중")
  print("연결이 완료되었습니다.")
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(""))
