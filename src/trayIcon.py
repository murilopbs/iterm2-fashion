# src/trayIcon.py

from PyQt6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu, QLabel, QStyle, QWidgetAction
from PyQt6.QtGui import QIcon, QAction, QPixmap
from . import change_image
import threading
import os
from src.photo_util import PhotoUtil
from PyQt6.QtCore import Qt

class TrayIcon(QMainWindow):
    def __init__(self, app):
        super().__init__()
        
        self.photoUtil = PhotoUtil()
        self.app = app
        self._create_tray_icon()
        self._create_menu()

    def _create_tray_icon(self):
        icon = QIcon.fromTheme("document-new") 
        self.tray_icon = QSystemTrayIcon(icon, self.app)
    
    def _create_menu(self):
        self.menu = QMenu()

        
        self.create_image_pix_map()
        self.apply_background_action = QAction("Aplicar este fundo", self)
        self.apply_background_action.triggered.connect(self._set_background_image_threaded)
        self.menu.addAction(self.apply_background_action)
        
        self.menu.addSeparator()

        self.configurationMenu = QAction("Mudar imagem")
        self.configurationMenu.triggered.connect(self._set_background_image_threaded)
        self.menu.addAction(self.configurationMenu)
        
        self.closeMenu = QAction("Fechar")
        self.closeMenu.triggered.connect(self.app.quit) 
        self.menu.addAction(self.closeMenu)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()

    def _set_background_image_threaded(self):
        thread = threading.Thread(target=change_image.main)
        thread.start()

    def create_image_pix_map(self):
        pixmap = QPixmap(self.photoUtil.get_first_image())
        if not pixmap.isNull():
            pixmap = pixmap.scaledToWidth(150, Qt.TransformationMode.SmoothTransformation)
            photo_preview_label = QLabel()
            photo_preview_label.setPixmap(pixmap)
            photo_preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 

            photo_preview_action = QWidgetAction(self)
            photo_preview_action.setDefaultWidget(photo_preview_label)

            self.menu.addAction(photo_preview_action)
