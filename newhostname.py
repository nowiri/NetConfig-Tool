# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newhostname.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from telnet_cmds import sethostname,conection


class HTDialog(QtWidgets.QDialog):
    def HT(self, Dialog,ip,port,user,passw, enpassw, Label):
        self.Diag = Dialog
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.enpassw = enpassw
        self.hostnamelbl = Label
        ico = QtGui.QIcon('gear-icon-32295.png')
        Dialog.setWindowIcon(ico)
        Dialog.setObjectName("Dialog")
        Dialog.resize(324, 61)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.lblHostname = QtWidgets.QLabel(Dialog)
        self.lblHostname.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.lblHostname.setObjectName("lblHostname")
        self.txtHostname = QtWidgets.QLineEdit(Dialog)
        self.txtHostname.setEnabled(True)
        self.txtHostname.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.txtHostname.setObjectName("txtHostname")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(230, 20, 75, 23))
        self.btnOK.setObjectName("btnOK")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.btnOK.clicked.connect(self.change)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Set new hostname"))
        self.lblHostname.setText(_translate("Dialog", "New hostname"))
        self.btnOK.setText(_translate("Dialog", "OK"))

    def change(self):
        name = self.txtHostname.text()
        if name == "":
            pass
        else:
            sethostname(conection(self.user,self.passw,self.enpassw,self.ip,1,self.port),name)
            self.hostnamelbl.setText(name)
            self.Diag.close()

