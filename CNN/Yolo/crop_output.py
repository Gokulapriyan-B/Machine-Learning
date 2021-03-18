import cv2
import glob
import pandas as pd


images = [cv2.imread(file) for file in glob.glob(r"C:\Users\Gokul\Downloads\test_images\*")]
df = pd.read_json(r"C:\Users\Gokul\Downloads\co-ordinates.json")
for i, img in enumerate(images):
    length = len(df.objects[i])
    for j in range(length):
        y = df.objects[i][j]['relative_coordinates']
        x_c = (y['center_x'])
        y_c = (y['center_y'])
        width = (y['width'])
        height = (y['height'])

        x1 = round((x_c - width/2)*img.shape[1])
        x2 = round((x_c + width/2)*img.shape[1]) + 7

        y1 = round((y_c - height/2)*img.shape[0])
        y2 = round((y_c + height/2)*img.shape[0]) + 7

        roi = img[y1:y2, x1:x2]
        cv2.imwrite(r"C:\Users\Gokul\Downloads\test_images_results\img{}_{}.jpg".format(i+1,j+1), roi)
    print("Done - Image {}".format(i+1))