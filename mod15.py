import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

cv2.circle(photo,(photo.shape[1]//2, photo.shape[0]//2),180, (255, 255, 255), thickness=3)

center_x, center_y = photo.shape[1]//2, photo.shape[0]//2
radius = 100

cv2.line(photo, (center_x - radius//2, center_y - 70), (center_x - radius//2 - 50, center_y - 70), (21, 21, 255), thickness=3)
cv2.line(photo, (center_x + radius//2, center_y - 70), (center_x + radius//2 + 50, center_y - 70), (21, 21, 255), thickness=3)

cv2.line(photo, (center_x - radius//2, center_y - 70), (center_x + radius//2 - 100, center_y + 10), (158, 74, 2), thickness=3)
cv2.line(photo, (center_x - radius//2 - 50, center_y - 70), (center_x + radius//2 - 150, center_y + 10), (158, 74, 2), thickness=3)

cv2.line(photo, (center_x + radius//2, center_y - 70), (center_x + radius//2 - 0, center_y + 10), (158, 74, 2), thickness=3)
cv2.line(photo, (center_x + radius//2 + 50, center_y - 70), (center_x + radius//2 + 50, center_y + 10), (158, 74, 2), thickness=3)

cv2.ellipse(photo, (center_x + radius//2 - 50, center_y + 10), (radius - 0, 100), 0, 0, 180, (66, 255, 170), thickness=3)
cv2.ellipse(photo, (center_x + radius//2 - 50, center_y + 10), (radius - 50, 50), 0, 0, 180, (66, 255, 170), thickness=3)

cv2.imshow('Photo', photo)
cv2.waitKey(0)
