import os
import json
import time


my_title = 'POWEREDGE'


# 1080 / 200 = 5
# 2500 / 300 = 4
#################


def main():
	perfil = importar_perfil()
	print("========================> |POWEREDGE| <========================")
	valor_limite = float(input("Escolha um valor mínimo para o trabalho. (0 = express)\n> "))
	#print(perfil)
	perfil['price_limit'] = valor_limite
	#print(perfil)
	exportar_perfil(perfil)
	poweredge()


def importar_perfil():
    with open('profile.json', 'r') as perfil_json:
        perfil = json.load(perfil_json)
        perfil_json.close()
    return perfil


def exportar_perfil(novo_perfil):
    with open('profile.json', 'w') as novo_json:
        novo_json = json.dump(novo_perfil, novo_json, indent = 4)



def poweredge():
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

	
	quantidade = int(input("Insira a quantidade de EdgeBOT que quer rodar\n> "))
	#quantidade = 16

	for i in range(quantidade):
		print(f"Iniciando EdgeBOT {i}...")
		os.system(f"%ComSpec% /C Start /High cmdow /RUN edge.py")
		time.sleep(15)
		os.system(f'cmdow "C:\\Windows\\py.exe" /ren "EDGE {i}" /SIZ {str(janela_horizontal)} {str(janela_vertical)} /MOV {str(pulo_horizontal)} {str(pulo_vertical)}')

		
		pulo_horizontal = pulo_horizontal + janela_horizontal
		
		if (i+1) / quantidade_horizontal == x:
			pulo_vertical = pulo_vertical + janela_vertical
			pulo_horizontal = 0
			x = x + 1
	print("Concluído!")


if __name__ == "__main__":
	os.system("title " + my_title)
	main()
	input('')
