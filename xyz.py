from revver.revbot import *
from revver.config import *
from revver.functions import *
from revver.start import run
import threading
import time


navegadores_suportados = ["webkit", "firefox", "edge", "chromium"]
navegador = input(f'Qual destes navegadores você quer usar: {str(navegadores_suportados).replace(chr(39), "").replace("[", "").replace("]", "")}?\n> ')
quantidade = int(input('Qual a quantidade de bots rodando?\n> '))


class EdgeBOT():

    def testing(self):
        run(navegador)
        time.sleep(2)

    def __init__(self):
        t = threading.Thread(target=self.testing)
        t.start()


print('======/REVBOT-EXPRESS/=====') if 0.0 == price_limit else print('=========/REVBOT-LIMITED/========')

for i in range(quantidade):
    EdgeBOT()
    printc(f'Iniciando {navegador} {i}...')
    time.sleep(30)

x = 1
for thread in threading.enumerate():
    if not thread.name == 'MainThread':
        thread.name = f'{navegador} {x}'
        x += 1

while True:
    printin(f"Monitorando...")
    time.sleep(1)
