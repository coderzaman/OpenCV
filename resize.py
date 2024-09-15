import cv2 as cv

def resize_frame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimessions = (width, height)

    return cv.resize(frame, dimessions, interpolation=cv.INTER_AREA)



img = cv.imread('image/cat_3.png')
res_img = resize_frame(img, .30)

cv.imshow('CAT', img)
cv.imshow('CAT Resize', res_img)

cv.waitKey(0)
cv.destroyAllWindows()


# Resizing Video 
capture = cv.VideoCapture('video/cat_2.mp4')

while True:
    isTrue, frame = capture.read()
    
    
    if not isTrue or frame is None:
        break

    if frame.shape[0] > 0 and frame.shape[1] > 0:
        cv.imshow('Cat', frame)
    resize_video = resize_frame(frame, 0.30)
    cv.imshow('Cat Resize', resize_video)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

    
    
   
    