import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.email_sender import views
from carbonmail.list_editor.manager import initialize as init_list_editor


class EmailSender:
    def __init__(self):
        self.window = None

    def instantiate(self):
        if self.window is None:
            self.window = views.get_window()

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if event == WIN_CLOSED:
                self.window.close()
                break

            if event == '-Send-':
                title = values['-Title-']
                content = values['-Content-']

                sg.popup(
                    f'O titulo é: {title}\nO Conteudo é : {content}', title='E-mail'
                )
            if event == '-ListEditor-':
                self.hide_window()
                init_list_editor(self)

    def close_window(self):
        if self.window is not None:
            self.window.close()
        self.window = None

    def hide_window(self):
        if self.window is not None:
            self.window.Hide()

    def unhidden_window(self):
        if self.window is not None:
            self.window.UnHide()
