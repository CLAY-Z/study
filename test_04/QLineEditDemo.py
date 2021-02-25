"""

QLineEdit综合案例

"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator, QDoubleValidator
import sys


class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('编辑框综合案例')

        # 各种检验器
        edit_1 = QLineEdit(self)
        edit_1.setValidator(QIntValidator())
        edit_1.setMaxLength(3)
        edit_1.setFont(QFont('隶书', 12))

        edit_2 = QLineEdit(self)
        edit_2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        # 掩码
        edit_3 = QLineEdit(self)
        edit_3.setInputMask('999.99.99;_')

        # 文本变化
        edit_4 = QLineEdit(self)
        edit_4.textChanged.connect(self.textchanged)

        # 回显
        edit_5 = QLineEdit(self)
        edit_5.setEchoMode(QLineEdit.Password)
        edit_5.editingFinished.connect(self.enterpress)

        # 只读
        edit_6 = QLineEdit('hello pyqt5')
        edit_6.setReadOnly(True)

        # 表单布局
        formlayout = QFormLayout()
        formlayout.addRow('整数校验：', edit_1)
        formlayout.addRow('浮点数校验：', edit_2)
        formlayout.addRow('数字掩码：', edit_3)
        formlayout.addRow('文本变化：', edit_4)
        formlayout.addRow('密码回显：', edit_5)
        formlayout.addRow('只读模式：', edit_6)

        self.setLayout(formlayout)

    def textchanged(self, text):
        print('the text is: ' + text)

    def enterpress(self):
        print('已输入值')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditDemo()
    main.show()

    sys.exit(app.exec_())