import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QLabel
from PIL import Image
from PyQt5.QtGui import QPainter, QColor
from тык import Ui_MainWindow


def resize(size):
    im = Image.open('round.png')
    im2 = im.resize((size, size))
    im2.save('round_new.png')


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            # Создаем объект QPainter для рисования
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw(qp)
            # Завершаем рисование
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self, qp):
        # Задаем кисть
        col1, col2, col3 = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        qp.setBrush(QColor(col1, col2, col3))
        # Рисуем прямоугольник заданной кистью
        x = random.randint(20, 100)
        cx, cy = random.randint(0, 250), random.randint(0, 250)
        qp.drawEllipse(cx, cy, x, x)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())