from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
import sys
import random

SCREEN_SIZE = [400, 450]
FIGURES = ['circle']
COLORS = ['yellow']


class Example(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False
        self.btn = QPushButton(self)
        self.btn.clicked.connect(self.draw)

    def initUI(self):
        uic.loadUi('UI.ui', self)

    # рисование фигур
    def draw(self):
        self.figure = random.choice(FIGURES)
        print(self.figure)
        self.size = random.randint(10, 100)
        self.color = random.choice(COLORS)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(self.color))
            qp.setBrush(QColor(self.color))
            self.x, self.y = random.randint(100, SCREEN_SIZE[0] - 100), random.randint(100, SCREEN_SIZE[1] - 100)
            if self.figure == 'circle':
                qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Example()
    ex.show()
    sys.exit(app.exec_())