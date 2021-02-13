import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


def onClicked_Button():

    # 窗口左上角坐标和工作区尺寸
    print('1')
    print('widget.x() = %d' % widget.x())
    print('widget.y() = %d' % widget.y())
    print('widget.width() = %d' % widget.width())
    print('widget.height() = %d' % widget.height())

    # 工作区左上角坐标和工作区尺寸
    print('2')
    print('widget.geometry().x() = %d' % widget.geometry().x())
    print('widget.geometry().y() = %d' % widget.geometry().y())
    print('widget.geometry().width() = %d' % widget.geometry().width())
    print('widget.geometry().height() = %d' % widget.geometry().height())

    # 窗口左上角坐标和窗口尺寸
    print('3')
    print('widget.frameGeometry().x() = %d' % widget.frameGeometry().x())
    print('widget.frameGeometry()).y() = %d' % widget.frameGeometry().y())
    print('widget.frameGeometry().width() = %d' % widget.frameGeometry().width())
    print('widget.frameGeometry().height() = %d' % widget.frameGeometry().height())


app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText('按钮')
btn.move(50, 60)

btn.clicked.connect(onClicked_Button)

widget.resize(500, 600)  # 设置工作区的尺寸
widget.move(250, 300)    # 设置整个窗口的坐标

widget.setWindowTitle('屏幕坐标系')
widget.show()

sys.exit(app.exec_())