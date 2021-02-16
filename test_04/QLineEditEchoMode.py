"""

QLineEdit控件与回显模式

基本功能：输入单行文本

EchoMode(回显模式)

4种回显模式

1. Normal
2. NoEcho
3. Password
4. PasswordEchoOnEdit

"""

import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout

class QLineEditEchoMode(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("文本输入框的回显模式")

        normalLineEdit = QLineEdit(self)
        noEchoLineEdit = QLineEdit(self)
        passwordLineEdit = QLineEdit(self)
        passwdEchoOnEdit = QLineEdit(self)

        # 表单布局
        formLayout = QFormLayout(self)
        formLayout.addRow('normal:', normalLineEdit)
        formLayout.addRow('noEchor:', noEchoLineEdit)
        formLayout.addRow('password:', passwordLineEdit)
        formLayout.addRow('passwdEchoOnEdit:', passwdEchoOnEdit)
        self.setLayout(formLayout)

        # 设置模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwdEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 设置placeholdertext
        normalLineEdit.setPlaceholderText("normal")
        noEchoLineEdit.setPlaceholderText("noEcho")
        passwordLineEdit.setPlaceholderText("password")
        passwdEchoOnEdit.setPlaceholderText("passwdEchoOnEdit")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()

    sys.exit(app.exec_())