import os
import time
import json
time.sleep(5)
os.system('cmdow "C:\\Windows\\py.exe" /ren "BOT LAUNCHER" /TOP /siz 900 300 /mov 775 340')
os.system('cmdow "Bot Launcher" /TOP')
print("######################################################")
print("###                  BOT LAUNCHER                  ###")
print("######################################################")
price_limit = float(input("Escolha um limite mínimo de valor para os projetos: "))

navegadores_limite = ["edge", "webkit", "selenium_firefox"]
navegadores_express = ["edge", "webkit", "selenium_firefox_express"]
navegadores = []
navegadores = navegadores_limite if price_limit > 0.0 else navegadores_express
sp_continuity = 0
screen_positions = [
    '0 0',
    '0 200',
    '0 400',
    '0 600',
    '0 800',
    '600 0',
    '600 200',
    '600 400',
    '600 600',
    '600 800',
    '1200 0',
    '1200 200',
    '1200 400',
    '1200 600',
    '1200 800'
    '1800 0',
    '1800 200',
    '1800 400',
    '1800 600',
    '1800 800'    
]
n = 0

while True:
    if sp_continuity > 19:
        sp_continuity = 0
    print("\nEscolha qual bot você quer rodar:")
    for navegador in navegadores:
        print(f"{n}. {navegador}")
        n = n + 1
    n = 0
    bot = navegadores[int(input("Qual?\n> "))]
    print(bot)
    quantos = int(input("Quantos?\n> "))
    espera = int(input("Intervalo entre a execução de cada bot.\n> "))
    nome = bot.replace('_', ' ').upper()
    
    for i in range(quantos):
        print(f"Inicialização automatica de {bot} a cada {espera} segundos.")
        time.sleep(1)
        print(f'iniciando {nome} e pausando por {espera} segundos até o próximo...')
        os.system(f"%ComSpec% /C Start /high cmdow /run {bot}.py")
        time.sleep(3)
        os.system(f'cmdow "C:\\Windows\\py.exe" /ren {nome} /mov {screen_positions[i]} /siz 600 200') if 'FIREFOX' not in nome else os.system(f'cmdow "Administrator: C:\\Windows\\py.exe" /ren "FIREFOX" /mov {screen_positions[i]} /siz 600 200')
        time.sleep(espera)
        sp_continuity = i + 1
    o_que_fazer = int(input("O que quer fazer agora?\n0. Sair\n1. Rodar mais bots\n> "))
    
    if o_que_fazer == 0:
        break


print("Todas os bots foram iniciados, verifique se não ocorreu nenhum erro em seus consoles.")
input("")
