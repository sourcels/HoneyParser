from PyQt5.QtWidgets import QWidget, QMenuBar

from application.ui.menu import FileMenu, TagsMenu, StartMenu, HelpMenu

class MenuBar(QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__()

        file_menu = FileMenu(self)
        self.addMenu(file_menu)

        tags_menu = TagsMenu(self)
        self.addMenu(tags_menu)
        
        go_menu = StartMenu(self)
        self.addMenu(go_menu)

        help_menu = HelpMenu(self)
        self.addMenu(help_menu)
