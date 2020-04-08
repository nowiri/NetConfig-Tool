# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from telnet_cmds import *
from configWindow import *


class Login(QtWidgets.QDialog):
    def setupUi(self, loginDiag,ip, port):
        self.ip = ip
        self.port = port
        self.loginD = loginDiag
        ico = QtGui.QIcon('gear-icon-32295.png')
        loginDiag.setWindowIcon(ico)
        loginDiag.setObjectName("loginDiag")
        loginDiag.resize(209, 150)
        loginDiag.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.lblUser = QtWidgets.QLabel(loginDiag)
        self.lblUser.setGeometry(QtCore.QRect(10, 20, 48, 13))
        self.lblUser.setObjectName("lblUser")
        self.lblPass = QtWidgets.QLabel(loginDiag)
        self.lblPass.setGeometry(QtCore.QRect(10, 50, 46, 13))
        self.lblPass.setObjectName("lblPass")
        self.txtPass = QtWidgets.QLineEdit(loginDiag)
        self.txtPass.setGeometry(QtCore.QRect(60, 50, 133, 20))
        self.txtPass.setObjectName("txtPass")
        self.txtUser = QtWidgets.QLineEdit(loginDiag)
        self.txtUser.setGeometry(QtCore.QRect(60, 20, 133, 20))
        self.txtUser.setObjectName("txtUser")
        self.btnOk = QtWidgets.QPushButton(loginDiag)
        self.btnOk.setGeometry(QtCore.QRect(10, 110, 181, 23))
        self.btnOk.setObjectName("btnOk")
        self.lblPass_2 = QtWidgets.QLabel(loginDiag)
        self.lblPass_2.setGeometry(QtCore.QRect(10, 80, 46, 13))
        self.lblPass_2.setObjectName("lblPass_2")
        self.txtPass_2 = QtWidgets.QLineEdit(loginDiag)
        self.txtPass_2.setGeometry(QtCore.QRect(60, 80, 133, 20))
        self.txtPass_2.setObjectName("txtPass_2")
        self.lblPass_3 = QtWidgets.QLabel(loginDiag)
        self.lblPass_3.setGeometry(QtCore.QRect(10, 90, 46, 13))
        self.lblPass_3.setObjectName("lblPass_3")

        self.retranslateUi(loginDiag)
        QtCore.QMetaObject.connectSlotsByName(loginDiag)

        self.btnOk.clicked.connect(self.openConfig)

    def retranslateUi(self, loginDiag):
        _translate = QtCore.QCoreApplication.translate
        loginDiag.setWindowTitle(_translate("loginDiag", "Credentials"))
        self.lblUser.setText(_translate("loginDiag", "Username"))
        self.lblPass.setText(_translate("loginDiag", "Password"))
        self.btnOk.setText(_translate("loginDiag", "OK"))
        self.lblPass_2.setText(_translate("loginDiag", "Enable"))
        self.lblPass_3.setText(_translate("loginDiag", "Password"))

    def openConfig(self):
        user = self.txtUser.text()
        passw = self.txtPass.text()
        enpassw = self.txtPass_2.text()
        if user == "" or passw == "" or enpassw == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Campo Vacio")
            msg.setInformativeText('Ningun campo puede estar vacio!')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            estatus = conection(user,passw,enpassw,self.ip,0,int(self.port))
            fail = "%" in estatus
            if fail:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Credicailes incorrectas")
                msg.setInformativeText('Las credenciales digitadas no son correctas')
                msg.setWindowTitle("Error")
                msg.exec_()
            else:
                self.conf = QtWidgets.QMainWindow()
                self.ui = ConfWindow()
                self.ui.setupUi(self.conf, self.ip, self.port, user,passw, enpassw)
                self.conf.show()
                self.loginD.close()