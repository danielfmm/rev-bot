import os
import json
import time
import threading


my_title = 'POWEREDGE'
ls = []
# 1080 / 200 = 5
# 2500 / 300 = 4
#################


def main():
	perfil = importar_perfil()
	valor_limite = float(input("Escolha um valor mínimo para o trabalho. (0 = express)\n> "))
	perfil['price_limit'] = valor_limite
	exportar_perfil(perfil)
	poweredge()


def importar_perfil():
	with open('profile.json', 'r') as perfil_json:
		perfil = json.load(perfil_json)
		perfil_json.close()
	return perfil


def exportar_perfil(novo_perfil):
	with open('profile.json', 'w') as novo_json:
		json.dump(novo_perfil, novo_json, indent=4)



def poweredge(first_time=True):
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

	if first_time:
		quantidade = int(input("Insira a quantidade de EdgeBOT que quer rodar\n> "))
	else:
		quantidade = len(ls)


	for i in range(quantidade):
		ls.append(i)
		print(f"Iniciando EdgeBOT {i}...")
		os.system(f"%ComSpec% /C Start /High cmdow /RUN edge.py")
		time.sleep(15)
		os.system(f'cmdow "C:\\Windows\\py.exe" /ren "EDGE {i}" /SIZ {str(janela_horizontal)} {str(janela_vertical)} /MOV {str(pulo_horizontal)} {str(pulo_vertical)}')

		
		pulo_horizontal = pulo_horizontal + janela_horizontal
		
		if (i+1) / quantidade_horizontal == x:
			pulo_vertical = pulo_vertical + janela_vertical
			pulo_horizontal = 0
			x = x + 1
	print("Todos os bots rodando.")


def limit():
	print(f"Vamor mínimo de trabalho é {importar_perfil()['price_limit']}")


def killbot(window):
	try:
		if window[0].lower() == 'all':
			for i in ls:
				os.system(f'cmdow "EDGE {i}" /CLS')
				time.sleep(2)
		else:
			os.system(f'cmdow "{window[0]} {window[1]}" /CLS')

	except TypeError as e:
		print("Bot não encontrado.")


def help_commands():
	print("Lista de de comandos:\n1. Comando 1\n2. Comando 2")


def restart():
	print("Reiniciando os bots...")
	killbot("all")
	time.sleep(4)
	#poweredge(False)


def change_limit(new_limit):
	perfil = importar_perfil()
	perfil['price_limit'] = float(new_limit)
	exportar_perfil(perfil)


def cli():
	while True:
		cmds = {
			"killbot": killbot,
			"help": help_commands,
			"limit": limit,
			"change_limit": change_limit,
			"restart": restart

		}

		cmd = input('> ')
		command = cmd.split()
		try:
			app = command[0].lower()
			if app == 'exit':
				break
			cmds[app](command[1::]) if command[1::] else cmds[app]()
		except KeyError as e:
			print("Comando inválido.")
			continue
		except IndexError as e:
			continue


class EdgeBOT:


	def run(self):
		main()
		time.sleep(1)
		cli()


	def __init__(self):
		t = threading.Thread(target=self.run)
		t.start()






if __name__ == "__main__":
	os.system("title " + my_title)
	print("========================> |POWEREDGE| <========================")
	EdgeBOT()

