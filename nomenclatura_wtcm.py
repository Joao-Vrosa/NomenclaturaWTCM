from time import sleep

print("\033[0;34m-\033[0;0m" * 35)
print("\033[0;34mBem-vindo ao gerador de OUTBOX WTCM\033[0;0m")
print("\033[0;34m-\033[0;0m" * 35)

separarSTR = []
acumuladorP = []
parceiraFinal = ""
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

sleep(1)

opcao = 0
while opcao != 2: # Inicio MENU
    print("\033[1;33m \n      --- MENU ---\033[0;0m")
    print("\033[0;32mSelecione uma das opções:\n[ 1 ] Gerar OUTBOX\n[ 2 ] Sair do programa\n\033[0;0m")
    opcao = int(input("\033[0;36mDigite a opção desejada: \033[0;0m"))
    
    if opcao == 1: # Opções MENU
        num = int(input("\033[0;32m\nDigite o número, seguindo a ordem: \033[0;0m"))
        parceira = str(input("\033[0;32mDigite a parceira: \033[0;0m")).upper()
        conta = int(input("\033[0;32mDigite o número da conta: \033[0;0m"))
        # Fim MENU
                    
        sleep(1)
            
        for i in range(len(parceira)):
            separarSTR.append(parceira[i])

            if separarSTR[i] in letras:
                acumuladorP.append(separarSTR[i])
                
                parceiraFinal = "".join(acumuladorP)
                
                '''
                print("\n[ERRO] O campo 'Parceira' deve conter apenas letras, tente novamente!")
                print("--- Digitos invalidos removidos! ---")'''

            
        print("\033[1;32m\n    --- COPIE A OUTBOX ---\033[0;0m")
        print("outbox" + str(num) + "=" + str(parceiraFinal) + "@F:\cash\\" + str(conta) + ".CSH")
        print("\033[1;32m    ----------------------\033[0;0m")
            
    elif opcao != 2:
        print("\033[1;31m\n[ERRO] Opção invalida, tente novamenete!\033[0;0m")
    
    sleep(3)
    
print("\033[0;31m\nSaindo do programa...\033[0;0m")
sleep(3)

