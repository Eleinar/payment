from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox, QPushButton, QMessageBox
)

from modules import PaymentList, Categories, create_connection
from datetime import datetime

class AddPaymentWindow(QDialog):
    def __init__(self, parent, user_id):
        super().__init__(parent)
        self.setWindowTitle("Добавить платеж")
        self.setGeometry(200, 200, 400, 300)

        self.user_id = user_id
        self.layout = QVBoxLayout(self)

        # Поля ввода
        self.name_label = QLabel("Наименование:")
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)

        self.count_label = QLabel("Количество:")
        self.count_input = QSpinBox()
        self.count_input.setRange(1, 1000000)
        self.layout.addWidget(self.count_label)
        self.layout.addWidget(self.count_input)

        self.cost_label = QLabel("Цена за единицу:")
        self.cost_input = QDoubleSpinBox()
        self.cost_input.setRange(0.01, 1000000.00)
        self.cost_input.setDecimals(2)
        self.layout.addWidget(self.cost_label)
        self.layout.addWidget(self.cost_input)

        self.category_label = QLabel("Категория:")
        self.category_combobox = QComboBox()
        self.layout.addWidget(self.category_label)
        self.layout.addWidget(self.category_combobox)
        self.load_categories()

        # Кнопки
        self.add_button = QPushButton("Добавить")
        self.cancel_button = QPushButton("Отмена")
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.cancel_button)

        # Привязываем кнопки к действиям
        self.add_button.clicked.connect(self.add_payment)
        self.cancel_button.clicked.connect(self.reject)

    def load_categories(self):
        # Загрузка категорий в выпадающий списокpay_
        db = create_connection()
        categories = db.query(Categories).all()
        for category in categories:
            self.category_combobox.addItem(category.category_name)

    def add_payment(self):
        # Добавление платежа в базу данных
        name = self.name_input.text().strip()
        count = self.count_input.value()
        cost = self.cost_input.value()
        category_name = self.category_combobox.currentText()

        if not name or category_name == "":
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля!")
            return
        
        if len(name) < 3:
            QMessageBox.warning(self, "Ошибка", "Название должно быть длиннее трёх символов")
            return

        db = create_connection()
        category = db.query(Categories).filter_by(category_name=category_name).first()

        if not category:
            QMessageBox.warning(self, "Ошибка", "Выбранная категория не найдена!")
            return

        # Создаём запись
        new_payment = PaymentList(
            pay_name=name,
            pay_count=count,
            pay_cost=cost,
            pay_day=datetime.today().strftime('%Y-%m-%d'),
            user_id=self.user_id,
            category_id=category.id
        )

        db.add(new_payment)
        db.commit()
        QMessageBox.information(self, "Успешно", "Платеж добавлен!")
        self.accept()
