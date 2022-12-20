from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint
from ui_file import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.setFixedSize(150, 120)
        self.pushButton.clicked.connect(self.circle)

        self.label = QLabel()
        # Размеры поля где будут появляться окружности
        self.w_h = 650
        canvas = QPixmap(self.w_h, self.w_h)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignCenter)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        # цикл для случайного количества новых окружностей
        for _ in range(randint(1, 5)):
            d = randint(10, 200)
            x, y = [randint(10, self.w_h - d) for _ in range(2)]
        # создаем экземпляр QPainter, передавая холст (self.label.pixmap())
            painter = QPainter(self.label.pixmap())
            pen = QPen()
            pen.setWidth(3)
            pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            painter.setPen(pen)
            painter.drawEllipse(x, y, d, d)
            painter.end()
            self.update()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
