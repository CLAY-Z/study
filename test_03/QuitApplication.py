import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget
from PyQt5.QtGui import QIcon


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()

        self.setWindowTitle('退出应用程序')
        self.resize(600, 400)

        self.button = QPushButton('退出应用程序')
        self.button.clicked.connect(self.onClicked_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        # Qwidget相比于Qmainwindow没有布局，相当于一个没有布局的窗口
        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        # 使用一个窗口或控件来填充主窗口的中心区域
        self.setCentralWidget(mainFrame)



    def onClicked_Button(self):

        # sender函数用于返回发送这个信号来源的对象指针，即是哪个控件发送信号给这个槽函数
        sender = self.sender()
        print(sender.text() + ' 按钮被按下，程序即将退出')

        # 退出应用程序
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())

