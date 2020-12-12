import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    #images, videos and live stream
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #live stream
    capture.set(3, width)
    capture.set(4, height)



capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()    
    cv.imshow('Video', rescaleFrame(frame, .2))
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
