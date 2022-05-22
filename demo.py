import requests
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_clicked)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        response = requests.get(
            url='https://62c9-95-56-128-231.ngrok.io/api/v1/roles/'
        )

        front_text: str = "\n".join(
            [f"{x['id']} - {x['name1']}" for x in response.json()]
        )
        self.button.setText(front_text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
