# -*-coding:utf-8-*-
# import cv2
# # 方式一
# video = cv2.VideoCapture(0)
# i = 0
# #将视频文件初始化为VideoCapture对象
# # video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
# success, frame = video.read()
# while success and cv2.waitKey(1) & 0xFF != ord('q'):
# #等待1毫秒读取键键盘输入，最后一个字节是键盘的ASCII码。ord()返回字母的ASCII码
#     cv2.imshow('frame', frame)
#     success, frame = video.read()
#     # cv2.imwrite("detect_to_save/"+str(i)+"image.jpg", frame)
# cv2.destroyAllWindows() 
# video.release()

# import cv2
# # import paddleocr
# video = cv2.VideoCapture(0)
# i = 0
# k = waitKey(100)
# success,frame = video.read()
# while success and cv2.waitKey(1) & 0xFF != ord('q'):
#     cv2.imshow('frame',frame)
#     success,frame = video.read()
#     if k == ord('s'):
#         cv2.imwrite("imgs/"+str(i)+"aim_image.jpg",frame)
# cv2.destroyAllWindows()
# video.release()

import cv2
video = cv2.VideoCapture(0)

while 1:
    success , frame = video.read()
    word = cv2.waitKey(1)
    if word  == ord('q'):
        break
    # k = cv2.waitKey(1)
        # if k == ord('s'):    
    elif word == ord('s'):
        cv2.imwrite("imgs/"+str(100)+"aim_image.jpg",frame)
    cv2.imshow('frame',frame)

cv2.destroyAllWindows()
video.release()





