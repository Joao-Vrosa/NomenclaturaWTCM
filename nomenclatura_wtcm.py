from time import sleep
from colorama import Fore, Back, Style

print(Fore.CYAN + "-" * 35)
print(Fore.CYAN + "Bem-vindo ao gerador de OUTBOX WTCM")
print(Fore.CYAN + "-" * 35)

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sleep(1)

opcao = 0
while opcao != 2: # Inicio MENU
    print(Fore.YELLOW + "\n      --- MENU ---")
    print(Fore.GREEN + "Selecione uma das opções:\n[ 1 ] Gerar OUTBOX\n[ 2 ] Sair do programa\n")
    opcao = int(input(Fore.GREEN + "Digite a opção desejada: "))
    
    if opcao == 1: # Opções MENU
        separarSTR = []
        acumuladorP = []
        parceiraFinal = ""
        
        num = int(input(Fore.BLUE + "\nDigite o número, seguindo a ordem: "))
        parceira = str(input(Fore.BLUE + "Digite a parceira: ")).upper()
        conta = int(input(Fore.BLUE + "Digite o número da conta: "))
        # Fim MENU
                    
        sleep(1)
            
        for i in range(len(parceira)):
            separarSTR.append(parceira[i])

            if separarSTR[i] in letras:
                acumuladorP.append(separarSTR[i])
                
                parceiraFinal = "".join(acumuladorP)
                
        if separarSTR[i] not in letras:
            print(Fore.YELLOW + "\n[ALERT] O campo 'Parceira' deve conter apenas letras!")
            print(Fore.YELLOW + "        --- Digitos invalidos removidos! ---")

            
        print(Fore.GREEN + "\n    --- COPIE A OUTBOX ---")
        print(Fore.RESET + "outbox" + str(num) + "=" + str(parceiraFinal) + "@F:\cash\\" + str(conta) + ".CSH")
        print(Fore.GREEN + "    ----------------------")
            
    elif opcao != 2:
        print(Fore.RED + "\n[ERRO] Opção invalida, tente novamenete!")
    
    sleep(3)
    
print(Fore.RED + "\nSaindo do programa...")
sleep(3)

