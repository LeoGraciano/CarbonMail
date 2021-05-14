def initialize():
    from carbonmail.email_sender import EmailSender

    ems = EmailSender()
    ems.enable_window()
