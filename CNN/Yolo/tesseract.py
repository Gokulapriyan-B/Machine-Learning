import pytesseract
import glob
import cv2
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
images = [cv2.imread(file) for file in glob.glob(r"C:\Users\Gokul\Downloads\test_images_results\*")]
gray_images = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) for img in images]
final_images = [cv2.threshold(img, 0,255,cv2.THRESH_BINARY| cv2.THRESH_OTSU)[1] for img in gray_images]
text = [pytesseract.image_to_string(img) for img in images]

no_classes = 4
name = []
cert = []
issue = []
expiry = []
for i in range(len(text)//no_classes):
    name.append(text[i*4+3][:-2].replace('\n', ' '))
    cert.append(text[i*4+2][:-2])
    issue.append(text[i*4+1][:-2])
    expiry.append(text[i*4+0][:-2])

dict = {'Company Name': name, 'Certificate No': cert, 'Issue Date': issue, 'Expiry Date': expiry}
df = pd.DataFrame(dict)
df.to_csv('output.csv')