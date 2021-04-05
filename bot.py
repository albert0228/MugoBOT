import asyncio
import discord
import random
import openpyxl

client = discord.Client()
wb = openpyxl.load_workbook('Sheet.xlsx')
test = wb["Sheet1"]   # '이름'이라는 워크시트 불러오기
wordlist = []


i = 0




randomNum = 0
randomList = ["멍체","냥체","중2병체","뀨체","TS","뱀파체(나른) ","성좌체","마들렌체(자신감뿜뿜)!","3인칭체","사벽이체 (제4의벽)","네모네모체(ㅇ>ㅁ)","나이변경","주인님체","나이변경","사극체","단답체","홍이체"]


# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("로그인 된 봇:")  # 화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("!부럼으로 부럼을 까보세요!")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        

# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.

# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot:  # 만약 메시지를 보낸사람이 봇일 경우에는
        return None  # 동작하지 않고 무시합니다.

    id = message.author.id  # id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel  # channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.
    i = 1

    id = id // 10000000000
  
    while i<15:
        if test['A'+str(i)].value == id:
            break
        i = i + 1

    
    if message.content == '!돈':
      await channel.send(str(test['C'+str(i)].value))

    if message.content.startswith('!닉변경 '):
        wordlist = (message.content).split('!닉변경 ')
        await channel.send("닉네임을 "+wordlist[1]+"으로 변경하셨습니다!")
        test['B'+str(i)] = wordlist[1]
      
    if message.content == '!아이디확인':
      await channel.send(str(id))
      
    if message.content == '!부럼':
        channel = message.channel
        randomNum = random.randint(0, 16)

        
        name = test['B'+str(i)].value
       

        if randomList[randomNum] == "나이변경":
            await channel.send(">이름 : "+name+"\n>부럼 결과 : "+randomList[randomNum]+"\n>부럼 시간 : "+str(random.randint(5, 30))+"분\n>나이 : "+str(random.randint(12,22))+"세")
            
        else:
            await channel.send(">이름 : "+name+"\n>부럼 결과 : "+randomList[randomNum]+"\n>부럼 시간 : "+str(random.randint(5, 30))+"분")
        


        
        


client.run(token)



