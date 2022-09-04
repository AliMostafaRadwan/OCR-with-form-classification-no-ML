import cv2

def resizer(img):
    img_raw = cv2.imread(img)
    img_raw2 =  cv2.resize(img_raw, (0,0), None,0.5,0.5)
    return  img_raw2