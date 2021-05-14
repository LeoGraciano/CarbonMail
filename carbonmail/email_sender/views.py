import PySimpleGUI as sg

lista = ['Administradores', 'Alunos']


def get_layout():
    layout = [
        [
            sg.Text('Selecione o Seus Código'),
            sg.InputText(),
            sg.FileBrowse(
                'Selecione',
                file_types=(
                    (
                        'Códigos Python', '*.py'
                    ),  # Lista não funciona apenas tupla
                )
            )
        ],
        [
            sg.Text('Selecione a Lista de destinatário'),
            sg.Combo(lista, default_value=lista[1])
        ],
        [
            sg.Text('Insira o Título'),
            sg.InputText(key='-Title-')
        ],
        [
            sg.Text('Insira o Conteudo do Email'),
            sg.MLine(key='-Content-')
        ],
        [
            sg.Button('Enviar', key='-Send-'),
            sg.Button('Gerenciar Lista', key='-ListEditor-')

        ]
    ],

    return layout


def get_window():
    sg.theme('DarkBlue14')
    return sg.Window('Enviar Email', get_layout())
