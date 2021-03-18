import os
from PIL import Image

f = r"E:\Deep learning\Data\ISO certificate"
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((1200,1724))
    img.save(f_img)
print('done')