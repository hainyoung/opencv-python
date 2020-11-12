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

    img2 = img1 # 얕은 복사 img2 영상 img1의 픽셀 데이터를 공유한다
    img3 = img1.copy() # 깊은 복사 copy()를 이용, 고양이 영상을 그대로 간직

    img1[:, :] = (0, 255, 255) # yellow(green + blue)

    cv2.imshow('img1', img1) # yellow
    cv2.imshow('img2', img2) # yellow
    cv2.imshow('img3', img3) # cat
    cv2.waitKey()
    cv2.destroyAllWindows()

# 부분 행렬 추출
def func4():
    img1 = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    img2 = img1[200:400, 200:400] # 부분 영상 추출 / 얕은 복사로, 소스 이미지에 영향을 미친다
    img3 = img1[200:400, 200:400].copy() # 부분 영상 추출 / copy()를 이용한 깊은 복사로, 소스 이미지에 영향을 미치지 않는다

    img2 += 20
    # img3 += 20
    print(img2)
    # print(img3)

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)
    cv2.imshow('img3', img3)
    cv2.waitKey()
    cv2.destroyAllWindows()


def func5():
    mat1 = np.array(np.arange(12)).reshape(3, 4)

    print('mat1:')
    print(mat1)
    print(mat1.shape) # (3, 4)

    h, w = mat1.shape[:2]
    print('h :', h) # 3
    print('w :', w) # 4

    mat2 = np.zeros(mat1.shape, type(mat1))
    print('mat2 :')
    print(mat2)
    # [[0 0 0 0]
    # [0 0 0 0]
    # [0 0 0 0]]

    for j in range(h):
        for i in range(w):
            mat2[j, i] = mat1[j, i] + 10
    print('--after loop--')
    print('mat2:')
    print(mat2)
    # [[10 11 12 13]
    # [14 15 16 17]
    # [18 19 20 21]]


def func6():
    mat1 = np.ones((3, 4), np.int32)    # 1's matrix
    mat2 = np.arange(12).reshape(3, 4)
    mat3 = mat1 + mat2
    mat4 = mat2 * 2

    print("mat1:", mat1, sep='\n')
    print("mat2:", mat2, sep='\n')
    print("mat3:", mat3, sep='\n')
    print("mat4:", mat4, sep='\n')



if __name__ == '__main__':
    # func1()
    # func2()
    # func3()
    func4()
    # func5()
    # func6()