from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class EmployeeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ofis xodimlari")
        self.setGeometry(300, 300, 300, 200)

        # Xodimlar dict
        self.employees = {
            "Dilshod": "Direktor",
            "Aziza": "Hisobchi"
        }

        # Widgets
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Xodim ismini kiriting")

        self.show_btn = QPushButton("Lavozimini ko'rsat")
        self.show_btn.clicked.connect(self.show_position)

        self.add_name_input = QLineEdit()
        self.add_name_input.setPlaceholderText("Yangi xodim ismi")

        self.add_position_input = QLineEdit()
        self.add_position_input.setPlaceholderText("Yangi xodim lavozimi")

        self.add_btn = QPushButton("Yangi xodim qo'shish")
        self.add_btn.clicked.connect(self.add_employee)

        self.result_label = QLabel("Natija shu yerda chiqadi")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addWidget(self.show_btn)
        layout.addWidget(self.add_name_input)
        layout.addWidget(self.add_position_input)
        layout.addWidget(self.add_btn)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

    # Lavozimni ko'rsatish funksiyasi
    def show_position(self):
        name = self.name_input.text()
        position = self.employees.get(name)
        if position:
            self.result_label.setText(f"{name} lavozimi: {position}")
        else:
            self.result_label.setText(f"{name} topilmadi!")

    # Yangi xodim qo'shish funksiyasi
    def add_employee(self):
        name = self.add_name_input.text()
        position = self.add_position_input.text()
        if name and position:
            self.employees[name] = position
            self.result_label.setText(f"{name} qo'shildi!")
            self.add_name_input.clear()
            self.add_position_input.clear()
        else:
            self.result_label.setText("Iltimos, ism va lavozim kiriting!")

# Ilovani ishga tushirish
app = QApplication(sys.argv)
window = EmployeeApp()
window.show()
sys.exit(app.exec_())
