# 5 Essential function


import cv2 as cv
img = cv.imread('image/cat_3.png')

cv.imshow("Cat", img)

# We have displayed that image in a new widnow. And Currently, this is a BGR image, a three channel blue, green and red image
# Now there are ways in open CV to essentially convert those BGR images to grayscale so that only see the intensity distribution
# of pixels rather than color itself.

# Converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Blur Image: Now Blurring an image essentially removes some of the noise that exists in an image. For example, in an image, there are may be some extra elements that were there because of bad lighting when the image was taken, or maybe some issues with the camera sensor

# now  we can cv.GaussianBlur(img,(kernel size has to be two odd number),  cv.BORDERDEFAULT)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)


# Edge Casecade: It's basically trying to find the edge that are present in the image. Now again, there are many edge casecade that are available. But for now we are going to be using canny edge ditector which is the very pretty famous in the computer vision world. Esentially, it's multi step process that involves a lot of blurring and then involves a lot of grading computations and stuff like that. We are using cv.Canny(img, threshold1, threshold2)

canny = cv.Canny(img, 125,175)
cv.imshow("Canny", canny)

# we can reduce the edge bluring the image
canny = cv.Canny(blur, 125,175)
cv.imshow("Canny2", canny)

# Now next function we're goint to discuss is how dialate image an image using specific strucreing elements. Now the structuring element that we are going use is actually these edges the canny edge that were found, so, we're say dialating the image

# Dilating the image
dialated = cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dialated", dialated)

# Eroding imge to dialing image to get back to casecade image
eroded = cv.erode(canny, (3,3), iterations=1)
cv.imshow("eroded", eroded)

# Resize and crop the image

# Resize
resized = cv.resize(img,(800,800), cv.INTER_CUBIC)

# Now There are is 
# By Default, there there is an interpolation that occurs in the background, and that is cv.INTER_AREA 
# Now this is the interpolation method that is useful if are shrinking the image to dimension that are smaller than of the original dimensions
# But in some cases, if your are trying to enlarge the image and scale image to much larger dimensions, you will probably use the inter underscore use the the INTER_LINEAR or INTER_CUBIC. cubic slowest among them all. Resulting image is more higer quality than the INTER_AREA or INTER_LINEAR 

cv.imshow("Resized", resized)

# Crop image 
cropped = img[210:287,234:307]
cv.imshow("Cropped",cropped)

cv.waitKey(0)


