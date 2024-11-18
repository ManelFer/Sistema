from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login do sistema")
        self.btn_login.clicked.connect(self.open_system)

    def open_system(self):
        if self.txt_password.text() == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('Senha inválida')


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")

        #******************PAGINAS DO SISTEMA******************
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_tables.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_table))
        self.btn_contato.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contato))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))

        self.btn_cadastrar.clicked.connect(self.subscribe_user)

    def subscribe_user(self):
        if self.txt_senha.text() != self.txt_senha_2.text():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.warning)
            msg.setWindowTitle("Senhas diferentes")
            msg.setText("Senha diferentes!!!")
            msg.exec_()
            return None
        nome = self.txt_nome.text()
        user = self.txt_usuario.text()
        password = self.txt_senha.text()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()