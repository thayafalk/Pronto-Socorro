from colorama import Fore
import time
import os
import heapq
from faker import Faker
import random
import csv

fake = Faker()


fila_prioridade = []  
pacientes_chamados = []  
pacientes_atendidos = []  
prioridades_usadas = set()

def gerar_prioridade_aleatoria():
    return random.randint(1, 10)  

def gerar_idade_aleatoria():
    return random.randint(1, 100)  

def gerar_nome_aleatorio():
    return fake.name()

def salvar_fila():
    with open('pacientes6.csv', 'w', newline='') as csvfile:
        fieldnames = ['Prioridade', 'Nome', 'Idade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for paciente in fila_prioridade:
            writer.writerow({'Prioridade': paciente[0], 'Nome': paciente[1], 'Idade': paciente[2]})

while True:
    print("BEM-VINDO AO PRONTO SOCORRO, selecione a opção desejada:")
    print(Fore.MAGENTA + "1. Cadastrar pacientes")
    print(Fore.RED + "2. Ver paciente que vai ser atendido")
    print(Fore.GREEN + "3. Mostrar fila de pacientes")
    print(Fore.CYAN + "4. Mostrar cinco últimos pacientes que já foram atendidos")
    print(Fore.YELLOW + "5. Mostrar todos os pacientes atendidos")
    print(Fore.WHITE + "6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        for _ in range(10):  
            prioridade = gerar_prioridade_aleatoria()
            nome = gerar_nome_aleatorio()
            idade = gerar_idade_aleatoria()
            paciente = (prioridade, nome, idade)
            heapq.heappush(fila_prioridade, paciente)
            salvar_fila()
            prioridades_usadas.clear()
        print("10 pacientes inseridos na fila de prioridade.")
        time.sleep(3)
        os.system('cls')

    elif opcao == '2':
        if fila_prioridade:
            paciente = heapq.heappop(fila_prioridade)
            pacientes_chamados.append(paciente)
            print(Fore.MAGENTA + "O paciente", paciente[1], "com prioridade", paciente[0], "acaba de ser atendido e não está mais na fila de prioridade")
            pacientes_atendidos.append(paciente)
            time.sleep(5)
            os.system('cls')
        else:
            print("A fila de prioridade do pronto socorro está vazia.")
            time.sleep(3)
            os.system('cls')

    elif opcao == '3':
        print(Fore.GREEN + "Fila de Prioridade:")
        for paciente in fila_prioridade:
            print(paciente)
        time.sleep(3)
        os.system('cls')


    elif opcao == '4':
        if pacientes_chamados:
            ultimos_pacientes = pacientes_chamados[-5:][::-1]
            print(Fore.BLACK + "5 últimos pacientes chamados:")
            for paciente in ultimos_pacientes:
                print("Nome:", paciente[1], "Prioridade:", paciente[0])
            time.sleep(5)
            os.system('cls')
        else:
            print("Nenhum paciente foi chamado ainda.")
            time.sleep(3)
            os.system('cls')

    elif opcao == '5':
        if pacientes_atendidos:
            print(Fore.CYAN + "Pacientes já atendidos:")
            for paciente in pacientes_atendidos:
                print("Nome:", paciente[1], "Prioridade:", paciente[0])
            time.sleep(5)
            os.system('cls')
        else:
            print("Nenhum paciente foi atendido ainda.")
            time.sleep(3)
            os.system('cls')

    elif opcao == '6':
        print("Encerrou o plantão do pronto socorro")
        break
