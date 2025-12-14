from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout
import sys

class TimetableApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dars jadvali")
        self.setGeometry(300, 300, 300, 150)

        # Dars jadvali dict
        self.timetable = {
            "Dushanba": ["Matematika", "Fizika"],
            "Seshanba": ["Ingliz tili", "Tarix"],
            "Chorshanba": ["Biologiya", "Geografiya"]
        }

        # ComboBox - foydalanuvchi kunni tanlaydi
        self.day_combo = QComboBox()
        self.day_combo.addItems(self.timetable.keys())
        self.day_combo.currentIndexChanged.connect(self.show_classes)

        # Natija chiqarish uchun label
        self.result_label = QLabel("Darslar shu yerda chiqadi")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.day_combo)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # Dastlabki kunning darslarini chiqarish
        self.show_classes()

    # Tanlangan kunning darslarini chiqarish funksiyasi
    def show_classes(self):
        day = self.day_combo.currentText()
        classes = self.timetable.get(day, [])
        self.result_label.setText(f"{day} darslari: {', '.join(classes)}")

# Ilovani ishga tushirish
app = QApplication(sys.argv)
window = TimetableApp()
window.show()
sys.exit(app.exec_())
