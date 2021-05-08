from carbonmail.email_sender import views


import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED


def enable_window():
    window = views.get_window()

    while True:
        event, values = window.read()

        if event == WIN_CLOSED:
            window.close()
            break


enable_window()
