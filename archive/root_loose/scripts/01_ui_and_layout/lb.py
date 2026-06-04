from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        lb=QLabel("Hello World",self)
        lb.setText("funny")
        lb.setAlignment(Qt.AlignmentFlag.AlignCenter)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()