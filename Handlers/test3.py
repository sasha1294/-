import pyautogui
from database.test4 import *
import cv2
def skrin():

    numbers = cur.execute("""SELECT number FROM Numbers;""")
    n = numbers.fetchall()

    image = pyautogui.screenshot(region=(0,0, n))
    print(image)
    return image

def video():
    numbers = cur.execute("""SELECT number FROM Numbers;""")
    n = numbers.fetchall()

    SCREEN_SIZE = tuple(pyautogui.size())
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    fps = 12.0
    out = cv2.VideoWriter("output.avi", fourcc, fps, (SCREEN_SIZE))
    record_seconds = 10
    print(out)
    return out