from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QListWidget, QVBoxLayout
import sys

class LibraryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kutubxona katalogi")
        self.setGeometry(300, 300, 400, 250)

        # Kitoblar ro'yxati
        self.books = ["Python Asoslari", "Flask Dasturlash", "Sun'iy Intellekt"]

        # Qidiruv oynasi
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Kitob nomini kiriting...")
        self.search_input.textChanged.connect(self.search_books)  # Matn o'zgarganda qidirish

        # Natija chiqarish uchun ro'yxat
        self.result_list = QListWidget()
        self.result_list.addItems(self.books)  # Dastlab barcha kitoblarni ko'rsatish

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.search_input)
        layout.addWidget(self.result_list)
        self.setLayout(layout)

    # Qidiruv funksiyasi
    def search_books(self):
        text = self.search_input.text().lower()  # Kiritilgan matnni kichik harfga o'zgartirish
        self.result_list.clear()  # Avvalgi natijalarni tozalash
        for book in self.books:
            if text in book.lower():  # Agar matn kitob nomida mavjud bo'lsa
                self.result_list.addItem(book)  # Ro'yxatga qo'shish

# Ilovani ishga tushirish
app = QApplication(sys.argv)
window = LibraryApp()
window.show()
sys.exit(app.exec_())
