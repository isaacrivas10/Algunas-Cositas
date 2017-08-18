import random
import os,sys
from time import sleep

menu_dict = {}
outcomes = ['piedra', 'papel', 'tijera']

def MainMenu():
	os.system('cls')
	print ('\n')
	print (' ¡Bienvenido a piedra, papel, o tijera! ')
	print ('\n')
	print (' [1] Nuevo juego')
	print (' [9] Salir')
	print (' \n')
	choice = input(' >>> ')
	SelectedOpt(choice)

def PaperRockScissor(ans,cpu):
	if ans == 'Piedra' or ans == 'piedra' or ans == 'Tijera' or ans == 'tijera' or ans == 'Papel' or ans == 'papel':
		if ans == 'Piedra' or ans == 'piedra' and cpu == 'tijera':
			print (' ¡Haz ganado! =)')
		elif ans == 'Piedra' or ans == 'piedra' and cpu == 'papel':
			print (' ¡Haz perdido¡ =(')
		elif ans == 'Piedra' or ans == 'piedra' and cpu == 'piedra':
			print (' ¡Es un empate! ')
		if ans == 'Tijera' or ans == 'tijera'  and cpu == 'papel':
			print (' ¡Haz ganado! =)')
		elif ans == 'Tijera' or ans == 'tijera' and cpu == 'piedra':
			print (' ¡Haz perdido¡ =(')
		elif ans == 'Tijera' or ans == 'tijera' and cpu == 'tijera':
			print (' ¡Es un empate! ')
		if ans == 'Papel' or ans == 'papel' and cpu == 'piedra':
			print (' ¡Haz ganado! =)')
		elif ans == 'Papel' or ans == 'papel' and cpu == 'tijera':
			print (' ¡Haz perdido¡ =(')
		elif ans == 'Papel' or ans == 'papel' and cpu == 'papel':
			print (' ¡Es un empate! ')
	else:
		print ( '¡Eh! No te pases de listo >:|')
		
def SelectedOpt(choice):
	ch = choice.lower()
	if ch == '':
		menu_dict['MainMenu']()
	elif ch == '9':
		sys.exit()
	elif ch != '':
		try:
			menu_dict[ch]()
		except Exception:
			print (' Opcion no valida')
			sleep(2)
			menu_dict['MainMenu']()

def NewGame():
	os.system('cls')
	print ('\n')
	print ( ' Muy bien, ¡un nuevo juego!')
	print ( ' Vamos a comenzar \n')
	sleep(1)
	ans = input(' ¿Piedra, Papel o tijera? >> ')
	cpu = random.choice(outcomes)
	sleep(1)
	print (' CPU: '+cpu)
	PaperRockScissor(ans,cpu)
	sleep(1)
	
	aksAgain = input(' Deseas seguir jugando?:  Y/N ')
	if askAgain == 'Y' or askAgain == 'y':
		NewGame()
	else:
		#menu_dict['MainMenu']()
		pass
		
		
menu_dict = {
'MainMenu' : MainMenu,
'1': NewGame
}


MainMenu()
"""
if  __name__ == '__main__':
	MainMenu()"""