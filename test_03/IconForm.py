import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
"""
窗口的setWindowIcon方法用于设置窗口的图标，只在Windows中可用

QApplication中的setWindowIcon方法用于设置主窗口和应用程序的图标，但如果调用了窗口的setWindowIcon方法
QApplication中的setWindowIcon方法只能用于设置应用程序的图标
"""

class IconForm(QMainWindow):
    def __init__(self, parent=None):
        super(IconForm, self).__init__(parent)

        self.initUI()

    def initUI(self):

        # 设置窗口大小和位置
        self.setGeometry(300, 300, 500, 250)
        # 设置主窗口的标题
        self.setWindowTitle("设置窗口图标")

        self.setWindowIcon(QIcon('E:\PYcharm\pyqt5\src\controls\images\Banshee.ico'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('E:\PYcharm\pyqt5\src\controls\images\Banshee.ico'))

    ui = IconForm()
    ui.show()
    sys.exit(app.exec_())


