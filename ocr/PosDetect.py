import pyrealsense2 as rs
import numpy as np
import cv2
import math
import time
# Configure depth and color streams

class targetPoint:
    def __init__(self):
        # 默认相机中心,直行
        self.x = 320
        self.y = 240
        self.depth = 0


    def update(self, nx, ny):
        self.x = nx
        self.y = ny


def cnt_area(cnt):
    area = cv2.contourArea(cnt)
    return area

def RET_deviation_coordinate():
    return target.x - 320,target.y - 240

def RET_depth():
    return target.depth

def get_dis():
    try:
        # Start streaming
        pipeline.start(config)
        while True :
            # Wait for a coherent pair of frames: depth and color
            frames = pipeline.wait_for_frames()
            depth_frame = frames.get_depth_frame()
            color_frame = frames.get_color_frame()
            if not depth_frame or not color_frame:
                continue

            # Convert images to numpy arrays
            depth_image = np.asanyarray(depth_frame.get_data())
            color_image = np.asanyarray(color_frame.get_data())
            color_image = cv2.blur(color_image,(5,5))



            hsv =  cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
            lower = np.array([11, 43, 46])  # 所要检测的像素范围11,67,70
            upper = np.array([25, 255, 255])  # 此处检测绿色区域44,255,114

            mask = cv2.inRange(hsv, lowerb=lower, upperb=upper)
            ret, binary = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)
            kernel = np.ones((9, 9), np.uint8)
            binary = cv2.dilate(binary,kernel,1)
            contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            if len(contours) > 0:
                contours.sort(key=cnt_area, reverse=True)
                cnt = contours[0]
                if cv2.contourArea(cnt) >150:
                    x, y, w, h = cv2.boundingRect(cnt)
                    center_x = int((x+ w/2))
                    center_y = int(y+ h/2)
                    if center_x > 479:  # 超出会报错
                        center_x = 479
                    target.update(center_x,center_y)
                    print(RET_deviation_coordinate())

                    cv2.circle(color_image, (center_x, center_y), 8, [255, 0, 255], thickness=-1)
                    cv2.drawContours(color_image, [cnt], -1, (0, 0, 255), 3)
                    cv2.putText(color_image, "Distance/cm:" + str(depth_image[center_x, center_y]), (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, [255, 0, 255])
                    target.depth = depth_image[center_x, center_y]
                    # print(center_x,center_y,str(depth_image[center_x, center_y]/10))
            # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
            depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

            # Stack both images horizontally
            images = np.hstack((color_image, depth_colormap))
            imgtest = np.hstack((mask,binary))
            # Show images
            cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
            cv2.imshow('RealSense', images)
            cv2.imshow('img',imgtest)

            key = cv2.waitKey(1)
            # Press esc or 'q' to close the image window
            if key & 0xFF == ord('q') or key == 27:
                cv2.destroyAllWindows()
                break
            elif key == ord('s'):
                cv2.imwrite('save.jpg',color_image)



    finally:
        print('stop get dis')
        # Stop streaming
        pipeline.stop()

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
target = targetPoint()

    # get_dis()
    # time.sleep(5)
    # get_dis()
