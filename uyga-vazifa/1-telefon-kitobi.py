from PyQt5.QtWidgets import (QApplication,
                             QWidget,QComboBox,
                            QLabel,QVBoxLayout  )
import sys
class PhoneBook(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telefon kitobi")
        self.setGeometry(300,300,300,150)

        self.phone_book = {
            "Ali": "99890 123 45 67",
            "Vali": "99891 987 65 43",
            "Zayd": "99893 555 44 33"
        }
        self.combo = QComboBox()
        self.combo.addItems(self.phone_book.keys())
        self.combo.currentTextChanged.connect(self.show_number)

        self.label = QLabel("Telefon raqami shu yerda chiqadi")

        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.label)       
        self.setLayout(layout)
        self.show_number()
    def show_number(self):
        name = self.combo.currentText()
        self.label.setText(self.phone_book[name])

app = QApplication(sys.argv)
window = PhoneBook()
window.show()
sys.exit(app.exec_())

