import numpy as np
import cv2

def brightness1():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return
    
    dst = cv2.add(src, 100)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def brightness2():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    
    print(src)
    
    if src is None :
        print('Image load failed!')
        return

    dst = np.empty(src.shape, src.dtype)

    print(dst)

    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = src[y, x] + 100 
            # src[0, 0]이 162일 때 + 100 -> 262 , 262-256 = 6 -> 
            # white(픽셀값 255)에 가까웠던 부분이 black(픽셀값 0)에 가깝게 됨

    print(dst)

    cv2.imshow('scr', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def saturated(value):
    if value > 255 :
        value = 255
    elif value < 0 :
        value = 0
    return value

def brightness3():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None :
        print('Image load failed!')
        return
    
    dst = np.empty(src.shape, dtype=src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y, x] = saturated(src[y, x] + 100) # 255를 넘기면 saturated() 때문에 최댓값 255로 그대로 적용, 반전되지 않는다

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()


def brightness4():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None :
        print('Image load failed!')
        return
    
    def update(pos):
        dst = cv2.add(src, pos)
        cv2.imshow('dst', dst)

    cv2.namedWindow('dst')
    cv2.createTrackbar('Brightness', 'dst', 0, 100, update)
    update(0)

    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    brightness1()
    brightness2()
    brightness3()
    brightness4()