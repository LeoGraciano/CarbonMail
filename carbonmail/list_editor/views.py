import PySimpleGUI as sg
from carbonmail.utils import inner_element_space


lista = ['Administradores', 'Alunos']


def get_layout():

    frame_list = [
        inner_element_space(600),
        [
            sg.Text('Selecione Lista'),
            sg.Combo(lista, default_value=lista[1], key='-List-')
        ],
        [
            sg.Text('Criar uma Lista'),
            sg.InputText(key='-ListName-'),
            sg.Button('Criar', key='-Create-', size=(10, 1))
        ],
        [
            sg.Button(
                'Deletar a Lista', key='-Delete-', size=(15, 1),
                # (Equerda e direita), (Cima e Baixo )
                pad=((5, 5), (7, 7))
            ),
            sg.Button(
                'Mostra Contatos', key='-Contacts-', size=(15, 1),
                # (Equerda e direita), (Cima e Baixo )
                pad=((5, 5), (7, 7))
            )
        ],
        inner_element_space(600),
    ]

    frame_import = [
        inner_element_space(600),
        [
            sg.Text(
                'Selecione o arquivo (CSV):',
                tooltip="Cabeçalho: name e email"
            ),
            sg.InputText(
                key='-CSV-'
            ),
            sg.FileBrowse(
                'Selecionar', file_types=(
                    ("CSV", '*.csv'),), tooltip="Cabeçalho: name e email"
            )
        ],
        [
            sg.Button(
                'Importa Contatos', key='-Import-', size=(15, 1),
                pad=((0, 0), (7, 7))  # (Equerda e direita), (Cima e Baixo )
            ),

        ],
        inner_element_space(600),
    ]

    frame_add = [
        inner_element_space(600),
        [
            sg.Text('Insira o nome:'),
            sg.InputText(key='-Name-')
        ],
        [
            sg.Text('Insira o Email:'),
            sg.InputText(key='-Email-')
        ],
        [
            sg.Button(
                'Adicionar Contato', key='-Add-',
                size=(15, 1),
                pad=(0, (7, 7))
            ),
        ],
        inner_element_space(600),
    ]
    layout = [
        [
            sg.Frame(
                'Configurações da Lista', frame_list,
                element_justification='c'
            )
        ],
        [
            sg.Frame(
                'Importar Contatos', frame_import,
                element_justification='c',

            )
        ],
        [
            sg.Frame(
                'Adicionar Contatos', frame_add,
                element_justification='c'
            )
        ],
        [
            sg.Button(
                'Voltar', key='-Back-',
                size=(15, 1),
                pad=(0, (7, 7))
            )
        ],
        inner_element_space(600),
    ]
    return layout


def get_window():
    sg.theme('DarkBlue14')
    return sg.Window(
        'Editor de lista', get_layout(), element_justification='c'
    )
