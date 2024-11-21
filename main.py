from PySide6.QtWidgets import QApplication
from login_window import LoginWindow
app = QApplication([])
window = LoginWindow()
window.show()
app.exec()