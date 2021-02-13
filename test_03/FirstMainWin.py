import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):

        '''
        子类实例化后只会调用自己的构造函数，不会去调用父类的构造函数，也就不会继承父类构造函数中的成员属性，
        但可以继承其中的类变量，除非子类没有重写构造函数。如果需要强制调用父类构造函数，可以使用super函数，
        super(cls, obj)函数返回绑定超类的一个实例,obj必须是cls类型的实例，super的作用就是间接调用父类的
        覆盖方法，不局限于构造函数！然后用返回的父类实例执行父类__init__函数即可。
        '''
        super(FirstMainWin, self).__init__(parent)

        # 设置主窗口的标题
        self.setWindowTitle("第一个主窗口应用")

        # 设置窗口的尺寸
        self.resize(400, 300)

        # statusBar()是QMainWindow的一个成员函数，返回一个状态栏类的对象
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒时间', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('E:\PYcharm\pyqt5\src\controls\images\Banshee.ico'))

    ui = FirstMainWin()
    ui.show()
    sys.exit(app.exec_())


