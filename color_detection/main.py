import cv2
from PIL import Image

from utils import get_limits
blue=(255,0,0)
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv_frame=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    lower_limit, upper_limit = get_limits(blue)
    mask=cv2.inRange(hsv_frame,lower_limit,upper_limit)
    mask_=Image.fromarray(mask)
    bboxes=mask_.getbbox()
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    if bboxes:
        x1,y1,x2,y2=bboxes
        frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
        cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
