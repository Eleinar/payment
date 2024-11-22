from PySide6.QtWidgets import (
    QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton,
    QWidget, QHBoxLayout, QLabel, QDateEdit, QComboBox, QMessageBox
)
from PySide6.QtCore import Qt, QDate

from modules import PaymentList, Categories, Users, create_connection

from add_payment_window import AddPaymentWindow
import generate_reports



class PaymentsWindow(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        self.setWindowTitle("Учёт платежей")
        self.setGeometry(100, 100, 800, 600)
        self.user_id = user_id
        self.db = create_connection()
        
        # Основной виджет и макет
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout(self.main_widget)
        
        # Верхняя панель управления
        self.control_layout = QHBoxLayout()
        self.layout.addLayout(self.control_layout)

        # Таблица
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(
            ["Наименование платежа", "Количество", "Цена", "Сумма", "Категория"]
        )
        self.layout.addWidget(self.table)

        # Кнопки управления
        self.add_button = QPushButton("+")
        self.delete_button = QPushButton("-")
        self.filter_label = QLabel("С:")
        self.from_date = QDateEdit()
        self.from_date.setCalendarPopup(True)
        self.from_date.setDate(QDate.currentDate())
        self.to_label = QLabel("по")
        self.to_date = QDateEdit()
        self.to_date.setCalendarPopup(True)
        self.to_date.setDate(QDate.currentDate())
        self.category_label = QLabel("Категория:")
        self.category_combobox = QComboBox()
        self.category_combobox.addItem("-")  # Добавим вариант "Все категории"
        self.load_categories()

        self.apply_filter_button = QPushButton("Выбрать")
        self.clear_filter_button = QPushButton("Очистить")
        self.report_button = QPushButton("Отчет")

        # Добавляем элементы на панель управления
        self.control_layout.addWidget(self.add_button)
        self.control_layout.addWidget(self.delete_button)
        self.control_layout.addWidget(self.filter_label)
        self.control_layout.addWidget(self.from_date)
        self.control_layout.addWidget(self.to_label)
        self.control_layout.addWidget(self.to_date)
        self.control_layout.addWidget(self.category_label)
        self.control_layout.addWidget(self.category_combobox)
        self.control_layout.addWidget(self.apply_filter_button)
        self.control_layout.addWidget(self.clear_filter_button)
        self.control_layout.addWidget(self.report_button)

        # Связываем кнопки с функциями
        self.add_button.clicked.connect(self.add_payment)
        self.delete_button.clicked.connect(self.delete_payment)
        self.apply_filter_button.clicked.connect(self.apply_filters)
        self.clear_filter_button.clicked.connect(self.clear_filters)
        self.report_button.clicked.connect(self.generate_report)

        # Загрузка данных
        self.load_payments()

    def load_categories(self):
        # Загрузка категорий в выпадающий список
        categories = self.db.query(Categories).all()
        for category in categories:
            self.category_combobox.addItem(category.category_name)

    def load_payments(self):
        # Загрузка платежей из базы данных
        
        payments = self.db.query(PaymentList).filter_by(user_id=self.user_id).all()

        self.table.setRowCount(0)  # Очищаем таблицу
        for payment in payments:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            # Заполняем данные о платеже
            self.table.setItem(row_position, 0, QTableWidgetItem(payment.pay_name))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(payment.pay_count)))
            self.table.setItem(row_position, 2, QTableWidgetItem(f"{payment.pay_cost:.2f} р"))

            # Вычисляем сумму
            total = payment.pay_count * payment.pay_cost
            self.table.setItem(row_position, 3, QTableWidgetItem(f"{total:.2f} р"))

            # Категория платежа
            self.table.setItem(row_position, 4, QTableWidgetItem(payment.category_rel.category_name))

    def add_payment(self):
        # Открывает окно для добавления нового платежа
        add_payment_window = AddPaymentWindow(self, self.user_id)
        if add_payment_window.exec():
            self.load_payments()  # Обновляем таблицу после добавления

    def delete_payment(self):
        # Удаляет выбранный платеж
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Ошибка", "Не выбран платеж для удаления")
            return

        # Подтверждение удаления
        reply = QMessageBox.question(
            self, "Подтверждение", "Вы уверены, что хотите удалить выбранный платеж?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            payment_name = self.table.item(selected_row, 0).text()
            payment = self.db.query(PaymentList).filter_by(pay_name=payment_name, user_id=self.user_id).first()
            if payment:
                self.db.delete(payment)
                self.db.commit()
                self.load_payments()
                QMessageBox.information(self, "Удалено", "Платеж успешно удален")

    def apply_filters(self):
        # Применяет фильтры для текущего пользователя.
        self.from_date = self.from_date.date().toPython()
        self.to_date = self.to_date.date().toPython()
        selected_category = self.category_combobox.currentText()

        db = create_connection()

        query = db.query(PaymentList).filter(
            PaymentList.user_id == self.user_id,  # Учитываем только платежи текущего пользователя
            PaymentList.pay_day >= self.from_date,
            PaymentList.pay_day <= self.to_date
        )

        if selected_category != "-":
            query = query.join(Categories).filter(Categories.category_name == selected_category)

        payments = query.all()

        self.table.setRowCount(0)
        for payment in payments:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)

            self.table.setItem(row_position, 0, QTableWidgetItem(payment.pay_name))
            self.table.setItem(row_position, 1, QTableWidgetItem(str(payment.pay_count)))
            self.table.setItem(row_position, 2, QTableWidgetItem(f"{payment.pay_cost:.2f} р."))
            total = payment.pay_count * payment.pay_cost
            self.table.setItem(row_position, 3, QTableWidgetItem(f"{total:.2f} р."))
            self.table.setItem(row_position, 4, QTableWidgetItem(payment.category_rel.category_name))


    def clear_filters(self):
        # Сбрасывает фильтры
        self.from_date.setDate(QDate.currentDate())
        self.to_date.setDate(QDate.currentDate())
        self.category_combobox.setCurrentIndex(0)
        self.load_payments()

    def generate_report(self):
        user = self.db.query(Users).filter(Users.id == self.user_id).first()
        generate_reports.generate_report(self, self.from_date, self.to_date, self.user_id, user.fio)


