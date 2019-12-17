# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'somme.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.bt = QtWidgets.QPushButton(Dialog)
        self.bt.setGeometry(QtCore.QRect(160, 170, 75, 23))
        self.bt.setObjectName("bt")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 40, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 47, 13))
        self.label_3.setObjectName("label_3")
        self.v1 = QtWidgets.QLineEdit(Dialog)
        self.v1.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.v1.setObjectName("v1")
        self.v2 = QtWidgets.QLineEdit(Dialog)
        self.v2.setGeometry(QtCore.QRect(90, 110, 113, 20))
        self.v2.setObjectName("v2")
        self.res = QtWidgets.QLabel(Dialog)
        self.res.setGeometry(QtCore.QRect(140, 230, 47, 13))
        self.res.setText("")
        self.res.setObjectName("res")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.bt.setText(_translate("Dialog", "Calculer"))
        self.label.setText(_translate("Dialog", "Calcule"))
        self.label_2.setText(_translate("Dialog", "V1:"))
        self.label_3.setText(_translate("Dialog", "V2:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
