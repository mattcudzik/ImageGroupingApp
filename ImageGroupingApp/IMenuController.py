from PyQt5.QtWidgets import QWidget


class IMenuController(QWidget):
    def __init__(self, mainController):
        super(QWidget, self).__init__()
        self.mainController = mainController


