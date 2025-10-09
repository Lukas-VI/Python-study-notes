
import os

desktop_path = r"d:\Users\lupo\OneDrive\桌面"
shortcut_name = "Minecraft.lnk"
shortcut_path = os.path.join(desktop_path,shortcut_name)

try:
    os.startfile(shortcut_path)
    print("langched")
    os.system("pause")
except FileNotFoundError:
    print("file not found")
    os.system("pause")