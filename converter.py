import cv2
import numpy as np
import os

def convert2cartoon(path2img):
    img = cv2.imread(path2img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def save_image(image, path2out):
    # Using cv2.imwrite() method 
    # Saving the image 
    cv2.imwrite(path2out, image)
    return 
    
def show_image(image):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

if __name__ == '__main__':
    my_input_dir = '/home/alaman/codes/pic-converter/resources/source_images/'
    my_output_dir = '/home/alaman/codes/pic-converter/resources/outs/'
    my_img = 'cat.jpeg'

    path2img = os.path.join(my_input_dir, my_img)
    path2out = os.path.join(my_output_dir, f'converted_{my_img}')

    cartoon = convert2cartoon(path2img)
    save_image(cartoon, path2out)
