# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confRip.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from telnet_cmds import conection,confRip,veriftIP

class Ui_confrip(object):
    def setupconfripUi(self, Dialog,ip,port,user,passw, enpassw):
        self.Diag = Dialog
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.enpassw = enpassw
        Dialog.setObjectName("Dialog")
        Dialog.resize(190, 100)
        ico = QtGui.QIcon('gear-icon-32295.png')
        Dialog.setWindowIcon(ico)
        self.lblNet = QtWidgets.QLabel(Dialog)
        self.lblNet.setGeometry(QtCore.QRect(11, 13, 47, 13))
        self.lblNet.setObjectName("lblNet")
        self.lblVer = QtWidgets.QLabel(Dialog)
        self.lblVer.setGeometry(QtCore.QRect(12, 38, 47, 13))
        self.lblVer.setObjectName("lblVer")
        self.rbtnOne = QtWidgets.QRadioButton(Dialog)
        self.rbtnOne.setGeometry(QtCore.QRect(80, 38, 31, 17))
        self.rbtnOne.setObjectName("rbtnOne")
        self.rbtnTwo = QtWidgets.QRadioButton(Dialog)
        self.rbtnTwo.setGeometry(QtCore.QRect(130, 39, 31, 17))
        self.rbtnTwo.setChecked(True)
        self.rbtnTwo.setObjectName("rbtnTwo")
        self.txtNet = QtWidgets.QLineEdit(Dialog)
        self.txtNet.setGeometry(QtCore.QRect(60, 10, 121, 20))
        self.txtNet.setObjectName("txtNet")
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(80, 63, 101, 23))
        self.btnOk.setObjectName("btnOk")
        self.rdbtnDelete = QtWidgets.QRadioButton(Dialog)
        self.rdbtnDelete.setGeometry(QtCore.QRect(14, 66, 61, 17))
        self.rdbtnDelete.setObjectName("rdbtnDelete")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnOk.clicked.connect(self.RIP)

    def RIP(self):
        no = False
        if self.rdbtnDelete.isChecked():
            no = True
        net = self.txtNet.text()
        if self.rbtnOne.isChecked():
            ver = "1"
        else:
            ver = "2"
        if veriftIP(net) == False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error Critico")
            msg.setInformativeText('Favor verificar datos')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            confRip(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port),net,ver,no)
        pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "RIP"))
        self.lblNet.setText(_translate("Dialog", "Network"))
        self.lblVer.setText(_translate("Dialog", "Version"))
        self.rbtnOne.setText(_translate("Dialog", "1"))
        self.rbtnTwo.setText(_translate("Dialog", "2"))
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.rdbtnDelete.setText(_translate("Dialog", "Delete"))
