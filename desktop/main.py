import sys

import requests
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from midka.settings import INTERNAL_HOST


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
        response = requests.get(url=f"{INTERNAL_HOST}/api/v1/roles/")

        front_text: str = "\n".join(
            [f"{x['id']} - {x['name1']}" for x in response.json()]
        )
        self.button.setText(front_text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
