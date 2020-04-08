# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staticroutes.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from telnet_cmds import *


class Ui_SROUTE(QtWidgets.QDialog):
    def setupSROUTEUi(self, Dialog,ip,port,user,passw, enpassw):
        self.Diag = Dialog
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.enpassw = enpassw
        Dialog.setObjectName("Dialog")
        Dialog.resize(217, 193)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        ico = QtGui.QIcon('gear-icon-32295.png')
        Dialog.setWindowIcon(ico)
        self.lblNet = QtWidgets.QLabel(Dialog)
        self.lblNet.setGeometry(QtCore.QRect(30, 10, 51, 16))
        self.lblNet.setObjectName("lblNet")
        self.lblMask = QtWidgets.QLabel(Dialog)
        self.lblMask.setGeometry(QtCore.QRect(40, 40, 31, 21))
        self.lblMask.setObjectName("lblMask")
        self.lblNext = QtWidgets.QLabel(Dialog)
        self.lblNext.setGeometry(QtCore.QRect(25, 70, 47, 13))
        self.lblNext.setObjectName("lblNext")
        self.lblInt = QtWidgets.QLabel(Dialog)
        self.lblInt.setGeometry(QtCore.QRect(25, 90, 47, 13))
        self.lblInt.setObjectName("lblInt")
        self.lvlDist = QtWidgets.QLabel(Dialog)
        self.lvlDist.setGeometry(QtCore.QRect(10, 120, 71, 16))
        self.lvlDist.setObjectName("lvlDist")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 120, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.rdbtnDelete = QtWidgets.QRadioButton(Dialog)
        self.rdbtnDelete.setGeometry(QtCore.QRect(20, 160, 51, 17))
        self.rdbtnDelete.setObjectName("rdbtnDelete")
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(90, 160, 111, 23))
        self.btnOk.setObjectName("btnOk")
        self.lblOr = QtWidgets.QLabel(Dialog)
        self.lblOr.setGeometry(QtCore.QRect(40, 80, 21, 16))
        self.lblOr.setObjectName("lblOr")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnOk.clicked.connect(self.confsroute)

    def confsroute(self):
        net = self.lineEdit.text() #net
        mask = self.lineEdit_2.text() #net
        src = self.lineEdit_3.text() #nexthop or interface
        dist = self.lineEdit_4.text() #adm dist
        no = False
        if veriftIP(net) == False or veriftIP(mask) == False or src == "" or dist == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error Critico")
            msg.setInformativeText('Verifique los datos insertados')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            if self.rdbtnDelete.isChecked():
                no = True
            staticroute(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port),net,mask,src,dist,no)
            self.Diag.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Static Route"))
        self.lblNet.setText(_translate("Dialog", "Network"))
        self.lblMask.setText(_translate("Dialog", "Mask"))
        self.lblNext.setText(_translate("Dialog", "Next-hop"))
        self.lblInt.setText(_translate("Dialog", "Interface"))
        self.lvlDist.setText(_translate("Dialog", "Adm. Distance"))
        self.rdbtnDelete.setText(_translate("Dialog", "Delete"))
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.lblOr.setText(_translate("Dialog", "or"))
