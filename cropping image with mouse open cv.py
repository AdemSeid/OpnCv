import cv2

# Load the image
image = cv2.imread('image.jpg')

# Display the image and wait for user to select the crop region
clone = image.copy()
cv2.namedWindow('image')
cv2.imshow('image', image)
rect = cv2.selectROI('image', clone, fromCenter=False, showCrosshair=True)
cv2.destroyAllWindows()

# Crop the image using slicing
x, y, w, h = rect
crop = image[y:y+h, x:x+w]

# Save the cropped image
cv2.imwrite('cropped.jpg', crop)
