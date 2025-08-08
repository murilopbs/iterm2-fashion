from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon, QAction
import sys

app = QApplication(sys.argv)

# Cria o ícone que aparecerá na barra de menus
icon = QIcon.fromTheme("document-new")
tray_icon = QSystemTrayIcon(QIcon(icon), app)

menu = QMenu()

configurations = QAction("Configurações")
menu.addAction(configurations)
quit_action = QAction("Sair")
quit_action.triggered.connect(app.exit)
menu.addAction(quit_action)


# Garante que o ícone seja visível
tray_icon.setContextMenu(menu)
tray_icon.show()

sys.exit(app.exec())
