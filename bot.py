import discord
from discord.ext import commands
import os
import asyncio
import random


client = commands.Bot(command_prefix = '-')


@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.online)

  await client.change_presence(activity=discord.Game(name="랜덤숫자봇"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)
  
@client.event
async def on_message(message):
    if message.author.bot:  # 만약 메시지를 보낸사람이 봇일 경우에는
        return None  # 동작하지 않고 무시합니다.

    id = message.author.id  # id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel  # channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
   
    if message.content == '!뽑기':
        channel = message.channel
        randomNum = random.randint(0, 367)
        user = message.author
        name = user.display_name
        await channel.send(name+"의 뽑기 결과 : "+str(Num))
                



client.run(os.environ['token'])

