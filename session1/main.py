import requests
import sys
import json
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *


def get():
    user_text = window.txt_box.text()
    response = requests.get(
        f"https://goweather.herokuapp.com/weather/{user_text}")
    data = json.loads(response.text)
    print(type(data))


app = QApplication(sys.argv)

loader = QUiLoader()
window = loader.load("weather.ui")
window.show()

user_text = window.txt_box.text()
window.btn_search.clicked.connect(get)

app.exec()
