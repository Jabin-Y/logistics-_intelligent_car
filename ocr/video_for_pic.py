# -*-coding:utf-8-*-
__author__ = 'Code->Y'

from paddleocr import com_interaction
import cv2
import _thread
import time
import communication
import PosDetect

save_flag = False
image_path_2021 = "pic_to_detect/aim_pic.jpg"
my_serial = communication.serialinit_move() #获取串口
def start_camera_all(threadName,delay):
    print("拍摄中------------------------")
    video = cv2.VideoCapture(0)
    success, frame = video.read()
    while success and cv2.waitKey(1) & 0xFF != ord('q'):
        # 等待1毫秒读取键键盘输入，最后一个字节是键盘的ASCII码。ord()返回字母的ASCII码
        # cv2.imshow('frame', frame)
        success, frame = video.read()
        global save_flag
        if save_flag == True:
            cv2.imwrite("pic_to_detect/aim_pic.jpg", frame)
            print("保存图片")
            save_flag = False
    video.release()

def work():
    global save_flag
    communication.work_forward_move(my_serial)
    # is_aim = com_interaction()
    if PosDetect.RET_depth() <= 85:
        save_flag = True
        if com_interaction(image_path_2021):
            communication.work_stop(my_serial)
            communication.put_down_arm(my_serial)
            communication.work_back_move(my_serial)
            communication.work_right_move(my_serial)
            communication.work_forward_move(my_serial)
        else:
            print("WARM:检测到目标未识别到文字信息！")
    



if __name__ == '__main__':
    time.sleep(10)
    try:
        _thread.start_new_thread(start_camera_all,('thread1',1))
        work()
    except:
        print("ERROR:启动失败")
    while(1):
        pass
