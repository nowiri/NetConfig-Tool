# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ospfconf.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from telnet_cmds import *


class Ui_ospfconf(object):
    def setupOspfUi(self, Dialog,ip,port,user,passw, enpassw):
        self.Diag = Dialog
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.enpassw = enpassw
        Dialog.setObjectName("Dialog")
        Dialog.resize(370, 73)
        ico = QtGui.QIcon('gear-icon-32295.png')
        Dialog.setWindowIcon(ico)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.lblPro = QtWidgets.QLabel(Dialog)
        self.lblPro.setGeometry(QtCore.QRect(260, 10, 61, 16))
        self.lblPro.setObjectName("lblPro")
        self.spboxPro = QtWidgets.QSpinBox(Dialog)
        self.spboxPro.setGeometry(QtCore.QRect(320, 10, 41, 22))
        self.spboxPro.setObjectName("spboxPro")
        self.lblNet = QtWidgets.QLabel(Dialog)
        self.lblNet.setGeometry(QtCore.QRect(10, 10, 41, 20))
        self.lblNet.setObjectName("lblNet")
        self.lblWild = QtWidgets.QLabel(Dialog)
        self.lblWild.setGeometry(QtCore.QRect(10, 40, 41, 20))
        self.lblWild.setObjectName("lblWild")
        self.lblArea = QtWidgets.QLabel(Dialog)
        self.lblArea.setGeometry(QtCore.QRect(180, 10, 41, 16))
        self.lblArea.setObjectName("lblArea")
        self.txtNet = QtWidgets.QLineEdit(Dialog)
        self.txtNet.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.txtNet.setObjectName("txtNet")
        self.txtWild = QtWidgets.QLineEdit(Dialog)
        self.txtWild.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.txtWild.setObjectName("txtWild")
        self.btnOk = QtWidgets.QPushButton(Dialog)
        self.btnOk.setGeometry(QtCore.QRect(250, 40, 101, 21))
        self.btnOk.setObjectName("btnOk")
        self.rbtnDelete = QtWidgets.QRadioButton(Dialog)
        self.rbtnDelete.setGeometry(QtCore.QRect(190, 36, 61, 31))
        self.rbtnDelete.setObjectName("rbtnDelete")
        self.spboxArea = QtWidgets.QSpinBox(Dialog)
        self.spboxArea.setGeometry(QtCore.QRect(210, 10, 41, 22))
        self.spboxArea.setObjectName("spboxArea")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnOk.clicked.connect(self.ospf)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblPro.setText(_translate("Dialog", "Process ID"))
        self.lblNet.setText(_translate("Dialog", "Network"))
        self.lblWild.setText(_translate("Dialog", "Wildcard"))
        self.lblArea.setText(_translate("Dialog", "Area"))
        self.btnOk.setText(_translate("Dialog", "OK"))
        self.rbtnDelete.setText(_translate("Dialog", "Delete"))

    def ospf(self):
        pro = self.spboxPro.text()
        net = self.txtNet.text()
        wild = self.txtWild.text()
        area = self.spboxArea.text()
        no = False
        if net == "" or wild == "" or veriftIP(net) == False:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error Critico")
            msg.setInformativeText('Verifique los datos insertados')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            if self.rbtnDelete.isChecked():
                no = True
            confospf(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port),pro,net,wild,area,no)
            self.Diag.close()

