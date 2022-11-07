import time
import discord
from discord import Spotify, Activity, ActivityType
from discord.ext import commands, tasks
import asyncio
from playwright.async_api import async_playwright
bad_words = ["buceta", "cu", "bolsonaro", "piroca"]

BOT_TOKEN = 'MTAyODM2NzEyNTM2NDA4NDgyNw.G1aeMl.M3211e5dQrt69PDEe0QngcsU2UQYWuuTyMt8aU'
CHANNEL_ID = 1028197388059430962
LOG_CHANNEL_ID = 711276905692659844

intents = discord.Intents().all()

bot = commands.Bot("!", intents=intents)


# channel = bot.get_channel(CHANNEL_ID)
# channel_log = bot.get_channel(LOG_CHANNEL_ID)

def timestamp():
    return time.strftime('%H:%M:%S')


@bot.event
async def on_ready():
    print(f"Bot online e logado como {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    channel_log = bot.get_channel(LOG_CHANNEL_ID)
    #await channel.send("Shuklambaradaram Vishnum!")
    #await channel_log.send("Monitoramento ativado.")
    #current_time.start()


@bot.event
async def on_presence_update(before, after):

    ############################################################
    ### Função que identifica status (on/offline) do usuário ###
    ############################################################

    online = ["dnd", "idle", "online"]
    status_translations = {
        "dnd": "ocupado",
        "idle": "ausente",
        "online": "online",
        "offline": "offline"
    }
    channel_log = bot.get_channel(LOG_CHANNEL_ID)
    if before.status != after.status:
        if str(after.status) == "offline" or str(after.status) in online:
            await channel_log.send(f"({timestamp()}) {after.name} ficou {status_translations[str(after.status)]}.")
            print(f"({timestamp()}) {after.name} ficou {after.status}.")

    ########################################################
    ### Função que identifica a atividade/jogo do membro ###
    ########################################################
    bug = False
    if before.activity != after.activity:
        print("before", before.activity)
        print("after", after.activity)
        condition_to_send = (str(after.activity) != "Spotify" or str(before.activity) != "Spotify")
        print("condition_to_send", condition_to_send)

        if after.activity:            
            if str(after.activity) == "Spotify":
                user = after
                for activity in user.activities:
                    if isinstance(activity, Spotify):
                        print(activity.title)
                        await channel_log.send(f"{after.name} está escutando {activity.title} de {activity.artist}")
                    else:
                        bug = True
                        print("nao conseguiu pegar a música")

            elif str(before.activity) != "Spotify" and not bug:
                await channel_log.send(f"({timestamp()}) {after.name} iniciou {after.activity.name}.")

        elif before.activities and after.activity and condition_to_send:
             bug = False
             await channel_log.send(f"({timestamp()}) {before.name} encerrou {before.activity.name}.")

             #print(f"({timestamp()}) {before.name} encerrou {before.activity.name}.")


@bot.event
async def on_member_update(before, after):
    channel_log = bot.get_channel(LOG_CHANNEL_ID)
    print(before.activity)
    if before.activity != after.activity:
        #await channel_log.send(f"({timestamp()}) {after.name} ligou o {after.activity}.")
        print(after.activity)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    user_message = message.content.split()
    for word in user_message:
        if word in bad_words:
            await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários.")
            channel_log = bot.get_channel(LOG_CHANNEL_ID)
            await channel_log.send(f"({timestamp()}) {message.author} escreveu um palavrão. Quote: {message.content}")
            await message.delete()
            break

    await bot.process_commands(message)



@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name

    response = "Olá, " + name

    await ctx.send(response)


@bot.command(name="desligar")
async def shutdown(ctx):
    name = ctx.author.name
    response = f'Até logo, {name}.'
    await ctx.send(response)
    exit()


@bot.command(name="manga")
async def last_chapter(ctx, *title):
    mangas = {'black clover': "https://onepiecechapters.com/mangas/3/black-clover",
              'chainSaw man': "https://onepiecechapters.com/mangas/13/chainsaw-man",
              'hunter x hunter': "https://onepiecechapters.com/mangas/15/hunter-x-hunter",
              'jujutsu kaisen': "https://onepiecechapters.com/mangas/4/jujutsu-kaisen",
              'my hero academia': "https://onepiecechapters.com/mangas/6/my-hero-academia",
              'one piece': "https://onepiecechapters.com/mangas/5/one-piece",
              'one-punch man': "https://onepiecechapters.com/mangas/10/one-punch-man"
              }
    lista_de_mangas = list(mangas.keys())
    ftitle = ""
    for arg in title:
        ftitle = f"{str(ftitle)}{str(arg)} "
    ftitle = ftitle.lower()[:-1]
    print(ftitle)
    print(ftitle)
    print(lista_de_mangas)

    if ftitle in lista_de_mangas:
        p = await async_playwright().start()
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(mangas[ftitle])
        all_caps = await page.inner_text('//*[@id="img-container"]/main/div[1]/div/div/div[1]')
        all_caps = all_caps.split('\n')
        URL = await page.eval_on_selector('#img-container > main > div.overflow-hidden > div > div > div.col-span-2 > a:nth-child(2)', 'el => el.href')
        await browser.close()
        response = f"Último capítulo dísponivel: {all_caps[1]}, {all_caps[2]}\n{URL}"
        await ctx.send(response)
    else:
        mangas_disp = ""
        for manga in lista_de_mangas:
            mangas_disp = f"{mangas_disp}\n{manga.upper()}"
        response = f'Lista de mangás disponíveis: {mangas_disp}\nBasta digitar o comando !manga <nome do manga na lista> que verá o último capítulo lançado.'
        await ctx.send(response)





@bot.command(name="jujutsu")
async def jujutsu_info(ctx):
    p = await async_playwright().start()
    browser = await p.chromium.launch()
    page = await browser.new_page()
    await page.goto("https://onepiecechapters.com/mangas/4/jujutsu-kaisen?2022-10-286178")
    all_caps = await page.inner_text('//*[@id="img-container"]/main/div[1]/div/div/div[1]')
    all_caps = all_caps.split('\n')
    text_to_click = f"text={all_caps[1]}"
    await page.click(text_to_click)
    URL = page.url
    response = f"Último capítulo dísponivel: {all_caps[1]}, {all_caps[2]}\n{URL}"
    await ctx.send(response)


@tasks.loop(hours=1)
async def current_time():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f'Hora atual: {timestamp()}')


bot.run(BOT_TOKEN)
