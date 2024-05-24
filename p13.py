from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QMessageBox
from PySide6.QtGui import QFont
from PySide6.QtCore import QSize

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.label = QLabel("Masukkan detail Anda:")
        self.label.setFont(QFont('Arial'))

        self.name_textbox = QLineEdit()
        self.name_textbox.setFont(QFont('Arial'))
        self.name_textbox.setPlaceholderText("Nama")

        self.nim_textbox = QLineEdit()
        self.nim_textbox.setFont(QFont('Arial'))
        self.nim_textbox.setPlaceholderText("NIM")

        self.hobby_textbox = QLineEdit()
        self.hobby_textbox.setFont(QFont('Arial'))
        self.hobby_textbox.setPlaceholderText("Hobi")

        self.button = QPushButton("Kirim")
        self.button.setFont(QFont('Arial'))


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.name_textbox)
        self.layout.addWidget(self.nim_textbox)
        self.layout.addWidget(self.hobby_textbox)
        self.layout.addWidget(self.button)
        # self.setStyleSheet("background-color: #F5B7AA;")
        self.button.clicked.connect(self.greet)
        self.button.setStyleSheet("background-color: #82E0AA ;")

    def greet(self):
        name = self.name_textbox.text()
        nim = self.nim_textbox.text()
        hobby = self.hobby_textbox.text()
        self.label.setText(f"Halo, {name}!\nNIM Anda adalah {nim}\ndan hobi Anda adalah {hobby}.")

    def reset(self):
        self.name_textbox.clear()
        self.nim_textbox.clear()
        self.hobby_textbox.clear()
        self.label.setText("Masukkan detail Anda:")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikasi Input Detail")
        
        self.widget = CustomWidget()
        self.setCentralWidget(self.widget)
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec_()
