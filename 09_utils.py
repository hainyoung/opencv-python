import numpy as np
import cv2

# lenna.bmp 영상의 일부 영역에 대해서만 픽셀 값을 특정색으로 설정
# 여기서는 (0, 255, 255) : yellow

def mask_setTo():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_smile.bmp', cv2.IMREAD_GRAYSCALE)
    # mask는 0 ~ 255로 이뤄져 있음(픽셀값이)

    if src is None or mask is None:
        print('Image laod failed!')
        return

    src[mask > 0] = (0, 255, 255)
    # mask 영상에서 픽셀 값이 0이 아닌 위치에서만 src 영상 픽셀을 노란색으로 설정
    # mask는 흑백영상, 따라서 0이 아닌 위치 : white 부분만 yellow 로 변함

    cv2.imshow('src', src)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()

def mask_copyTo():
    src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
    dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

    if src is None or mask is None or dst is None:
        print('Image load failed!')
        return
    cv2.copyTo(src, mask, dst)
    # cv2.copyTo(src, mask, dst=None) -> dst
    # src : source, 입력 영상
    # mask : 마스크 영상
    # dst : 출력 영상, 만약 src와 크기 및 타입이 같은 dst를 입력으로 지정하면 dst를 새로 생성하지 않고 연산을 수행
    # 그렇지 않으면 dst를 새로 생성하여 연산을 수행한 후 반환

    # dst[mask > 0] = src[mask > 0]

    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


def time_inverse():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
    print(src.shape)
    print(src)

    if src is None :
        print('Image load failed!')
        return
    dst = np.empty(src.shape, dtype = src.dtype)

    tm = cv2.TickMeter()
    tm.start()

    for y in range(src.shape[0]):
        for x in range(src.shape[1]): 
            dst[y, x] = 255 - src[y, x]
    
    tm.stop()
    print('Image inverse implementation took %4.3f ms' % tm.getTimeMilli())
    print(dst)

    cv2.imshow('src', src)
    cv2.imshow('dst', dst) 
    cv2.waitKey()
    cv2.destroyAllWindows()   

def useful_func():
    img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('Image load faild!')
        return

    sum_img = np.sum(img)
    mean_img = np.mean(img, dtype = np.int32)
    print('Sum :', sum_img)
    print('Mean :', mean_img)
    print()

    minVal, maxVal, minPos, maxPos = cv2.minMaxLoc(img)
    print('minVal is', minVal, 'at', minPos)
    print('maxVal is', maxVal, 'at', maxPos)
    print()

    src = np.array([[-1, -0.5, 0, 0.5, 1]], dtype = np.float32)
    dst1 = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    # cv2.normalize(src, dst, alpha, beta, norm_type, dtype, mask)
    # src : input image, 정규화 이전의 데이터
    # dst : output image, 정규화 이후의 데이터
    # alpha : 수치의 표준화를 진행할 때 하한값, 정규화 구간 1
    # beta : 수치의 표준화를 진행할 때 상한값, 정규화 구간 2 (구간 정규화가 아닌 경우 사용 하지 않음)
    # norm type : 정규화 알고리즘 선택 플래그 상수, 아래의 옵션들이 있다
    # 1) alpha와 beta 구간으로 정규화하는 cv2.NORM_MIINMAX
    # 2) 전체합으로 나누는 cv2.NOMR_L1
    # 3) 단위벡터로 정규화하는 cv2.NORM_L2
    # 4) 최댓값으로 나누는 cv2.NORM_INF

    dst2 = cv2.normalize(src, None, cv2.NORM_L1)
    dst3 = cv2.normalize(src, None, cv2.NORM_L2)
    dst4 = cv2.normalize(src, None, cv2.NORM_INF)

    dst5 = cv2.normalize(dst1, None, cv2.NORM_L1)
    dst6 = cv2.normalize(dst1, None, cv2.NORM_L2)
    dst7 = cv2.normalize(dst1, None, cv2.NORM_INF)

    # dst = cv2.normalize(src, None, 0, 65535, cv2.NORM_MINMAX, cv2.CV_16U)
    # dst = cv2.normalize(src, None, 0, 1, cv2.NORM_MINMAX, cv2.CV_32F)

    # CV_8U : 이미지값 범위 0 ~ 255
    # CV_16U : 이미지값 범위 0 ~ 65535
    # CV_32F : 이미지값 범위 0 ~ 1

    print('src :', src)
    print('dst :', dst1)
    print('dst :', dst2)
    print('dst :', dst3)
    print('dst :', dst4)
    print('dst :', dst5)
    print('dst :', dst6)
    print('dst :', dst7)
    print()

    # print('round(2.5) is', round(2.5))
    # print('round(2.51) is', round(2.51))
    # print('round(3.499) is', round(3.499))
    # print('round(3.5) is', round(3.5))



if __name__ == '__main__':
    # mask_setTo()
    # mask_copyTo()
    # time_inverse()
    useful_func()

# a = np.array([[1, 1], [2, 2]])
# print(10-a)