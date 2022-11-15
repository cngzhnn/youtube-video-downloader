import sys
from pytube import YouTube
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(420, 140))
        self.setWindowTitle("Youtube Video Downloader")

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Link:')

        self.line = QLineEdit(self)
        self.line.move(80, 20)
        self.line.resize(300, 32)
        self.nameLabel.move(20, 20)

        pybutton = QPushButton('OK', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(300, 32)
        pybutton.move(80, 60)

        self.bittiLabel = QLabel(self)
        self.bittiLabel.setText("İndirildi")
        self.bittiLabel.hide()
        self.bittiLabel.move(205, 100)
        self.bittiLabel.setStyleSheet("QLabel { color : green; }")

    def clickMethod(self):
        print(self.bittiLabel.isVisible())
        self.bittiLabel.hide()

        print('Your name: ' + self.line.text())
        yt = YouTube(self.line.text())
        ys = yt.streams.get_highest_resolution()
        ys.download("C:\\Users\\cngzh\\Desktop")
        self.bittiLabel.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
