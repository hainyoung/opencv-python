import numpy as np
import cv2

def drawLines():
    img = np.full((400, 400, 3), 255, np.uint8)

    cv2.line(img, (50, 50), (200, 50), (0, 0, 255)) # (x0, y0), (x1, y1), (b, g, r)
    cv2.line(img, (50, 100), (200, 100), (255, 0, 255), 3) # x0, y0), (x1, y1), (b, g, r), thickness
    cv2.line(img, (50, 150), (200, 150), (255, 0, 0), 10)

    cv2.line(img, (250, 50), (350, 100), (0, 0, 255), 1, cv2.LINE_4)
    cv2.line(img, (250, 70), (350, 120), (255, 0, 255), 1, cv2.LINE_8)
    cv2.line(img, (250, 90), (350, 140), (255, 0, 0), 1, cv2.LINE_AA)

    cv2.arrowedLine(img, (50, 200), (150, 200), (0, 0, 255), 1)
    cv2.arrowedLine(img, (50, 250), (350, 250), (255, 0, 255), 1)
    cv2.arrowedLine(img, (50, 300), (350, 300), (255, 0, 0), 1, cv2.LINE_8, 0, 0.05)

    cv2.drawMarker(img, (50, 350), (0, 0, 255), cv2.MARKER_CROSS)
    cv2.drawMarker(img, (100, 350), (0, 0, 255), cv2.MARKER_TILTED_CROSS)
    cv2.drawMarker(img, (150, 350), (0, 0, 255), cv2.MARKER_STAR)
    cv2.drawMarker(img, (200, 350), (0, 0, 255), cv2.MARKER_DIAMOND)
    cv2.drawMarker(img, (250, 350), (0, 0, 255), cv2.MARKER_SQUARE)
    cv2.drawMarker(img, (300, 350), (0, 0, 255), cv2.MARKER_TRIANGLE_UP)
    cv2.drawMarker(img, (350, 350), (0, 0, 255), cv2.MARKER_TRIANGLE_DOWN)
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


def drawPolys():
    img = np.full((400, 400, 3), 255, np.uint8)

    cv2.rectangle(img, (50, 50), (150, 100), (0, 0, 255), 2)
    cv2.rectangle(img, (50, 150), (150, 200), (0, 0, 128), -1)

    cv2.circle(img, (300, 120), 30, (255, 255, 0), -1, cv2.LINE_AA)
    cv2.circle(img, (300, 120), 60, (255, 0, 0), 3, cv2.LINE_AA)

    cv2.ellipse(img, (120, 300), (60, 30), 20, 0, 270, (255, 255, 0), cv2.FILLED, cv2.LINE_AA)
    cv2.ellipse(img, (120, 300), (100, 50), 20, 0, 360, (0, 255, 0), 2, cv2.LINE_AA)

    pts = np.array([[250, 250], [300, 250], [300, 300], [350, 300], [350, 350], [250, 350]])
    cv2.polylines(img, [pts], True, (255, 0, 255), 2)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    # drawLines()
    drawPolys()
    # drawText1()
    # drawText2()
