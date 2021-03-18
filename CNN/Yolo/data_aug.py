import albumentations as A
import cv2
import glob

# initialize augmentations
bright_contrast = A.RandomBrightnessContrast(p=1) # random brightness and contrast
clahe = A.CLAHE(p=1) # CLAHE
blur = A.Blur(p=0)

# apply augmentations
# pass image to the augmentation
def aug(img):
    img_plain = blur(image = img)
    img_bc = bright_contrast(image = img)
    img_clahe = clahe(image = img)
    return img_plain, img_bc, img_clahe

images = [cv2.imread(file) for file in glob.glob("E:\Deep learning\Data\ISO certificate new\*")]
aug_images = [aug(img) for img in images]
final_images = [item for sublist in aug_images for item in sublist]

for i,img in enumerate(final_images):
    cv2.imwrite('E:\Deep learning\Data\ISO certificate processed new\img_%3d.jpg'%(1+i), img['image'])
    print('Img %3d Done'%(1+i))