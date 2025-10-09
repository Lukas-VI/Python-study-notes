#Color_auto_get
import cv2
import numpy as np

# 颜色选项
color_options = ['RED', 'GREEN', 'PURPLE', 'BLUE', 'BROWN', 'WHITE', 'BLACK']
thresholds = {}  # 存储颜色阈值

# 全局变量
current_color_index = 0
button_pressed = False
REC_W = 100
REC_H = 25

def mouse_callback(event, x, y, flags, param):
    global button_pressed
    frame_width, frame_height = param
    # 检查是否在按钮区域内（右下角100x50的区域）
    if event == cv2.EVENT_LBUTTONDOWN:
        if x > frame_width - 100 and y > frame_height - 50:
            button_pressed = True

def color_trackbar_callback(value):
    global current_color_index
    current_color_index = value

def main():
    global button_pressed
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    # 获取摄像头帧的尺寸
    ret, frame = cap.read()
    if not ret:
        return
    frame_height, frame_width = frame.shape[:2]
    cap.release()

    # 创建窗口
    cv2.namedWindow('Camera')
    # 创建颜色选择trackbar
    cv2.createTrackbar('Color', 'Camera', 0, len(color_options)-1, color_trackbar_callback)
    # 设置鼠标回调
    cv2.setMouseCallback('Camera', mouse_callback, (frame_width, frame_height))

    # 创建颜色预览窗口
    preview = np.zeros((50, 200, 3), np.uint8)
    cv2.namedWindow('Color Preview')

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)  # 镜像翻转
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 计算中心区域
        center_x, center_y = frame_width // 2, frame_height // 2
        top_left = (center_x - REC_W, center_y - REC_H)
        bottom_right = (center_x + REC_W, center_y + REC_H)

        # 绘制中心区域
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

        # 绘制取色按钮区域
        cv2.rectangle(frame, (frame_width - 100, frame_height - 50), (frame_width, frame_height), (0, 0, 255), -1)
        cv2.putText(frame, 'Capture', (frame_width - 80, frame_height - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        # 显示当前选择的颜色
        current_color_name = color_options[current_color_index]
        cv2.putText(frame, f'Color: {current_color_name}', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        # 检查是否点击了取色按钮
        if button_pressed:
            # 提取中心区域的HSV值
            roi_hsv = hsv[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
            # 分离通道
            H, S, V = cv2.split(roi_hsv)
            minH, maxH = H.min(), H.max()
            minS, maxS = S.min(), S.max()
            minV, maxV = V.min(), V.max()
            # 保存到字典
            thresholds[current_color_name] = [minH, minS, minV, maxH, maxS, maxV]
            # 打印到控制台
            print(f"{current_color_name} {minH} {minS} {minV} {maxH} {maxS} {maxV}")
            # 保存到文件
            with open('thresholds.txt', 'w') as f:
                for color, vals in thresholds.items():
                    f.write(f"{color} {' '.join(map(str, vals))}\n")
            # 更新颜色预览
            lower_hsv = np.array([minH, minS, minV], dtype=np.uint8)
            upper_hsv = np.array([maxH, maxS, maxV], dtype=np.uint8)
            lower_bgr = cv2.cvtColor(lower_hsv.reshape(1,1,3), cv2.COLOR_HSV2BGR).reshape(3,)
            upper_bgr = cv2.cvtColor(upper_hsv.reshape(1,1,3), cv2.COLOR_HSV2BGR).reshape(3,)
            # 绘制预览
            preview[:] = (0, 0, 0)  # 黑色背景
            cv2.rectangle(preview, (0, 0), (100, 50), (int(lower_bgr[0]), int(lower_bgr[1]), int(lower_bgr[2])), -1)
            cv2.rectangle(preview, (100, 0), (200, 50), (int(upper_bgr[0]), int(upper_bgr[1]), int(upper_bgr[2])), -1)
            cv2.imshow('Color Preview', preview)
            button_pressed = False  # 重置按钮状态

        # 显示帧
        cv2.imshow('Camera', frame)

        # 退出键
        key = cv2.waitKey(1)
        if key == 27:  # ESC键退出
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()