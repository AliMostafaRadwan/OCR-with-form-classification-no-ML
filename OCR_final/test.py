import cv2
import  json
import pytesseract
img = cv2.imread('form.png')
# form1_name = cv2.selectROI('',img)
# output = img[48:486, 297:52]

scale=0.5

    #read image
img_raw = img
img_raw = cv2.resize(img_raw, (0,0), None,scale,scale)
    #select ROI function
x_name1,y_name1,w_name1,h_name1 = [47, 487, 297, 52]#.5
x_phone1,y_phone1,w_phone1,h_phone1 = [369, 486 ,297, 55] #.5
#run ocr on cropped image
name1 = pytesseract.image_to_string(img_raw[y_name1:y_name1+h_name1, x_name1:x_name1+w_name1])
phone1 = pytesseract.image_to_string(img_raw[y_phone1:y_phone1+h_phone1, x_phone1:x_phone1+w_phone1])
print(name1)
print(phone1)

#show the image with bounding box
cv2.rectangle(img_raw,(x_name1,y_name1),(x_name1+w_name1,y_name1+h_name1),(0,255,0),2)
cv2.rectangle(img_raw,(x_phone1,y_phone1),(x_phone1+w_phone1,y_phone1+h_phone1),(0,255,0),2)
cv2.imshow('img',img_raw)
cv2.waitKey(0)
cv2.destroyAllWindows()

