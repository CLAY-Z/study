"""

限制QLineEdit控件的输入（校验器）

如限制只能输入整数、浮点数或者满足一定条件的字符串

"""

import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QFormLayout, QWidget
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('编辑框校验器')

        # 生成一个表单布局
        formLayout = QFormLayout()

        # 生成三个编辑框
        intLineEdit = QLineEdit(self)
        doubleLineEdit = QLineEdit(self)
        validatorLineEdit = QLineEdit(self)

        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('浮点数类型', doubleLineEdit)
        formLayout.addRow('数字和字母', validatorLineEdit)

        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('数字和字母')

        self.setLayout(formLayout)

        # 生成校验器
        intvalidator = QIntValidator(self)
        intvalidator.setRange(0, 99)

        doublevalidator = QDoubleValidator(self)
        doublevalidator.setRange(-360, 360, 2)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation)

        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(reg)

        # 添加校验器至编辑框
        intLineEdit.setValidator(intvalidator)
        doubleLineEdit.setValidator(doublevalidator)
        validatorLineEdit.setValidator(validator)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()

    sys.exit(app.exec_())