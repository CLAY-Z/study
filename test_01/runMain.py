import sys
from test_01 import Ui_MainWindow1
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()

    ui = Ui_MainWindow1()
    # 向主窗口中添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()

    sys.exit(app.exec_())