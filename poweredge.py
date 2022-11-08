import os
import time
print("POWEREDGE ON THE WAY...")
# 1080 / 200 = 5
# 2500 / 300 = 4

tela_vertical = 1080
tela_horizontal = 2560
janela_vertical = 200
janela_horizontal = 600

quantidade_vertical = int(tela_vertical / janela_vertical)
quantidade_horizontal = int(tela_horizontal / janela_horizontal)
quantidade = quantidade_horizontal * quantidade_vertical
pulo_vertical = 0
pulo_horizontal = 0
x = 1

quantidade = 14

for i in range(quantidade):
	os.system(f"%ComSpec% /C Start /High cmdow /run edge.py")
	time.sleep(30)
	os.system(f'cmdow "C:\\Windows\\py.exe" /ren "EDGE {i+1}" /SIZ {str(janela_horizontal)} {str(janela_vertical)} /MOV {str(pulo_horizontal)} {str(pulo_vertical)}')
	
	pulo_horizontal = pulo_horizontal + janela_horizontal
	
	if (i+1) / quantidade_horizontal == x:
		pulo_vertical = pulo_vertical + janela_vertical
		pulo_horizontal = 0
		x = x + 1
