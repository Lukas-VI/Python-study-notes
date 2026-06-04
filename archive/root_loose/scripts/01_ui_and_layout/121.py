from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Hello World", self)
        btn.setGeometry(0, 0, 100, 50)
        btn.setToolTip("This is a tooltip")
        btn.setText("Click me")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()