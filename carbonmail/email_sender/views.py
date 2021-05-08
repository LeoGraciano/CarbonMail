import PySimpleGUI as sg


def get_layout():
    layout = [
        [sg.Text('Eu sou um Texto')],
        [sg.Text('Eu sou um Texto'), sg.Button('Eu sou um Botão')],
    ]
    return layout


def get_window():
    return sg.Window('Teste de Janela', get_layout())
