import os
import math
import time

# 1080 / 200 = 5
# 2500 / 300 = 4

tela_vertical = 1000
tela_horizontal = 2500
janela_vertical = 200
janela_horizontal = 600

quantidade_vertical = int(tela_vertical / janela_vertical)
quantidade_horizontal = int(tela_horizontal / janela_horizontal)
quantidade = quantidade_horizontal * quantidade_vertical
pulo_vertical = 0
pulo_horizontal = 0
x = 1
y = 1
print(quantidade)
print(quantidade_horizontal)
print(quantidade_vertical)
print(x)
print(pulo_horizontal)
print(pulo_vertical)
#input()


for i in range(quantidade):

	
	os.system('%ComSpec% /C Start /High cmdow /run cmd')
	time.sleep(5)
	os.system(f'cmdow "Administrator: C:\\Windows\\System32\\cmd.exe" /REN "CMD {i}" /SIZ {str(janela_horizontal)} {str(janela_vertical)} /MOV {str(pulo_horizontal)} {str(pulo_vertical)}')
	print(i)
	pulo_horizontal = pulo_horizontal + janela_horizontal
	if (i+1) / quantidade_horizontal == x:
		pulo_vertical = pulo_vertical + janela_vertical
		pulo_horizontal = 0
		x = x + 1
	
	#input()

# 	elif pulo_vertical >= quantidade_vertical:
# 		os.system(f'%ComSpec% /C Start /high cmdow /run "notepad" /siz 240 200 /mov {janela_horizontal * i} {pulo_vertical + janela_horizontal}')
# 	time.sleep(5)
# #	os.system(f'cmdow "Untitled - Notepad" /ren "Notepad {i}" /siz 240 200 /mov {str(int(i * 216))} 0')
#	time.sleep(5)
