# import cv2 as cv
# img = cv.imread('image/cat_3.png')
# cv.imshow('Cat_2', img)
# cv.waitKey(0)  # Use 'waitKey' with an uppercase 'K'

# import cv2 as cv 

# img = cv.imread('image/cat_3.png')
# cv.imshow('Cat_3', img) 
# cv.waitKey(0)

# # Close the display window when a key is pressed
# cv.destroyAllWindows()


# import cv2 as c
# img = c.imread('image/cat_3.png')
# c.imshow('Cat_3', img)
# c.waitKey(0)
# c.destroyAllWindows()


import cv2 as cv
#cv imread() method takes in a path o an image and returns that image as matrix pixels
# img = cv.imread('image/cat_3.png')

#We can display the image cv.imshow() method First parameter is name of the window and second parameter is matrix of pixels(image)
# cv.imshow('Cat_3', img)

#cv.waitKey(0) is a keyword binding function wait for a specific delay, or time milliseconds for a key to be pressed
# so if you pass in 0, it basically waits for an infinite amount of time for a keyboard key to be pressed
# cv.waitKey(0)

# If we read a image greater than my coumputer screen  it get out some part out of screen. Now currently openCV doesn't have
# inbuilt way of dealing with images that are larger than coumputer screen


# Reading Video
# cv.VideoCapture method either takes an integer arguments like 0123,etc, or path to a video file
# Now you would provide and integer arguments like 0,1,2, and three, if your are using webcam or camera that is connected to your computer
# In most cases, your webcam would be reffered by using the integer zero. But if you have multiple cameras connected to your computer, you can 
# reference by using the appropiate argument.

# capture = cv.VideoCapture('video/baby_1.mp4')

# Now here's where reading videoes is kind of like different from reading images. 
# In the case reading videos we can use while loop read video frame by frame

# capture.read() basically reads in this video frame by frame 
# Here we use to variable for read frame isTrue received a Boolean value read the frame sucessfully or not
# and frame receive the frame of video 
# then we can show video frame by frame imshow
# we need to break the loop after few frames

# The line `cv.waitKey(20) & 0xFF == ord('d')` is used to check for keyboard input in OpenCV. Here’s a breakdown:

# - `cv.waitKey(20)`: This function waits for a key event for 20 milliseconds. It returns a 32-bit integer corresponding to the key pressed.

# - `& 0xFF`: This bitwise AND operation ensures that only the lower 8 bits of the result are considered. This is done because `cv.waitKey()` returns a 32-bit integer, but only the lower 8 bits are relevant for key detection.

# - `ord('d')`: This gets the ASCII value of the character 'd'. 

# So, `cv.waitKey(20) & 0xFF == ord('d')` checks if the key pressed within the 20-millisecond window is 'd'. If it is, `cv.waitKey(20) & 0xFF == ord('d')` evaluates to `True`, and the loop breaks, stopping the video capture and closing the window.


# while True:
#     isTrue, frame = capture.read()
    
    # Check if frame is successfully captured
    # if not isTrue or frame is None:
    #     break

    # Ensure the frame has valid dimensions
    # if frame.shape[0] > 0 and frame.shape[1] > 0:
    #     cv.imshow('Baby', frame)
    # else:
    #     break

    # if cv.waitKey(20) & 0xFF == ord('d'):
    #     break

# After the loop ends, release the video and close windows

# after reading the we need release the video
# capture.release(): Releases the video capture resource.
# cv.destroyAllWindows(): Closes any OpenCV windows that were opened.
# Both are important for proper cleanup of resources and to ensure your program exits cleanly.

# capture.release()
# cv.destroyAllWindows()

# Resize and Rescaling. We can resize and rescale video file and images to prevent computational starin.
# Large media files tend to store a lot of information in it and displaying it takes up a lot processing needs that your computer needs to assign.
# So by resizing and rescaling trying to get rid of some that information. Rescaling video implies modifying its height and width to a particular height and
# width. Generally It's best practice to downscale or change the width and height of your video files to a smaller value than the original diemension. The reason for this is because while most cameras your webcam included, do not support going higher than it maximum capability.
# So for example, if a camera shoots 720 p, chances are it's not going to be able to shoot in 1080 p or higher. 

# So to rescale a video frame or an image, we can create a function called defrescaleframe. 

img = cv.imread('image/cat_3.png')
cv.imshow('cat_3.png', img)
cv.waitKey(0)
cv.destroyAllWindows()