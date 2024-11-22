from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox
)

from modules import Users, create_connection
import payments_window
import bcrypt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Вход в приложение")
        self.setGeometry(200, 200, 300, 200)

        # Создаем элементы интерфейса
        self.user_label = QLabel("Имя пользователя")
        self.user_combobox = QComboBox()
        self.load_users()  # Заполнение выпадающего списка именами пользователей

        self.password_label = QLabel("Пароль")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Войти")
        self.exit_button = QPushButton("Выход")

        # Связываем кнопки с действиями
        self.login_button.clicked.connect(self.authenticate)
        self.exit_button.clicked.connect(self.close)

        # Располагаем элементы интерфейса
        layout = QVBoxLayout()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_combobox)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)

    def load_users(self):
        #Загружаем логины пользователей из базы данных
        session = create_connection()
        users = session.query(Users).all()
        self.user_combobox.addItems([user.login for user in users])

    def authenticate(self):
        #Обработка входа пользователя
        login = self.user_combobox.currentText()
        password = self.password_input.text()

        session = create_connection()
        user = session.query(Users).filter_by(login=login).first()

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            print("Введённый пароль:" + str(password.encode('utf-8')))
            print("Пароль в базе: " + str(user.password.encode('utf-8')))
            QMessageBox.information(self, "Успех", f"Добро пожаловать, {user.fio}!")
            self.open_payments_window(user.id)
            
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль!")


    def open_payments_window(self, user_id):
        self.payments_window = payments_window.PaymentsWindow(user_id)
        self.payments_window.show()
        self.close()
        
