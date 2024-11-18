from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from ui_login import Ui_Login
import sys

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do sistema")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()