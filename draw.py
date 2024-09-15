# Drawing Shape and Putting Text
import cv2 as cv
import numpy as np

# There two ways to draw on images. Drawing on standalone images is like image of a cat or we create dummy images
# We can create blank images by np.zeros((width, height,no of color channel), dtype='uint8')
# uint8 is image data type. Data types of an image
blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow("Blank Image", blank)

#image the paint certain color
# [:] this means reference all the pixels of image
# blank[:] = 0,255,0
# cv.imshow("Green Image", blank)

# blank[0:100, 0:100] = 255,255,255
# cv.imshow("Green Image", blank)


# blank[400:500, 0:100] = 255,255,255
# cv.imshow("Green Image", blank)

# blank[0:100, 400:500] = 255,255,255
# cv.imshow("Green Image", blank)

# blank[400:500, 400:500] = 255,255,255
# cv.imshow("Green Image", blank)
# we can also color certain protion of image 

# We can Draw Rectangle with cv.rectangle() function
# cv.rectangle(blank,(100,200),(400,400),(244,222,233), thickness=2)

# If we wnat filled the rectangle with color cv.FILLED or -1 instead of thickness parameter
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(244,222,123), cv.FILLED)
cv.imshow("Rectangle", blank)

# Draw a circle with cv.circle() function
cv.circle(blank,(250,250),50,(0,0,255),-1)
cv.imshow("Circle", blank)

# Draw a line with cv.line() function
cv.line(blank,(0,0),(255,255),(255,255,255),thickness=4)
cv.imshow("Line", blank)

# Write text on image with cv.putText() function
cv.putText(blank,"Bismillahir Rahmanir Rahim",(40,20),cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)
cv.destroyAllWindows()