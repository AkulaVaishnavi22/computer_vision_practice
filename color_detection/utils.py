import numpy as np
import cv2

def get_limits(color):
    # Check for White (255,255,255)
    if color == (255, 255, 255) :
        lower_limit = np.array([0, 0, 200], dtype=np.uint8)     # Low color, very bright
        upper_limit = np.array([180, 40, 255], dtype=np.uint8)  # Full hue range
        return lower_limit, upper_limit
        
    # Check for Black (0,0,0)
    elif color == (0, 0, 0) :
        lower_limit = np.array([0, 0, 0], dtype=np.uint8)       # Complete darkness
        upper_limit = np.array([180, 255, 50], dtype=np.uint8)  # Up to very dark gray
        return lower_limit, upper_limit

    # Standard logic for all normal colors (Blue, Red, Green, Yellow, etc.)
    c = np.uint8([[color]])
    hsv_color = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsv_color[0][0][0]
    
    lower_limit = np.array([max(0, hue - 10), 100, 100], dtype=np.uint8)
    upper_limit = np.array([min(180, hue + 10), 255, 255], dtype=np.uint8)
    
    return lower_limit, upper_limit
