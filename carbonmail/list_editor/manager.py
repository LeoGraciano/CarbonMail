def initialize(email_sender):
    from carbonmail.list_editor import ListEditor

    ems = ListEditor(email_sender)
    ems.enable_window()
