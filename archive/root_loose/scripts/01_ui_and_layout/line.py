from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        line = QLineEdit(self)
        line.setPlaceholderText("Enter text here")

        #mainlayout = QVBoxLayout()

        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()