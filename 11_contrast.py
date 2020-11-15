import numpy as np
import cv2

def contrast1():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None :
        print('Image load failed!')
        return
    
    print(src)

    s = 2.0
    dst = cv2.multiply(src, s)

    print(dst) 
    print()
    print()
    # 어떤 픽셀값이 162일 경우에 2를 곱하면 324가 된다
    # 이 경우에는 최댓값 255로 나타나진다

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def contrast2():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None :
        print('Image load failed!')
        return

    print(src)
    
    # dst(x,y) = src(x,y) + (src(x,y) - 128)*alpha
    alpha = 1.0
    dst = np.clip(src + (src - 128.)*alpha, 0, 255).astype(np.uint8)
    # np.clip(a, a_min, a_max) # 최솟값, 최댓값을 적용시켜 범위를 제한한다

    print(dst)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    cv2.destroyAllWindows()    

if __name__ == '__main__':
    contrast1()
    contrast2()