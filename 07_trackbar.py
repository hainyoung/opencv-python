import numpy as np
import cv2

def saturated(value):
    if value > 255 :
        value = 255
    elif value < 0 :
        value = 0
    
    return value

def on_level_change(pos):
    img[:] = saturated(pos * 16)
    cv2.imshow('image', img)

img = np.zeros((400, 400), np.uint8)

cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)
# cv2.createTracbar(trackbarName, windowName, value, count, onChange) -> None
# trackbarName : 트랙바 이름
# windowName : 트랙바를 생성할 창 이름
# value : 트랙바 위치 초기값
# count : 트랙바 최댓값. 최솟값은 항상 0
# onChange : 트랙바 위치가 변경될 때마다 호출할 콜백 함수 이름


cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()