import cv2


class Weacom_video(object):
    def __init__(self, src=0):
        self.capture = cv2.VideoCapture(src)
        self.count = 0

    # vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
    # success, image = vidcap.read()
    # count = 0
    # success = True
    # while success:
    #     cv2.imwrite("frame%d.jpg" % count, image)  # save frame as JPEG file
    #     success, image = vidcap.read()
    #     count += 1
    #     vidcap.set(cv2.CAP_PROP_POS_FRAMES, count * 10)
    # def get_shot_video(self):

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

# cap = cv2.VideoCapture('https://cctv1.dreamnet.su:8090/hls/311490/8751c2768bca7321dcd4/playlist.m3u8')
# #if not vcap.isOpened():
# #    print "File Cannot be Opened"
#
# while (True):  # Вывод кадров производится  в цикле
#
#     ret, frame = cap.read()
#     cv2.imshow("frame", frame)  # Метод для визуализации массива кадров
#
# cap.release()
# cv2.destroyAllWindows()

# while(True):
#     # Capture frame-by-frame
#     ret, frame = vcap.read()
#     #print cap.isOpened(), ret
#     if frame is not None:
#         # Display the resulting frame
#         cv2.imshow('frame',frame)
#         # Press q to close the video windows before it ends if you want
#         if cv2.waitKey(22) & 0xFF == ord('q'):
#             break
#     else:
#         print("Frame is None")
#         break
#
# # When everything done, release the capture
# vcap.release()
# cv2.destroyAllWindows()
# print("Video stop")


# class WeacomParser:
#     def __init__(self, url):
#         self.url = url
#
#     def parser_video(self):
#         content = requests.get(self.url)
#         soup = BeautifulSoup(content.text, "html.parser")
#         view_count = soup.find("video", {"class": "vjs-tech"}).text
#         return view_count
#
# url = "https://weacom.ru/cams"
# x = WeacomParser(url)
# x.parser_video_count()
