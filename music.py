import discord
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
import random
import os

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print('봇이 로그인되었습니다.')

    # 예약된 시간에 메시지를 보내는 함수 실행
    await send_message_at_time("07:00", "좋은 아침이에요, 여행자님. 아침부터 이렇게 만나다니··· 오늘은 모든 일이 잘 풀리겠어요")
    await send_message_at_time("12:00", "즐거운 오후에요. 점심을 먹고 난 후의 식곤증은 어쩔 수 없죠. 바둑을 두면서 졸음을 쫓는 건 어때요?")
    await send_message_at_time("18:00", "좋은 저녁이에요. 밤바람이 포근하니 아름다운 밤이 될 것 같네요")
    await send_message_at_time("22:00", "「꿈인 줄 알았다면 깨지 않았을 것을, 실제 만남보다 낫지 아니한가」")

async def send_message_at_time(target_time, message):
    while True:
        now = datetime.now().strftime("%H:%M")
        if now == target_time:
            channel = bot.get_channel(970942440309673994)  # 메시지를 보낼 채널 ID로 대체해야 합니다.
            await channel.send(message)
            break

        # 다음 날 00시로 시간 갱신
        next_day = datetime.now() + timedelta(days=1)
        next_day = next_day.replace(hour=0, minute=0, second=0, microsecond=0)

        # 현재 시간과 다음 날 00시 사이의 시간 간격 계산
        time_diff = (next_day - datetime.now()).total_seconds()

        # 계산된 시간 간격만큼 대기
        await asyncio.sleep(time_diff)

@bot.event
async def on_message(message):
    if message.content.startswith("안녕 아야카"):
        await message.channel.send("이나즈마의 카미사토류 태도술 계승자——카미사토 아야카, 참전! 잘 부탁드려요")
    await bot.process_commands(message)

@bot.command()
async def 투표(ctx, *, number):
    global Ftext
    correct = 0
    global Flist
    titlename = str(ctx.message.author.name) + "여행자의 투표에요."
    embed = discord.Embed(title = titlename, description = number, color = 0x00ff00)
    embed.add_field(name = "맞다:o:", value = "⠀", inline = False)
    embed.add_field(name = "아니다:x:", value = "⠀", inline = False)
    Flist = await ctx.send(embed = embed)
    await Flist.add_reaction("⭕")
    await Flist.add_reaction("❌")

@bot.command()
async def 설문(ctx, *, number):
    global Ftext
    correct = 0
    global Flist
    titlename = str(ctx.message.author.name) + "여행자의 설문이에요"
    embed = discord.Embed(title = titlename, description = number, color = 0x00ff00)
    embed.add_field(name = "매우 그렇다/그렇다/보통이다/아니다/매우 아니다", value = "⠀", inline = False)
    Flist = await ctx.send(embed = embed)
    await Flist.add_reaction("1️⃣")
    await Flist.add_reaction("2️⃣")
    await Flist.add_reaction("3️⃣")
    await Flist.add_reaction("4️⃣")
    await Flist.add_reaction("5️⃣")

@bot.command()
async def 숫자뽑기(ctx):
    global Ftext
    correct = 0
    global Flist
    titlename = str(ctx.message.author.name) + "여행자의 숫자에요"
    embed = discord.Embed(title = titlename, color = 0x00ff00)
    embed.add_field(name = random.sample(range(1,100),1), value = "⠀", inline = False)
    Flist = await ctx.send(embed = embed)

@bot.command()
async def ox(ctx):
    global Ftext
    correct = 0
    global Flist
    ox = ['맞다고 생각해요' , '아니라고 생각 해요']
    titlename = str(ctx.message.author.name) + "아야카의 선택이에요"
    embed = discord.Embed(title = titlename, color = 0x00ff00)
    embed.add_field(name = random.choice(ox), value = "⠀", inline = False)
    Flist = await ctx.send(embed = embed)

@bot.command()
async def 가위바위보(ctx):
    com=random.randint(1,9)
    if com==1:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 가위, 아야카는 가위\r\n 무승부네요.. 다음에 한판 더 해요. 여행자님.'), color = 0x00ff00))
    
    if com==2:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 가위, 아야카는 바위\r\n 제가 이겼어요 여행자님'), color = 0x00ff00))
    
    if com==3:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 가위, 아야카는 보자기\r\n 여행자님이 이겼어요 축하해요.'), color = 0x00ff00))
    
    if com==4:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 바위, 아야카는 가위\r\n 여행자님이 이겼어요 축하해요.'), color = 0x00ff00))
    
    if com==5:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 바위, 아야카는 바위\r\n 무승부네요.. 다음에 한판 더 해요. 여행자님.'), color = 0x00ff00))
    
    if com==6:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 바위, 아야카는 보자기\r\n 제가 이겼어요 여행자님'), color = 0x00ff00))
    
    if com==7:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 보자기, 아야카는 가위\r\n 제가 이겼어요 여행자님'), color = 0x00ff00))
    
    if com==8:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자은 보자기, 아야카는 바위\r\n 여행자님이 이겼어요 축하해요.'), color = 0x00ff00))
    
    if com==9:
      await ctx.send(embed = discord.Embed(title='가위바위보',description=(f'{ctx.message.author.mention}여행자님은 보자기, 아야카는 보자기\r\n 무승부네요.. 다음에 한판 더 해요. 여행자님.'), color = 0x00ff00))



access-token = os.environ["BOT_TOKEN]
bot.run(access-token)
