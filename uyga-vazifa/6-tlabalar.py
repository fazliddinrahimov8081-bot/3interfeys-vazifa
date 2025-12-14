from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
import sys
import random  # Tasodifiy tanlash uchun

class RandomStudentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Talabani tasodifiy tanlash")
        self.setGeometry(300, 300, 300, 150)

        # Talabalar ro'yxati
        self.students = ["Ali", "Sara", "Dilshod", "Aziza", "Jasur"]

        # Natijani chiqarish uchun label
        self.result_label = QLabel("Tanlangan talabani shu yerda ko'rasiz")

        # 'Tanlash' tugmasi
        self.pick_btn = QPushButton("Tanlash")
        self.pick_btn.clicked.connect(self.pick_student)  # Tugma bosilganda funksiyani chaqirish

        # Layout - elementlarni ustma-ust joylashtirish
        layout = QVBoxLayout()
        layout.addWidget(self.result_label)
        layout.addWidget(self.pick_btn)
        self.setLayout(layout)

    # Tasodifiy talabani tanlash funksiyasi
    def pick_student(self):
        student = random.choice(self.students)  # listdan tasodifiy ism tanlash
        self.result_label.setText(f"Tanlangan talaba: {student}")  # Natijani ekranga chiqarish

# Ilovani ishga tushirish
app = QApplication(sys.argv)
window = RandomStudentApp()
window.show()
sys.exit(app.exec_())

