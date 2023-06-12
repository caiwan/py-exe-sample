import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sample Qt App")
        self.setGeometry(100, 100, 300, 200)
        self.label = QLabel("Hello, Qt!", self)
        self.label.setGeometry(100, 100, 100, 30)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
