# python program to loop over the images in img folder and save a greyscale copy

import cv2
from os import walk

mypath = './img/'
list_of_images = []
for (dirpath, dirnames, filenames) in walk(mypath):
    list_of_images.extend(filenames)
    break

print(list_of_images)

# verify installation & import
print(cv2.__version__)

counter = 1

for image_name in list_of_images:
    image = cv2.imread(mypath+image_name, 0)

    # show the image
    cv2.imshow('PyImage',image)

    # Do not close the image window immediate but wait till the user closes it.
    key_hit = cv2.waitKey(1000)      # in milliseconds - 0: wait forever

    cv2.imwrite(mypath + 'grayscale/' + image_name + '-copy-.png', image)
    
# Exit gracefully - clear memory
cv2.destroyAllWindows()