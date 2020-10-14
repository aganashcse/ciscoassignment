"""
This python code will show a picture of combined geometric shapes.
"""

import numpy as np
import cv2


def imageProcessing():
    image = np.zeros((512, 512, 3), np.uint8)

    cv2.circle(image, (250, 250), 50, (0, 255, 0), 5)
    cv2.line(image, (250, 220), (280, 250), (255, 0, 0), 5)
    cv2.line(image, (280, 250), (250, 280), (255, 0, 0), 5)
    cv2.line(image, (250, 280), (220, 250), (255, 0, 0), 5)
    cv2.line(image, (220, 250), (250, 220), (255, 0, 0), 5)

    cv2.line(image, (220, 190), (280, 190), (0, 0, 255), 5)
    cv2.line(image, (280, 190), (320, 250), (0, 0, 255), 5)
    cv2.line(image, (320, 250), (280, 310), (0, 0, 255), 5)
    cv2.line(image, (280, 310), (220, 310), (0, 0, 255), 5)
    cv2.line(image, (220, 310), (180, 250), (0, 0, 255), 5)
    cv2.line(image, (180, 250), (220, 190), (0, 0, 255), 5)

    cv2.imshow("Black image ", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


imageProcessing()
