from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QVBoxLayout
import sys

class SupermarketApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Supermarket savatchasi")
        self.setGeometry(300, 300, 300, 200)

        # Mahsulotlar va narxlari
        self.products = {
            "Olma": 5000,
            "Banan": 7000,
            "Sut": 12000
        }

        # Widgets
        self.product_combo = QComboBox()
        self.product_combo.addItems(self.products.keys())

        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("Miqdorini kiriting")

        self.calc_btn = QPushButton("Hisoblash")
        self.calc_btn.clicked.connect(self.calculate_total)

        self.result_label = QLabel("Natija shu yerda chiqadi")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.product_combo)
        layout.addWidget(self.quantity_input)
        layout.addWidget(self.calc_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    # Umumiy summani hisoblash funksiyasi
    def calculate_total(self):
        product = self.product_combo.currentText()
        try:
            quantity = int(self.quantity_input.text())
            total = self.products[product] * quantity
            if total > 100000:
                self.result_label.setText(f"Umumiy summa: {total} so'm. Chegirma qo'llandi!")
            else:
                self.result_label.setText(f"Umumiy summa: {total} so'm")
        except ValueError:
            self.result_label.setText("Iltimos, miqdorni to'g'ri kiriting!")

# Ilovani ishga tushirish
app = QApplication(sys.argv)
window = SupermarketApp()
window.show()
sys.exit(app.exec_())
