"""
QLabel 控件

Text():获取文本
setText():设置文本
setAlignment():设置文本的对齐方式
setBuddy():设置伙伴关系
setIndent():设置文本缩进
selectedText():返回选择的字符
setWordWarp():设置文本是否允许换行

QLabel常用的信号：
1. 当鼠标滑过标签控件时：linkHovered
2. 当鼠标单击标签控件时：linkActivated,这其实是一种超链接实现方式之一

"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是第一个标签</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window, Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        # href="#”,浏览器就会阻止默认的打开新页面的操作，只实现鼠标移上去变小手的效果
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")
        label2.setToolTip("这是一个虚假的超链接")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("E:\PYcharm\pyqt5\src\controls\images\python.jpg"))

        # 如果设置为True，浏览器打开超链接，如果设置为false，则触发槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>python从菜鸟到高手</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个真实的超链接")

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        self.setLayout(vbox)

        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

    def linkHovered(self):
        print("当鼠标滑过标签2时，触发此事件")

    def linkClicked(self):
        print("当鼠标单击标签2时，触发此事件")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ui = QLabelDemo()
    ui.show()
    sys.exit(app.exec_())