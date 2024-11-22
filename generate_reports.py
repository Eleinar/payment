from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from PySide6.QtWidgets import QFileDialog, QMessageBox

from modules import PaymentList, create_connection

font_path = "DejaVuSans.ttf"

def generate_report(self, start_date, end_date, user_id, user_name):
    db = create_connection()

    start_date = start_date.date().toPython()
    end_date = end_date.date().toPython()
    
    # Получение платежей, фильтрация и сортировка
    payments = db.query(PaymentList).filter(
        PaymentList.pay_day >= start_date,
        PaymentList.pay_day <= end_date,
        PaymentList.user_id == user_id
    ).order_by(PaymentList.category_id, PaymentList.pay_day).all()

    if not payments:
        QMessageBox.warning(self, "Нет данных", "Нет платежей за выбранный период!")
        return

    # Создание файла PDF
    file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить отчёт", "", "PDF Files (*.pdf)")
    if not file_name:
        return

    c = canvas.Canvas(file_name, pagesize=A4)
    width, height = A4

    pdfmetrics.registerFont(TTFont('DejaVuSans', font_path))
    
    # Настройки шрифта
    c.setFont("DejaVuSans", 10)

    # Функция для вывода заголовков
    def draw_header(page_number):
        c.setFont("DejaVuSans", 12)
        c.drawString(50, height - 30, f"Отчёт по платежам ({user_name}) с {start_date} по {end_date}")
        c.setFont("DejaVuSans", 10)
        c.drawString(50, height - 50, f"Страница {page_number}")
        c.setFont("DejaVuSans", 10)
        c.drawString(20, height - 80, "№")
        c.drawString(80, height - 80, "Название")
        c.drawString(200, height - 80, "Количество")
        c.drawString(300, height - 80, "Цена")
        c.drawString(400, height - 80, "Итоговая сумма")
        c.drawString(500, height - 80, "Дата")

    # Начальные настройки
    y_position = height - 100
    page_number = 1
    draw_header(page_number)

    # Группировка платежей по категориям
    current_category = None
    total_sum = 0
    idx = 0

    for payment in payments:
        # Если категория изменилась, добавить её название
        if payment.category_rel.category_name != current_category:
            current_category = payment.category_rel.category_name
            y_position -= 20
            c.setFont("DejaVuSans", 12)
            c.drawString(20, y_position, f"Категория: {current_category}")
            c.setFont("DejaVuSans", 10)

        y_position -= 20
        idx += 1

        # Проверка, достаточно ли места на странице
        if y_position < 50:
            c.showPage()
            page_number += 1
            y_position = height - 100
            draw_header(page_number)

        # Добавление строки данных
        c.drawString(20, y_position, str(idx))
        c.drawString(80, y_position, payment.pay_name)
        c.drawString(200, y_position, str(payment.pay_count))
        c.drawString(300, y_position, f"{payment.pay_cost:.2f}")
        total = payment.pay_count * payment.pay_cost
        c.drawString(400, y_position, f"{total:.2f}")
        c.drawString(500, y_position, payment.pay_day.strftime('%d-%m-%Y'))
        total_sum += total

    # Итоговая сумма
    y_position -= 20
    if y_position < 50:  # Если места недостаточно, перейти на новую страницу
        c.showPage()
        page_number += 1
        y_position = height - 100
        draw_header(page_number)

    c.setFont("DejaVuSans", 10)
    c.drawString(400, y_position, "Общая сумма:")
    c.drawString(500, y_position, f"{total_sum:.2f}")

    # Сохранение файла
    c.save()

    # Уведомление об успешном сохранении
    QMessageBox.information(self, "Отчёт сгенерирован", f"Отчёт успешно сохранён в {file_name}")
