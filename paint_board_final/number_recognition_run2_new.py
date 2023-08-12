import sys

from PyQt5.QtCore import Qt, QLineF, QObject
from PyQt5.QtGui import QPainter, QPen, QColor

import number_recognition2
from PyQt5.QtWidgets import QWidget, QApplication


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = number_recognition2.Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.clear)
        self.ui.lcdNumber.display(99999)

    def clear(self):
        self.ui.widget.pos_xy = []
        self.ui.lcdNumber.display(99999)
        self.ui.widget.update()

    # def pushButton_clicked


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    app.exec_()
