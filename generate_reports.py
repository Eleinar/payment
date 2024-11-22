from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab import rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from PySide6.QtWidgets import QFileDialog, QMessageBox

from modules import PaymentList, create_connection

font_path = "DejaVuSans.ttf"

def generate_report(self, start_date, end_date, user_id):
    # Запрос всех данных по платежам в выбранном периоде
    db = create_connection()
    
    #start_date = start_date.date().toPython()
    #end_date = end_date.date().toPython()
    
    payments = db.query(PaymentList).filter(
        PaymentList.pay_day >= start_date,
        PaymentList.pay_day <= end_date,
        PaymentList.user_id == user_id
    )
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
    
    c.setFont("DejaVuSans", 12)

    # Заголовок
    c.setFont("DejaVuSans", 16)
    c.drawString(50, height - 40, f"Отчёт по платежам с {start_date} по {end_date}")

    # Таблица
    c.setFont("DejaVuSans", 10)
    c.drawString(20, height - 80, "№")
    c.drawString(80, height - 80, "Название")
    c.drawString(200, height - 80, "Количество")
    c.drawString(300, height - 80, "Цена")
    c.drawString(400, height - 80, "Итоговая сумма")
    c.drawString(500, height - 80, "Дата")

    # Заполнение таблицы
    y_position = height - 100
    total_sum = 0

    for idx, payment in enumerate(payments, start=1):
        y_position -= 20
        c.drawString(20, y_position, str(idx))
        c.drawString(80, y_position, payment.pay_name)
        c.drawString(200, y_position, str(payment.pay_count))
        c.drawString(300, y_position, f"{payment.pay_cost:.2f}")
        total = payment.pay_count * payment.pay_cost
        c.drawString(400, y_position, f"{total:.2f}")
        c.drawString(500, y_position, payment.pay_day.strftime('%d-%m-%Y'))
        total_sum += total

    # Итоговая сумма
    c.setFont("DejaVuSans", 10)
    c.drawString(450, y_position - 20, "Общая сумма:")
    c.drawString(550, y_position - 20, f"{total_sum:.2f}")

    # Сохранение файла
    c.save()

    # Уведомление об успешном сохранении
    QMessageBox.information(self, "Отчёт сгенерирован", f"Отчёт успешно сохранён в {file_name}")
