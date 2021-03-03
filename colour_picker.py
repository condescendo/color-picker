import cv2
import numpy as np
from PIL import Image

def pix(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        r, g, b = rgbimg.getpixel((x,y))
        txt = str(r) + "," + str(g) + "," + str(b)
        print(txt)
        bg = np.zeros((200,400,3), np.uint8)
        bg[:,0:400] = (b,g,r)
        font = cv2.FONT_ITALIC
        cv2.putText(bg, txt, (10,100), font, 1, (255,255,255), 2, cv2.LINE_AA)
        cv2.imshow("rgb", bg)

print("1. Press 'space bar' to quit \n2.Left Mouse Click + 'c' to capture frame \n3.Double Click on captured image to see colour")
cap = cv2.VideoCapture(0)
while(True):
    ret, img = cap.read()
    frame = cv2.flip(img,1)
    cv2.imshow("feed",frame)
    if cv2.waitKey(1) & 0xFF == ord(" "):
        break

    elif cv2.waitKey(1) & 0xFF == ord("c"):
        cv2.imwrite("1.png", frame)
        image = Image.open("1.png")
        rgbimg = image.convert("RGB")
        cv2.imshow("pic", frame)
        cv2.setMouseCallback("pic", pix)
    
    
 
cap.release()
cv2.destroyAllWindows()
