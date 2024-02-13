from PyQt5.QtWidgets import QMainWindow

from application.ui.menu_bar import MenuBar
from application.ui.central_widget import CentralWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.central_widget = CentralWidget(self)
        self.setCentralWidget(self.central_widget)