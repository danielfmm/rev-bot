import os
import time
import json

with open('profile.json') as profile_json:
    profile = json.load(profile_json)
    profile_json.close()


price_limit = profile["price_limit"]
navegadores_limite = ["edge", "webkit", "selenium_firefox"]
navegadores_express = ["edge", "webkit", "selenium_firefox_express"]

navegadores = []
navegadores = navegadores_limite if price_limit > 0.0 else navegadores_express


instancias = 12 # deve um numero ser multiplo da quantidade de navegadores existentes
espera = 30
print(f"Inicialização automatica de bots com {instancias} instâncias\niniciadoas cada uma de {espera} em {espera} segunddos.")
multi = int(instancias / len(navegadores))
navegadores = navegadores * multi
navegadores.sort()
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
]
n = 0
time.sleep(1)
os.system('cmdow "C:\\Windows\\py.exe" /ren "Bot Launcher" /TOP /siz 800 300 /mov 850 700')
os.system('cmdow "Bot Launcher" /TOP')
time.sleep(4)
for navegador in navegadores:
    nome = navegador.replace('_', ' ').upper()
    os.system(f"%ComSpec% /C Start /high cmdow /run {navegador}.py")
    time.sleep(espera)
    print(f'iniciando {nome} e pausando por {espera} segundos até o próximo...')
    os.system(f'cmdow "C:\\Windows\\py.exe" /ren {nome} /mov {screen_positions[n]} /siz 600 200') if 'FIREFOX' not in nome else os.system(f'cmdow "Administrator: C:\\Windows\\py.exe" /ren "FIREFOX" /mov {screen_positions[n]} /siz 600 200')
    n = n + 1

print("Todas as instâncias foram iniciadas, verifique se não ocorreu nenhum erro em seus consoles.")
input("")
