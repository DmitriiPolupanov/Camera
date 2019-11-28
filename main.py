import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from Ui import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.flag = False
        self.pushButton.clicked.connect(self.clicked)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        if self.flag:
            for i in range(randint(1, 100)):
                qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                self.x = randint(0, 900)
                self.y = randint(0, 500)
                self.r = randint(10, 60)
                qp.drawEllipse(self.x, self.y, self.r, self.r)

    def clicked(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec_())
