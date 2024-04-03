import requests
import sys
import json
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *


def get():
    global data
    user_text = window.txt_box.text()
    response = requests.get(
        f"https://goweather.herokuapp.com/weather/{user_text}")
    data = json.loads(response.text)
    print(data)

    window.dec_lb.setText("             " + data["description"])
    window.temp_lb.setText("     " + data["temperature"])
    window.wind_lb.setText("Wind: " + data["wind"])


app = QApplication(sys.argv)

loader = QUiLoader()
window = loader.load("weather.ui")
window.show()

window.btn_search.clicked.connect(get)

app.exec()
