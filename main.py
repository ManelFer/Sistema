from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QMessageBox)
from ui_login import Ui_Login
from ui_main import Ui_MainWindow
import sys
from database import DataBase

class Login(QWidget, Ui_Login):
    def __init__(self) -> None:
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle("Login do sistema")
        self.btn_login.clicked.connect(self.checkLogin, self.open_system)

    def open_system(self):
        if self.txt_password.text() == '123':
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('Senha inválida')

    # check de usuario no banco
    def checkLogin(self):
        self.users = DataBase()
        self.users.conecta()
        autenticado = self.users.check_user(self.txt_login.text().upper(), self.txt_password.text())
        if autenticado.lower == "administrador" or autenticado == "user":
            self.w = MainWindow(self.txt_login.text(), autenticado.lower())
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \n Tentativas: {self.tentativas +1} de 3')
                msg.exec_()
                self.tentativas +=1
            if self.tentativas == 3:
                #bloquear usuário
                self.users.close_connection()
                sys.exit(0)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, username, user):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de gerenciamento")

        self.user = username
        if user.lower() == "user":
            self.btn_pg_cadastro.setVisible(False)

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
        access = self.cb_perfil.currentText()

        db = DataBase()
        db.conecta()
        db.insert_user(nome, user, password, access)
        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.information)
        msg.setWindowTitle("Cadastro de usuário")
        msg.setText("Cadastro realizado com sucesso!!!")
        msg.exec_()

        self.txt_nome.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()