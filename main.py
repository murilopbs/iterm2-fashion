import sys
from PyQt6.QtWidgets import QApplication
from src.trayIcon import TrayIcon

if __name__ == '__main__':
    # cria o app 
    app = QApplication(sys.argv)
    
    # instancia a classe trayIcon
    trayIcon = TrayIcon(app)
#    trayIcon.show()
    
    # Fica no loop
    sys.exit(app.exec())
