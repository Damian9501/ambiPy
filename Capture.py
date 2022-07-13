import cv2

class Capture:
    def __init__(self):
        self.port = self.getPort()
        if self.port > -1:
            self.cam = cv2.VideoCapture(self.port)
        else:
            raise Exception('No camera input')

    def getPort(self):
        port = -1
        for i in range(0,6):
            testedPort = cv2.VideoCapture(i)
            if testedPort.isOpened():
                is_reading, img = testedPort.read()
                if is_reading:
                    port = i
            if port > -1:
                break
        return port

    def captureImageArray(self):
        result, image = self.cam.read()
        if not result:
            raise Exception('Image not captured')
        return image

    def captureImagePng(self):
        result, image = self.cam.read()
        cv2.imwrite('frame.png', image)

    def previewVideo(self):
        while(True):
            result, image = self.cam.read()
            cv2.imshow('preview (press q to quit)', image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.destroy()

    def destroy(self):
        self.cam.release()
        cv2.destroyAllWindows()



def capture_test():
    capture = Capture()
    capture.captureImagePng()

def video_test():
    capture = Capture()
    capture.previewVideo()

#capture_test()