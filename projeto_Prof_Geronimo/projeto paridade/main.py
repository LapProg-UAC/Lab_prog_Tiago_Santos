import datetime as dt
import random as r
import os

# Global variables to store the numbers and their parity
parity_file = 'projeto_Prof_Geronimo/projeto paridade/parity.txt'
numbers_file = 'projeto_Prof_Geronimo/projeto paridade/numbers.txt'

random_seed = dt.datetime.now().microsecond
r.seed(random_seed)

def generate_files() -> None:
    """
    creat two files, one with random numbers and another with their parity (0 for even and 1 for odd).
    If the files already exist, they will be deleted and recreated with new random numbers and their parity.
    param:
        None
    return:
        None
    """
    if os.path.exists(parity_file):
        os.remove(parity_file)
    if os.path.exists(numbers_file):
        os.remove(numbers_file)
    listnum.clear()
    listparity.clear()
    for i in range(r.randint(50,65)):
        listnum.append(r.randint(0,128))
    print(listnum)
    for i in listnum:
        listparity.append(int(i)%2)
    print(listparity)
    with open(parity_file,'w') as file:
        for i in listparity:
            file.write(str(i)+'\n')
    print('Arquivo criado com sucesso!')
    with open(numbers_file,'w') as file:
        for i in listnum:
            file.write(str(i)+'\n')
    print('Arquivo criado com sucesso!')
    return None

def setup() -> None:
    global listnum, listparity
    listnum = []
    listparity = []

    """
    Setup function that checks if the files parity_file and 'numbers.txt' exist. If they do, it reads the contents of the files and stores them in the lists 'listparity' and 'listnum', respectively. If the files do not exist, it calls the 'generate_files()' function to create them.
    param:
        None
    return:
        None
    """
    if os.path.exists(parity_file) and os.path.exists(numbers_file):
        with open(parity_file,'r') as file:
            listparity = file.read().strip().split('\n')
            listparity = [int(i) for i in listparity]
        with open(numbers_file,'r') as file:
            listnum = file.read().strip().split('\n')
            listnum = [int(i) for i in listnum]
        print(listparity)
        print(listnum)
    else:
        generate_files()
    return None

def main() -> bool:
    """
    Main function of the program, responsible for displaying the menu and handling user input.
    It allows the user to read the files, generate new files, check the parity of the numbers, or exit the program.
    param:
        None
    return:
        bool: Returns False if the user chooses to exit the program, otherwise returns True.
    """
    global listnum, listparity
    print("1- Ler arquivos\n2- Gerar novos arquivos\n3 - Verificar paridade\n4 - Sair")
    option = int(input("Digite a opção desejada: "))
    if option == 1:
        with open(parity_file,'r') as file:
            listparity = file.read().strip().split('\n')
        with open(numbers_file,'r') as file:
            listnum = file.read().strip().split('\n')
        print(listparity)
        print(listnum)
    elif option == 2:
        generate_files()
    elif option == 3:
        with open(parity_file,'r') as file:
            listparity = file.read().strip().split('\n')
            listparity = [int(i) for i in listparity]
        with open(numbers_file,'r') as file:
            listnum = file.read().strip().split('\n')
            listnum = [int(i) for i in listnum]
        for i in range(len(listnum)):
            if int(listnum[i]) % 2 != listparity[i]:
                print(f'O número {listnum[i]} está com paridade incorreta.')
        print('Verificação de paridade concluída!')
    elif option == 4:        
        print('Saindo do programa...')
        return False
    else:
        print('Opção inválida!')
    return True

setup()
while True:
    if not main():
        break