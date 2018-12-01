import glob
import cv2

# print(cv2.__version__)

# 0 = gray | 1 = RGB
img = cv2.imread('galaxy.jpg', 0)

# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)

resize_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
cv2.imshow("Galaxy", resize_img)
cv2.imwrite("Galaxy_resized.jpg", resize_img)
# 2000 ms | 0 waits for button to close
cv2.waitKey(2000)
cv2.destroyAllWindows()

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image, re)
