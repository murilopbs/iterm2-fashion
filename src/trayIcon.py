# src/trayIcon.py

from PyQt6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from . import change_image
import threading

class TrayIcon(QMainWindow):
    def __init__(self, app):
        super().__init__()
        
        self.app = app
        self._create_tray_icon()
        self._create_menu()

    def _create_tray_icon(self):
        icon = QIcon.fromTheme("document-new") 
        self.tray_icon = QSystemTrayIcon(icon, self.app)
    
    def _create_menu(self):
        self.menu = QMenu()
        
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
