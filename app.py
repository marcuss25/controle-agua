import os
from colorama import Fore, Style

os.system('cls' if os.name == 'nt' else 'clear')

# functions
def level_color(nivel):
    match(nivel):
        case 'Nivel 1':
            print(Fore.RED, 'Muito baixo(critico)', Style.RESET_ALL)
        case 'Nivel 2':
            print(Fore.YELLOW, 'Baixo', Style.RESET_ALL)
        case 'Nivel 3':
            print(Fore.GREEN, 'Medio', Style.RESET_ALL)
        case 'Nivel 4':
            print(Fore.CYAN, 'Alto', Style.RESET_ALL)
        case 'Nivel 5':
            print(Fore.BLUE, 'Muito alto(alerta)', Style.RESET_ALL)

# codigo principal
nivel = ['Nivel 1', 'Nivel 2', 'Nivel 3', 'Nivel 4', 'Nivel 5']

choice = nivel[3] # recebe o item da lista

# printa o nivel e a cor
print(f'{choice}: ')
level_color(choice)