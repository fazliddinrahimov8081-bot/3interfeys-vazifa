from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QVBoxLayout
import sys

class BudgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oyma-oy byudjet nazorati")
        self.setGeometry(300, 300, 300, 150)

        # Oylar va xarajatlar
        self.expenses = {
            "Yanvar": [1200000, 500000],
            "Fevral": [2000000, 800000],
            "Mart": [1000000, 600000]
        }

        # ComboBox
        self.combo = QComboBox()
        self.combo.addItems(self.expenses.keys())
        self.combo.currentIndexChanged.connect(self.show_expense)

        # Label
        self.label = QLabel("Umumiy xarajat shu yerda chiqadi")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.combo)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Dastlab tanlangan oy xarajatini chiqarish
        self.show_expense()

    def show_expense(self):
        oy = self.combo.currentText()
        total = sum(self.expenses[oy])
        self.label.setText(f"{oy} oyining umumiy xarajati: {total} so'm")

# Ilovani ishga tushirish
app = QApplication(sys.argv)
window = BudgetApp()
window.show()
sys.exit(app.exec_())
