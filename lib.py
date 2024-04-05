#Запросить данные с помощью библиотеки requests из API и вывести их в консоль.
import requests as rq
response = rq.get('https://openweathermap.org/api')
print(response)
#Считать данные из файла с помощью библиотеки pandas, выполнить простой анализ данных и вывести результаты.
import pandas as pd
data = pd.read_csv("C:\\Users\\Valeriya\\AppData\\Local\\Programs\\Python\\Python312\\time_series_19-covid-Confirmed_archived_0325.csv")
print(data.head(5))
#Создать массив чисел с помощью библиотеки numpy, выполнить математические операции с массивом и вывести результаты.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2
print(result)
#Визуализировать данные с помощью библиотеки matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [25, 32, 34, 20, 25]
plt.plot(x, y)
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Первый график')
plt.show()
#Обработать изображение с помощью библиотеки pillow, например, изменить его размер, применить эффекты и сохранить в другой формат.
from PIL import Image
image = Image.open('C:\\Users\\Valeriya\\AppData\\Local\\Programs\\Python\\Python312\\dori.jpg')
# Изменяем цветовую палитру изображения на оттенки серого
gray_image = image.convert("L")
gray_image.save("gray_image.jpg")
gray_image.show()