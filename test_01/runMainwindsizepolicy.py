import sys
from mainwindsizepolicy import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()

    ui = Ui_MainWindow()
    # 向主窗口中添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()

    sys.exit(app.exec_())