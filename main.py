import cv2


class Weacom_video(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.count = 0


    def show_frame(self):
        # Display frames in main program
        # if self.status:
        #     cv2.imshow('Weacom', cv2.resize(self.capture.read(), (600, 350)))
        # key = cv2.waitKey(1)
        # if key == ord('s'):
        #     self.capture.release()
        #     cv2.destroyAllWindows()
        #     exit(1)
        ret, frame = self.capture.read()
        cv2.imwrite("frame%d.jpg" % self.count, frame)  # save frame as JPEG file
        self.count += 1
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.count)
        cv2.imshow('Weacom', cv2.resize(frame, (600, 350)))

        key = cv2.waitKey(1)
        if key == ord('s'):
            self.capture.release()
            cv2.destroyAllWindows()
            exit(1)


if __name__ == '__main__':
    video_stream_widget = Weacom_video('https://cctv1.dreamnet.su:8090/hls/311490/8751c2768bca7321dcd4/playlist.m3u8')
    while True:
        try:
            video_stream_widget.show_frame()
        except AttributeError:
            pass

