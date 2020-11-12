import numpy as numpy
import cv2

# 카메라 입력 처리 
def camera_in():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open failed!")
        return

    print('Frame width :', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height :', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    while True :
        ret, frame = cap.read()

        if not ret :
            break

        inversed = ~frame

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        # waitKey() 함수 인자에 보통 0보다 큰 정수를 입력해야 한다
        # 0을 지정하면 사용자의 키 입력을 무한히 기다리기 때문에
        # 카메라 혹은 동영상 파일의 초당 프레임 수를 고려햐여 충분히 작은 정수를 입력해야 한다
        # 아래처럼 10을 전달하면 10ms 동안 기다린 후, 다음 프레임을 받아 오게 된다
        if cv2.waitKey(10) == 27 : # 27 == esc
            break

    cv2.destroyAllWindows()

# 동영상 파일 처리
def video_in():
    cap = cv2.VideoCapture('stopwatch.avi')

    if not cap.isOpened():
        print("Video open failed!")
        return

    print('Frame width :', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
    print('Frame height :', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print('Frame  count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT))) # 비디오 파일의 전체 프레임 수 반환
    
    fps = cap.get(cv2.CAP_PROP_FPS) # 초당 프레임 수
    print('FPS :', fps)

    delay = round(1000 / fps)

    while True :
        ret, frame = cap.read()
        
        if not ret :
            break

        inversed = ~frame

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(delay) == 27 :
            break

    cv2.destroyAllWindows()

# 동영상 파일 저장하기
def camera_in_video_out():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Camera open failed!')
        return

    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # 'DIVX' == 'D', 'I', 'V', 'X'
    delay = round(1000/fps)

    outputVideo = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

    if not outputVideo.isOpened():
        print('File open failed!')
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        inversed = ~frame

        outputVideo.write(inversed)

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(delay) == 27:
            break

    cv2.destroyAllWindows()

if __name__ == '__main__' :
    # camera_in()   
    # video_in()
    camera_in_video_out()



# 동영상 파일 처리하기
# 동영상 파일은 모두 나름대로의 초당 프레임 수, FPS(Frames Per Second) 값을 가지고 있다
# 동영상 파일을 재생하는 프로그램을 만들 경우 해당 동영상의 FPS 값을 고려하지 않으면 동영상이
# 너무 빠르거나 느리게 재생되는 경우가 발생
# 그래서 동영상을 적절한 속도로 재생하려면 동영상의 FPS 값을 참고해야 한다
# cv2.CAP_PROP_FPS를 통해 동영상의 FPS 값을 확인하고 그 값으로부터 각 프레임 사이의 시간 간격,
# delay(밀리초 단위)를 계산한다