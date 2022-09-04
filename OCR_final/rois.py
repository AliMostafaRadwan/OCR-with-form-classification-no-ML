import cv2
import numpy as np
import pytesseract
#image_path
img_path="form.png"
#read image
img_raw = cv2.imread(img_path)
img_raw = cv2.resize(img_raw, (0,0), None,0.5,0.5)
#select ROIs function
ROIs = cv2.selectROIs("Select Rois",img_raw)
x,y,h,w = ROIs[0]
#print rectangle points of selected roi
print(ROIs)
#loop over every bounding box save in array "ROIs"
for crop_number, rect in enumerate(ROIs):
	x1=rect[0]
	y1=rect[1]
	x2=rect[2]
	y2=rect[3]
    #crop roi from original image
	img_crop=img_raw[y1:y1+y2,x1:x1+x2]
    #show cropped image
	cv2.imshow(f"crop{str(crop_number)}", img_crop)
#loop over every bounding box and perform OCR on each cropped image
for rect in ROIs:
	x1=rect[0]
	y1=rect[1]
	x2=rect[2]
	y2=rect[3]
    #crop roi from original image
	img_crop=img_raw[y1:y1+y2,x1:x1+x2]
    #perform OCR on cropped image
	text = pytesseract.image_to_string(img_crop)
    #print OCR output
	print(f"ocr result: {text}")

#hold window
cv2.waitKey(0)