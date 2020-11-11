import numpy as np
import cv2

def func1():
    img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

    if img1 is None:
        print("Image load failed")
        return

    print('type(img1):', type(img1))
    print('image1.shape:', img1.shape)
    print('imag1.shape length:', len(img1.shape))

    if len(img1.shape) == 2:
        print('img1 is a grayscale image')
    elif len(img1.shape) == 3:
        print('img1 is a truecolor image')

    cv2.imshow('img1', img1)
    cv2.waitKey()
    cv2.destroyAllWindows()

def func2():
    img1 = np.empty((480, 640), np.uint8) # grayscale image
    img2 = np.zeros((480, 640, 3), np.uint8) # color image
    img3 = np.ones((480, 640), np.int32) # 1's matrix
    img4 = np.full((480, 640), 0, np.float32) # Fill with 0.0

    mat1 = np.array([[11, 12, 13, 14],
                    [21, 22, 23, 24],
                    [31, 32, 33, 34]]).astype(np.uint8)
    mat1[0, 1] = 100 # element at x = 1, y = 0
    mat1[2, :] = 200

    print(mat1)

def func3():
    img1 = cv2.imread('cat.bmp')

    img2 = img1
    img3 = img1.copy()

    img1[:, :] = (0, 255, 255) # yellow(green + blue)

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # func1()
    # func2()
    func3()