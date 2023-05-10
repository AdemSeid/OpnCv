import cv2 as cv
import os

# Path to the folder containing the images to be cropped
input_folder = 'D:/fin yr/cropping/train'

# Path to the folder where the cropped images will be saved
output_folder = 'D:/fin yr/cropping/train cropped'

# Loop through all the files in the input folder
for filename in os.listdir(input_folder):

    # Read the input image
    img = cv.imread(os.path.join(input_folder, filename))

    # Crop the image
    cropped = img[400:1546, 600:3850] #you can chage it as your requirement

    # Save the cropped image to the output folder with the same filename
    cv.imwrite(os.path.join(output_folder, filename), cropped)




'''bellow code is used for an image'''
##import cv2 as cv
##img = cv.imread('uncropped.jpg')
##print(img.shape)

##cropped = img[400:1546,600:3850]
##
##cv.imshow('cropped', cropped)
##cv.imwrite('crp2.jpg', cropped)
##cv.waitKey(0)
##cv.destroyAllWindows()
