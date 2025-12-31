import cv2
import numpy as np

# Загрузка изображения
image_path = 'D:\Users\rom\laserimages\apelsin'  # укажи путь к своему изображению
image = cv2.imread(image_path)

# Проверка, загрузилось ли изображение
if image is None:
    print("Не удалось загрузить изображение. Проверьте путь.")
    exit()

# Применение размытия по Гауссу
gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)  # радиус 15, можно изменить по желанию

# Создание матрицы для резкости
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],в
                   [0, -1, 0]])

# Применение фильтра резкости
sharpened = cv2.filter2D(gaussian_blur, -1, kernel)

# Сохранение итогового изображения
cv2.imwrite('result.jpg', sharpened)
print("Обработка завершена. Результат сохранен как 'result.jpg'.")