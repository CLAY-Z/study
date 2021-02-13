# 显示控件提示信息

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QToolTip, QPushButton, QHBoxLayout
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('仿宋', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setGeometry(600, 600, 500, 500)
        self.setWindowTitle('设置控件提示信息')

        self.button = QPushButton('按钮')
        self.button.setToolTip('这是按钮提示信息')

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())