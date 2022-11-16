import PySimpleGUI as sg


def tela_inicio():
    sg.theme('Reddit')
    layout = [
        [sg.Text(">" * 30)],
        [sg.Text("Bem-vindo ao gerador de OutBox WTCM")],
        [sg.Text("<" * 30)],
        [sg.Button("Menu"), sg.Button("Sair")],
        
        
    ]
    return sg.Window("Nomenclatura WTCM", layout=layout, finalize=True)


def tela_dadosOutbox():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Digite os dados da sua OutBox: \n\n", pad=(190, 0))],
        [sg.Text("Digite o número, seguindo a ordem: ")],
        [sg.Input(key='ordem')],
        [sg.Text("Selecione a parceira: ")],
        [sg.Input(key='parceira')],
        [sg.Text("Digite o número da conta: ")],
        [sg.Input(key='conta')],
        [sg.Button("Gerar OutBox"), sg.Button("Sair")],
        
    ]
    return sg.Window("Nomenclatura WTCM", layout=layout, finalize=True)


def tela_outboxGerada():
    sg.theme('Reddit')
    layout = [
        [sg.Text("--- COPIE A OUTBOX ---\n", pad=(190, 0))],
        [sg.Output("Olá")],
        [sg.Button("Gerar OutBox"), sg.Button("Sair")],
        
    ]
    return sg.Window("Nomenclatura WTCM", layout=layout, finalize=True)


janela1, janela2, janela3 = tela_inicio(), None, None

while True:
    window, event, value = sg.read_all_windows()
    
    if window == janela1 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    if window == janela2 and event == sg.WIN_CLOSED or event == 'Sair':
        break
    if window == janela1 and event == 'Menu':
        janela2 = tela_dadosOutbox()
        janela1.hide()
    if window == janela2 and event == 'Gerar OutBox':
        janela2.hide()
        janela3 = tela_outboxGerada()

