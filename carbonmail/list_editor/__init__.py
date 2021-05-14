import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.list_editor import views


class ListEditor:
    def __init__(self, email_sender):
        self.window = None
        self.ems = email_sender

    def instantiate(self):
        if self.window is None:
            self.window = views.get_window()

    def enable_window(self):
        self.instantiate()

        while True:
            event, values = self.window.read()

            if event == WIN_CLOSED:
                self.window.close()
                self.ems.unhidden_window()
                break

            if event == '-Send-':
                title = values['-Title-']
                content = values['-Content-']

                sg.popup(
                    f'O titulo é: {title}\nO Conteudo é : {content}', title='E-mail'
                )

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
