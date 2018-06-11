import ctypes


class Alert:

    # module for raising alert notification

    def __init__(self):
        logging.getLogger().setLevel(logging.DEBUG)

    def Mbox(title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    



