from PyQt5.QtWidgets import QWidget, QStyle, QMenu, QAction

class FileMenu(QMenu):
    def __init__(self, parent: QWidget) -> None:
        super().__init__('&File', parent)

        self.open_folder_to_save_action = QAction(self.style().standardIcon(QStyle.SP_DirOpenIcon), '&Open folder to Save', self)
        self.open_folder_to_save_action.setShortcut('Ctrl+O')
        self.addAction(self.open_folder_to_save_action)
        self.addSeparator()
        self.import_authors_action = QAction(self.style().standardIcon(QStyle.SP_ArrowDown), '&Import tags', self)
        self.import_authors_action.setShortcut('Ctrl+W')
        self.addAction(self.import_authors_action)
        self.export_authors_action = QAction(self.style().standardIcon(QStyle.SP_ArrowUp), '&Export tags', self)
        self.export_authors_action.setShortcut('Ctrl+S')
        self.addAction(self.export_authors_action)
        self.addSeparator()
        self.exit_action = QAction(self.style().standardIcon(QStyle.SP_TitleBarCloseButton), "&Exit", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)
        self.addAction(self.exit_action)

class TagsMenu(QMenu):
    def __init__(self, parent: QWidget) -> None:
        super().__init__('&Tags', parent)

        self.add_hentai_action = QAction(self.style().standardIcon(QStyle.SP_FileDialogNewFolder), '&Add tag', self)
        self.add_hentai_action.setShortcut('+')
        self.addAction(self.add_hentai_action)
        self.addSeparator()
        self.select_all_action = QAction(self.style().standardIcon(QStyle.SP_DialogApplyButton), '&Select all', self)
        self.select_all_action.setShortcut('Ctrl+A')
        self.addAction(self.select_all_action)
        self.deselect_all_action = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton), '&Deselect all', self)
        self.deselect_all_action.setShortcut('Ctrl+D')
        self.addAction(self.deselect_all_action)
        self.addSeparator()
        self.delete_action = QAction(self.style().standardIcon(QStyle.SP_BrowserStop), '&Remove selected tags', self)
        self.delete_action.setShortcut('-')
        self.addAction(self.delete_action)

class StartMenu(QMenu):
    def __init__(self, parent: QWidget) -> None:
        super().__init__('&Start', parent)

        self.start_process = QAction(self.style().standardIcon(QStyle.SP_MediaPlay), '&Start!', self)
        self.start_process.setShortcut('F1')
        self.addAction(self.start_process)
        self.api_key_action = QAction(self.style().standardIcon(QStyle.SP_FileDialogDetailedView), '&Enter API Key', self)
        self.api_key_action.setShortcut('Ctrl+K')
        self.addAction(self.api_key_action)

class HelpMenu(QMenu):
    def __init__(self, parent: QWidget) -> None:
        super().__init__('&Help', parent)

        self.info_action = QAction(self.style().standardIcon(QStyle.SP_FileDialogInfoView), '&Info', self)
        self.info_action.setShortcut('Ctrl+I')
        self.addAction(self.info_action)