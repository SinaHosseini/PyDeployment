import requests
import sys
import json
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtGui import *


def get():
    try:
        global data
        user_text = window.txt_box.text()
        response = requests.get(
            f"https://goweather.herokuapp.com/weather/{user_text}")
        data = json.loads(response.text)

        window.dec_lb.setText("           " + data["description"])
        window.temp_lb.setText("     " + data["temperature"])
        window.wind_lb.setText("Wind: " + data["wind"])
        window.tomorrow.setText(
            "tomorrow\n" + data["forecast"][0]["temperature"] + "\n" + data["forecast"][0]["wind"])
        window.day_later.setText(
            "2 days later\n" + data["forecast"][1]["temperature"] + "\n" + data["forecast"][1]["wind"])
        window.day_later2.setText(
            "3 days later\n" + data["forecast"][2]["temperature"] + "\n" + data["forecast"][2]["wind"])

        if data["description"] == "Sunny":
            window.icon_lb.setPixmap(QIcon("Icon\Sun.png"))
            window.icon_lb.pixmap(340, 340)
        elif data["description"] == "Partly cloudy":
            window.icon_lb.setPixmap(QIcon("Icon\Day Partly Cloudy.png"))
            window.icon_lb.pixmap(340, 340)
        elif data["description"] == "Cloudy":
            window.icon_lb.setPixmap(QIcon("Icon\Day Cloudy.png"))
            window.icon_lb.pixmap(340, 340)
        elif data["description"] == "Rainy":
            window.icon_lb.setPixmap(QIcon("Icon\Rain Drops.png"))
            window.icon_lb.pixmap(340, 340)
        elif data["description"] == "Snow":
            window.icon_lb.setPixmap(QIcon("Icon\Snow.png"))
            window.icon_lb.pixmap(340, 340)
        elif data["description"] == "Wind":
            window.icon_lb.setPixmap(QIcon("Icon\Wind.png"))
            window.icon_lb.pixmap(340, 340)
        elif data["description"] == "Tornado":
            window.icon_lb.setPixmap(QIcon("Icon\Tornado.png"))
            window.icon_lb.pixmap(340, 340)
        elif data["description"] == "Thunderstorm":
            window.icon_lb.setPixmap(
                QIcon("Icon\Day Windy Angled Rain Drops With Lightning.png"))
            window.icon_lb.pixmap(340, 340)

    except:
        msg_box = QMessageBox(text="Connection error")
        msg_box.exec()


app = QApplication(sys.argv)

loader = QUiLoader()
window = loader.load("weather.ui")
window.show()

window.btn_search.clicked.connect(get)

app.exec()
