import cv2
import numpy as np

# 初始化全局变量
selected_color = None
hsv_min, hsv_max = None, None
colors = {"RED": "red.txt", "GREEN": "green.txt", "PURPLE": "purple.txt", "BLUE": "blue.txt"}

def draw_center_box(frame, box_size=(10, 20)):
    """在帧的中心绘制一个矩形框"""
    height, width, _ = frame.shape
    x1, y1 = width // 2 - box_size[0] // 2, height // 2 - box_size[1] // 2
    x2, y2 = width // 2 + box_size[0] // 2, height // 2 + box_size[1] // 2
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return x1, y1, x2, y2

def extract_hsv_values(frame, box_coords):
    """从框选区域提取 HSV 值"""
    x1, y1, x2, y2 = box_coords
    roi = frame[y1:y2, x1:x2]
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    hsv_values = hsv_roi.reshape(-1, 3)
    return hsv_values

def save_thresholds(hsv_values, color):
    """计算 HSV 最大最小值并保存到文件"""
    global hsv_min, hsv_max
    h_min, s_min, v_min = np.min(hsv_values, axis=0)
    h_max, s_max, v_max = np.max(hsv_values, axis=0)
    hsv_min = (h_min, s_min, v_min)
    hsv_max = (h_max, s_max, v_max)

    # 保存到文件
    with open(colors[color], "w") as f:
        f.write(f"{color.lower()} {h_min} {s_min} {v_min} {h_max} {s_max} {v_max}\n")

    # 输出到控制台
    print(f"[{color}] HSV Thresholds:")
    print(f"Low: {hsv_min}")
    print(f"High: {hsv_max}")
    return hsv_min, hsv_max

def display_preview(frame, hsv_min, hsv_max):
    """在窗口中显示颜色阈值预览"""
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, hsv_min, hsv_max)
    preview = cv2.bitwise_and(frame, frame, mask=mask)
    return preview

def create_menu():
    """创建菜单窗口"""
    menu = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.rectangle(menu, (10, 10), (140, 50), (0, 0, 255), -1)
    cv2.putText(menu, "RED", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.rectangle(menu, (10, 60), (140, 100), (0, 255, 0), -1)
    cv2.putText(menu, "GREEN", (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.rectangle(menu, (10, 110), (140, 150), (128, 0, 128), -1)
    cv2.putText(menu, "PURPLE", (20, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.rectangle(menu, (10, 160), (140, 200), (255, 0, 0), -1)
    cv2.putText(menu, "BLUE", (20, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.rectangle(menu, (10, 220), (140, 260), (255, 255, 255), -1)
    cv2.putText(menu, "Get Color", (20, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    return menu

# 鼠标回调函数
def mouse_callback(event, x, y, flags, param):
    global selected_color
    if event == cv2.EVENT_LBUTTONDOWN:
        if 10 < x < 140:
            if 10 < y < 50:
                selected_color = "RED"
            elif 60 < y < 100:
                selected_color = "GREEN"
            elif 110 < y < 150:
                selected_color = "PURPLE"
            elif 160 < y < 200:
                selected_color = "BLUE"
            elif 220 < y < 260:
                selected_color = "GET_COLOR"

# 主函数
def main():
    global selected_color, hsv_min, hsv_max

    # 打开摄像头
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Camera Output")
    cv2.namedWindow("Menu")
    cv2.setMouseCallback("Menu", mouse_callback)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法读取摄像头输入")
            break

        # 绘制中心框
        box_coords = draw_center_box(frame)

        # 显示菜单
        menu = create_menu()

        # 检测按钮点击
        if selected_color == "GET_COLOR":
            if any([selected_color == key for key in colors.keys()]):
                hsv_values = extract_hsv_values(frame, box_coords)
                hsv_min, hsv_max = save_thresholds(hsv_values, selected_color)

                # 显示 HSV 阈值预览
                preview = display_preview(frame, hsv_min, hsv_max)
                cv2.imshow("Preview", preview)

        # 将菜单和相机输出显示在窗口中
        cv2.imshow("Camera Output", frame)
        cv2.imshow("Menu", menu)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()