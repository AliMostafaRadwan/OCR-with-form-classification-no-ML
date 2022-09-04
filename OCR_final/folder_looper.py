#loop over the images folder and print the files names
import os
from OCR_MAIN import ocr
import pandas as pd
Directory = 'images'

for files in os.listdir(Directory):
    # print(files)
    f = os.path.join(Directory, files)
    ocr1 = ocr(f)
    ocr1.img()
    ocr1.FormClassifire()
    ocr1.roi_bbox()
    ocr1.itt()
    ocr1.df()


