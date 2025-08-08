from PyQt6.QtWidgets import QMainWindow, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import QCoreApplication


class TrayIcon(QMainWindow):
    def __init__(self, app):
        super().__init__()
        
        self.app = app

        icon = QIcon.fromTheme("document-new")
        self.tray_icon = QSystemTrayIcon(QIcon(icon), self.app)

        self.menu = QMenu()
        self.configurationMenu = QAction("Configuração")
        self.menu.addAction(self.configurationMenu)
        self.closeMenu = QAction("Fechar")
        self.closeMenu.triggered.connect(self.app.exit)
        self.menu.addAction(self.closeMenu)

        self.tray_icon.setContextMenu(self.menu)
        self.tray_icon.show()

