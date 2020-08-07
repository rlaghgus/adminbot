import asyncio
import discord
from discord.ext import commands
import random
import os

app = commands.Bot(command_prefix='방장아')

token = "your_token"
calcResult = 0

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("스밍")
    await app.change_presence(status=discord.Status.online, activity=game)

@app.command(pass_context=True)
async def randomNum(ctx, num1, num2):
    picked = random.randint(int(num1), int(num2))
    await ctx.send('뽑힌 숫자는 : '+str(picked))

@app.event
async def on_message(message):
    await app.process_commands(message)
    if message.author.bot:
        return None
    if message.content == "방장아출력":
        await message.channel.send("𝔸𝔻𝕄𝕀ℕ에 의해 출력됨.")
    if message.content.startswith("방장아1부터10"):
        for x in range(10):
            await message.channel.send(x+1)
    if message.content.startswith("방장아계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2]) + int(param[3])
                await message.channel.send("Result : " + str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2]) - int(param[3])
                await message.channel.send("Result : " + str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2]) * int(param[3])
                await message.channel.send("Result : " + str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2]) / int(param[3])
                await message.channel.send("Result : " + str(calcResult))
        except IndexError:
            await message.channel.send("무슨 숫자를 계산할지 알려주세요.")
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")
    param = message.content.split()


    if message.content.startswith("방장아 광고"):
        embed=discord.Embed(title="Example Embed", description="이것은 Embed입니다.", color=0x00ff56)
        embed.set_author(name="저자의 이름", url="https://blog.naver.com/huntingbear21", icon_url="https://cdn.discordapp.com/attachments/541913766296813570/672624076589760512/DRG.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/541913766296813570/672624076589760512/DRG.png")
        embed.add_field(name="이것은 필드입니다.", value="필드의 값입니다.", inline=True)
        embed.add_field(name="이것은 필드 2입니다.", value="필드의 값입니다.", inline=True)
        embed.add_field(name="이것은 필드 3입니다.", value="필드의 값입니다.", inline=True)
        embed.add_field(name="이것은 필드 4입니다.", value="필드의 값입니다.", inline=True)
        embed.set_footer(text="이것은 푸터입니다.")
        await message.channel.send(embed=embed)


    if message.content == "방장아 안녕":
            channel = message.channel
            msg = "안녕"
            await channel.send(msg)
            return None
    if message.content == "방장아 지성이":
            channel = message.channel
            msg = "여친은 윤이"
            await channel.send(msg)
            return None
    if message.content == "방장아 계좌":
            channel = message.channel
            msg = "농협 3511123640683"
            await channel.send(msg)
            return None
    if message.content == "방장아 준서":
            channel = message.channel
            msg = "여친은 유빈이"
            await channel.send(msg)
            return None


from bs4 import BeautifulSoup
import urllib




@app.command(name="블로그검색")
async def _search_blog(ctx, *, search_query):
    temp = 0
    url_base = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query="
    url = url_base + urllib.parse.quote(search_query)
    title = ["", "", ""]
    link = ["", "", ""]
    soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
    result = soup.find_all('a', "sh_blog_title _sp_each_url _sp_each_title")
    embed = discord.Embed(title="검색 결과", description=" ", color=0x00ff56)
    for n in result:
        if temp == 3:
            break
        title[temp] = n.get("title")
        link[temp] = n.get("href")
        embed.add_field(name=title[temp], value=link[temp], inline=False)
        temp+=1
    embed.set_footer(text="검색 완료!")
    await ctx.send(embed=embed)


@app.command(name="추방", pass_context=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+"을(를) 추방하였습니다.")

@app.command(name="밴", pass_context=True)
async def _ban(ctx, *, user_name: discord.Member):
    await user_name.ban()
    await ctx.send(str(user_name)+"을(를) 영원히 매장시켰습니다.")

@app.command(name="언밴", pass_context=True)
async def _unban(ctx, *, user_name):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention}을(를) 회생시켰습니다.")
            return

        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel



@app.command(name="참가", pass_context=True)
async def _join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("채널에 연결되지 않았습니다.")




@app.command(name="연결끊기")
async def _leave(ctx):
    await app.voice_clients[0].disconnect()


import youtube_dl
import re






























access_token = os.environ["BOT_TOKEN"]
app.run(access_token)

