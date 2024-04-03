import requests
import json
import numpy as np
import cv2
import matplotlib.pyplot as plt

response = requests.get("https://goweather.herokuapp.com/weather/Mashhad")

print(json.loads(response.text))
# print("\n", response.status_code)

# response = requests.get("https://picsum.photos/200/300")

# # print(response.status_code)
# # print(response.content)

# file_date = np.frombuffer(response.content, dtype="int8")
# image = cv2.imdecode(file_date, cv2.IMREAD_UNCHANGED)

# plt.imshow(image)
# plt.show()


# # #response = requests.get("https://thispersondoesnotexist.com")
# # #file_date = np.frombuffer(response.content, dtype="int8")
# # #image = cv2.imdecode(file_date, cv2.IMREAD_UNCHANGED)
# # #
# # #plt.imshow(image)
# # #plt.show()
