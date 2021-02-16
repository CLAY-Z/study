"""

QLabel与伙伴关系

知识点：Dialog类型窗口、栅格布局、伙伴关系设置

"""
import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QLabel与伙伴关系")

        nameLabel = QLabel('&Name:', self)
        nameLineEdit = QLineEdit(self)
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password:', self)
        passwordLineEdit = QLineEdit(self)
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('OK', self)
        btnCancel = QPushButton('Cancel', self)

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel, 0, 0)
        mainLayout.addWidget(nameLineEdit, 0, 1, 1, 2)

        mainLayout.addWidget(passwordLabel, 1, 0)
        mainLayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainLayout.addWidget(btnOK, 2, 1)
        mainLayout.addWidget(btnCancel, 2, 2)

        btnCancel.clicked.connect(self.btnCancel_clicked)

    def btnCancel_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()

    sys.exit(app.exec_())