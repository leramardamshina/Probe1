from PIL import Image
image = Image.open('C:\\Users\\Valeriya\\AppData\\Local\\Programs\\Python\\Python312\\dori.jpg')
# Изменяем цветовую палитру изображения на оттенки серого
gray_image = image.convert("L")
gray_image.save("gray_image.jpg")
gray_image.show()