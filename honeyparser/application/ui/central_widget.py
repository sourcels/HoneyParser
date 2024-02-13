import os, sys, shutil, json, pickle
from typing import Optional, Dict, List

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyle, QStackedWidget, QListWidget, QVBoxLayout, QHBoxLayout, QListWidgetItem, QLabel, QAbstractItemView, QMenuBar, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap, QColor
from PyQt5.QtCore import Qt, QUrl, QSize

class CentralWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setObjectName("central_widget")

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout(self)

        self.list_widget = QListWidget()
        self.list_widget.setIconSize(QSize(60, 60))
        self.list_widget.setMinimumWidth(76)
        self.list_widget.setMaximumWidth(76)
        self.list_widget.itemDoubleClicked.connect(self.on_item_click)
        self.list_widget.setSelectionMode(QAbstractItemView.NoSelection)
        self.list_widget.setStyleSheet("background-color: transparent; border: none;")

        icons = ['honeyparser/assets/hentaikage.png']
        icon_size = QSize(60, 60)
        for icon_path in icons:
            pixmap = QPixmap(icon_path).scaled(icon_size, aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation)
            icon = QIcon(pixmap)
            item = QListWidgetItem(icon, "", self.list_widget)
            self.list_widget.addItem(item)

        # Создаем виджет со страницами
        self.pages_widget = QStackedWidget()

        # Создаем страницы
        page1 = QWidget()
        label1 = QLabel('Страница 1')
        layout1 = QVBoxLayout(page1)
        layout1.addWidget(label1)


        # Добавляем страницы в виджет со страницами
        self.pages_widget.addWidget(page1)

        # Добавляем список и виджет со страницами в главное окно
        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.pages_widget)

        self.setLayout(main_layout)

    def on_item_click(self, item: QListWidgetItem):
        index = self.list_widget.row(item)
        self.pages_widget.setCurrentIndex(index)
