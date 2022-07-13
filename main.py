import os
import time
import discord
import asyncio
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

@bot.command(name="안녕")
async def hello(ctx):
  with open('goodbye.txt', 'r') as f:
    message = f.readlines()
    await ctx.send(message[1])

@bot.command(name="잘가")
async def goodbye(ctx):
  # path = './goodbye.txt'
  # message = open(path, 'r', encoding = 'utf-8')
  with open('goodbye.txt', 'r') as f:
    message = f.readlines()
    await ctx.send(message[0])

@bot.command(name="입력")
async def input(ctx):
  timeout = 5
  send_message = await ctx.send(f"아무거나 입력하세요! {timeout}초 동안 기다립니다!")

  def check(m):
    return m.author == ctx.message.author and m.channel == ctx.message.channel

  try:
    msg = await bot.wait_for('message', check=check, timeout=timeout)
  except asyncio.TimeoutError:
    await ctx.send("시간이 초과되었습니다. 다시 명령어를 입력해주세요!")
  else:
    await ctx.send(msg.content)
    

bot.run(os.environ['SECRET'])
