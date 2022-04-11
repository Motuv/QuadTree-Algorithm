import cv2
def draw(rect, img):
    cv2.rectangle(img, (rect.top, rect.left), (rect.top+rect.height, rect.left+rect.width), (0, 0, 255), 1)
