from urllib.robotparser import RobotFileParser
import cv2
import pytesseract
from form_classifier import  mse
import numpy as np
from resizer import resizer
import pandas as pd
class ocr:

    def __init__(self,img_path):
        self.img_path = img_path



    #reading the image and resizeing it
    def img(self):
        global img_raw
        global img_raw2
        img_raw = cv2.imread(self.img_path, cv2.IMREAD_UNCHANGED)
        img_raw2 = cv2.imread(self.img_path)
    
        width = 1414
        height = 2000
        dim = (width, height)
        img_raw = cv2.resize(img_raw, dim, interpolation = cv2.INTER_AREA)
        img_raw2 = cv2.resize(img_raw2, (0,0), None,0.5,0.5)
        return img_raw, img_raw2


    def FormClassifire(self):
        original = cv2.imread("comppppp.png") # the indicator don't change it!!!
        global diff
        global form_res
        diff = round(mse(original,img_raw))
        # global img_form
        if diff in np.arange(15850,15900):
            print('form 1 is detected')
            # img_form = resizer('form.png')
        elif diff in np.arange(14900,14950):
            print('form 2 is detected')
            # img_form = resizer('form2.png')
        print(f'MSE: {diff}')
        form_res =  resizer('form.png') if diff in np.arange(15850,15900) else resizer('form2.png')
        return  diff ,form_res


    def roi_bbox(self):
        global name1
        global name2
        global phone1
        global phone2
        if diff in np.arange(15850,15900):
            x_name1,y_name1,w_name1,h_name1 = [47, 487, 297, 52]
            x_phone1,y_phone1,w_phone1,h_phone1 = [369, 486 ,297, 55]
            name1 = form_res[y_name1:y_name1+h_name1, x_name1:x_name1+w_name1]
            phone1 = form_res[y_phone1:y_phone1+h_phone1, x_phone1:x_phone1+w_phone1]
        elif diff in np.arange(14900,14950):
            x_name2,y_name2,w_name2,h_name2 = [47, 487, 297, 52]
            x_phone2,y_phone2,w_phone2,h_phone2 = [369, 486 ,297, 55]
            name2 = form_res[y_name2:y_name2+h_name2, x_name2:x_name2+w_name2]
            phone2 = form_res[y_phone2:y_phone2+h_phone2, x_phone2:x_phone2+w_phone2]
            return name2,phone2
        return phone1,name1


    def itt(self):
        global O_name1
        global O_phone1
        global O_name2
        global O_phone2
        
        if diff in np.arange(15850,15900):
            O_name1 = pytesseract.image_to_string(name1)
            #remove the last char from the string
            
            O_phone1 = pytesseract.image_to_string(phone1)
            print(O_name1)
            print(O_phone1)
        elif diff in np.arange(14900,14950):
            O_name2 = pytesseract.image_to_string(name2)
            O_phone2 = pytesseract.image_to_string(phone2)
            print(O_name2)
            print(O_phone2)
            return O_name2,O_phone2
        return O_name1,O_phone1
        
    def df(self):
        df = pd.DataFrame(columns=['Name','Phone'])
        if diff in np.arange(15850,15900):
            df.loc[0] = [O_name1[:-2],O_phone1[:-2]]
        elif diff in np.arange(14900,14950):
            df.loc[1] = [O_name2[:-2],O_phone2[:-2]]
        with open('output.csv', 'a') as f:
            df.to_csv(f, index=False)
        return df

if __name__ == "__main__":
    user_path_input = str(input('Enter the image path: '))
    ocr1 = ocr(user_path_input)
    ocr1.img()
    ocr1.FormClassifire()
    ocr1.roi_bbox()
    ocr1.itt()
    ocr1.df()