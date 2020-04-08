# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaceConfig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from telnet_cmds import showinterfaces, conection,interfaceConfig


class Ui_intconf(object):
    def setupintconfUi(self, Dialog, ip,port,user,passw, enpassw):
        self.Diag = Dialog
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.enpassw = enpassw
        Dialog.setObjectName("Dialog")
        Dialog.resize(464, 197)
        ico = QtGui.QIcon('gear-icon-32295.png')
        Dialog.setWindowIcon(ico)
        Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.lblInterface = QtWidgets.QLabel(Dialog)
        self.lblInterface.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.lblInterface.setObjectName("lblInterface")
        self.txtbInterfaces = QtWidgets.QTextBrowser(Dialog)
        self.txtbInterfaces.setGeometry(QtCore.QRect(10, 40, 171, 151))
        self.txtbInterfaces.setObjectName("txtbInterfaces")
        self.txtInterface = QtWidgets.QLineEdit(Dialog)
        self.txtInterface.setGeometry(QtCore.QRect(60, 10, 121, 20))
        self.txtInterface.setObjectName("txtInterface")
        self.lblTip = QtWidgets.QLabel(Dialog)
        self.lblTip.setGeometry(QtCore.QRect(200, 10, 381, 21))
        self.lblTip.setObjectName("lblTip")
        self.lblDesc = QtWidgets.QLabel(Dialog)
        self.lblDesc.setGeometry(QtCore.QRect(210, 40, 61, 16))
        self.lblDesc.setObjectName("lblDesc")
        self.txtDescription = QtWidgets.QLineEdit(Dialog)
        self.txtDescription.setEnabled(False)
        self.txtDescription.setGeometry(QtCore.QRect(290, 40, 161, 20))
        self.txtDescription.setObjectName("txtDescription")
        self.rdbtnDesc = QtWidgets.QRadioButton(Dialog)
        self.rdbtnDesc.setGeometry(QtCore.QRect(190, 40, 16, 17))
        self.rdbtnDesc.setText("")
        self.rdbtnDesc.setAutoExclusive(False)
        self.rdbtnDesc.setObjectName("rdbtnDesc")
        self.rdbtnSw = QtWidgets.QRadioButton(Dialog)
        self.rdbtnSw.setGeometry(QtCore.QRect(190, 126, 16, 17))
        self.rdbtnSw.setText("")
        self.rdbtnSw.setAutoExclusive(False)
        self.rdbtnSw.setObjectName("rdbtnSw")
        self.rdbtnDelente = QtWidgets.QRadioButton(Dialog)
        self.rdbtnDelente.setGeometry(QtCore.QRect(330, 160, 16, 17))
        self.rdbtnDelente.setText("")
        self.rdbtnDelente.setAutoExclusive(False)
        self.rdbtnDelente.setObjectName("rdbtnDelente")
        self.rdbtnIP = QtWidgets.QRadioButton(Dialog)
        self.rdbtnIP.setGeometry(QtCore.QRect(190, 73, 16, 17))
        self.rdbtnIP.setText("")
        self.rdbtnIP.setAutoExclusive(False)
        self.rdbtnIP.setObjectName("rdbtnIP")
        self.lblIP = QtWidgets.QLabel(Dialog)
        self.lblIP.setGeometry(QtCore.QRect(211, 73, 21, 16))
        self.lblIP.setObjectName("lblIP")
        self.cboxIP = QtWidgets.QComboBox(Dialog)
        self.cboxIP.setEnabled(False)
        self.cboxIP.setGeometry(QtCore.QRect(230, 70, 51, 22))
        self.cboxIP.setObjectName("cboxIP")
        self.cboxIP.addItem("")
        self.cboxIP.addItem("")
        self.lblsAddress = QtWidgets.QLabel(Dialog)
        self.lblsAddress.setGeometry(QtCore.QRect(291, 75, 47, 13))
        self.lblsAddress.setObjectName("lblsAddress")
        self.txtAddress = QtWidgets.QLineEdit(Dialog)
        self.txtAddress.setEnabled(False)
        self.txtAddress.setGeometry(QtCore.QRect(338, 70, 113, 20))
        self.txtAddress.setObjectName("txtAddress")
        self.lblMask = QtWidgets.QLabel(Dialog)
        self.lblMask.setGeometry(QtCore.QRect(299, 98, 47, 13))
        self.lblMask.setObjectName("lblMask")
        self.txtMask = QtWidgets.QLineEdit(Dialog)
        self.txtMask.setEnabled(False)
        self.txtMask.setGeometry(QtCore.QRect(338, 93, 113, 20))
        self.txtMask.setObjectName("txtMask")
        self.lblSw = QtWidgets.QLabel(Dialog)
        self.lblSw.setGeometry(QtCore.QRect(210, 126, 51, 16))
        self.lblSw.setObjectName("lblSw")
        self.cboxSw = QtWidgets.QComboBox(Dialog)
        self.cboxSw.setEnabled(False)
        self.cboxSw.setGeometry(QtCore.QRect(260, 123, 61, 22))
        self.cboxSw.setObjectName("cboxSw")
        self.cboxSw.addItem("")
        self.cboxSw.addItem("")
        self.lblAccess = QtWidgets.QLabel(Dialog)
        self.lblAccess.setGeometry(QtCore.QRect(330, 125, 61, 16))
        self.lblAccess.setObjectName("lblAccess")
        self.txtVlan = QtWidgets.QLineEdit(Dialog)
        self.txtVlan.setEnabled(False)
        self.txtVlan.setGeometry(QtCore.QRect(390, 123, 61, 20))
        self.txtVlan.setObjectName("txtVlan")
        self.cboxShut = QtWidgets.QComboBox(Dialog)
        self.cboxShut.setEnabled(False)
        self.cboxShut.setGeometry(QtCore.QRect(260, 157, 61, 22))
        self.cboxShut.setObjectName("cboxShut")
        self.cboxShut.addItem("")
        self.cboxShut.addItem("")
        self.lblShut = QtWidgets.QLabel(Dialog)
        self.lblShut.setGeometry(QtCore.QRect(210, 160, 51, 16))
        self.lblShut.setObjectName("lblShut")
        self.rdbtnShut = QtWidgets.QRadioButton(Dialog)
        self.rdbtnShut.setGeometry(QtCore.QRect(190, 160, 16, 17))
        self.rdbtnShut.setText("")
        self.rdbtnShut.setAutoExclusive(False)
        self.rdbtnShut.setObjectName("rdbtnShut")
        self.lblDelete = QtWidgets.QLabel(Dialog)
        self.lblDelete.setGeometry(QtCore.QRect(350, 162, 31, 16))
        self.lblDelete.setObjectName("lblDelete")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(390, 156, 61, 23))
        self.btnOK.setAutoExclusive(True)
        self.btnOK.setObjectName("btnOK")

        self.retranslateUi(Dialog)

        self.rdbtnDesc.clicked.connect(self.actDesc)
        self.rdbtnIP.clicked.connect(self.actIP)
        self.rdbtnShut.clicked.connect(self.actShut)
        self.rdbtnSw.clicked.connect(self.actSw)
        self.cboxIP.currentIndexChanged.connect(self.changeIP)
        self.cboxSw.currentIndexChanged.connect(self.changeSw)

        self.btnOK.clicked.connect(self.interfaces)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def actDesc(self):
        if self.rdbtnDesc.isChecked():
            self.txtDescription.setEnabled(True)
        else:
            self.txtDescription.setEnabled(False)

    def actIP(self):
        if self.rdbtnIP.isChecked():
            self.cboxIP.setEnabled(True)
            if self.cboxIP.currentIndex() == 1:
                self.txtAddress.setEnabled(True)
                self.txtMask.setEnabled(True)
        else:
            self.txtAddress.setEnabled(False)
            self.txtMask.setEnabled(False)

    def changeIP(self):
        if self.cboxIP.currentIndex() == 0:
            self.txtAddress.setEnabled(False)
            self.txtMask.setEnabled(False)
        else:
            self.txtAddress.setEnabled(True)
            self.txtMask.setEnabled(True)

    def actShut(self):
        if self.rdbtnShut.isChecked():
            self.cboxShut.setEnabled(True)
        else:
            self.cboxShut.setEnabled(False)

    def actSw(self):
        if self.rdbtnSw.isChecked():
            self.cboxSw.setEnabled(True)
            if self.cboxIP.currentIndex() == 0:
                self.txtVlan.setEnabled(True)
        else:
            self.cboxSw.setEnabled(False)
            self.txtVlan.setEnabled(False)

    def changeSw(self):
        if self.cboxSw.currentIndex() == 0:
            self.txtVlan.setEnabled(True)
        else:
            self.txtVlan.setEnabled(False)

    def interfaces(self):
        int = desc = ip = mask = swmode = vlan = shut = ""
        adddesc = addip = addswmode = addaccess = addshut = no = False
        int = self.txtInterface.text()
        if self.rdbtnDesc.isChecked():
            adddesc = True
            desc = self.txtDescription.text()
        if self.rdbtnIP.isChecked():
            addip = True
            if self.cboxIP.currentIndex()==0:
                ip = "dhcp"
            else:
                ip = self.txtAddress.text()
            mask = self.txtMask.text()
        if self.rdbtnSw.isChecked():
            addswmode = True
            if self.cboxSw.currentIndex()==0:
                addaccess = True
                swmode = "access"
                vlan = self.txtVlan.text()
            else:
                swmode = "trunk"
        if self.rdbtnShut.isChecked():
            addshut = True
            if self.cboxShut.currentIndex()==0:
                shut = "no"
            else:
                pass
        if self.rdbtnDelente.isChecked():
            no = True

        interfaceConfig(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port), int, desc, ip, mask, swmode, vlan, shut, adddesc, addip, addswmode,addaccess, addshut,no)
        pass

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configure Interface"))
        self.lblInterface.setText(_translate("Dialog", "Interface"))
        self.lblTip.setText(_translate("Dialog", "* Tip * : Puede utilizar el comando range."))
        self.lblDesc.setText(_translate("Dialog", "Description"))
        self.lblIP.setText(_translate("Dialog", "IP"))
        self.cboxIP.setItemText(0, _translate("Dialog", "DHCP"))
        self.cboxIP.setItemText(1, _translate("Dialog", "Static"))
        self.lblsAddress.setText(_translate("Dialog", "Address"))
        self.lblMask.setText(_translate("Dialog", "Mask"))
        self.lblSw.setText(_translate("Dialog", "Sw Mode"))
        self.cboxSw.setItemText(0, _translate("Dialog", "Access"))
        self.cboxSw.setItemText(1, _translate("Dialog", "Trunk"))
        self.lblAccess.setText(_translate("Dialog", "Access Vlan"))
        self.cboxShut.setItemText(0, _translate("Dialog", "No"))
        self.cboxShut.setItemText(1, _translate("Dialog", "Yes"))
        self.lblShut.setText(_translate("Dialog", "Shutdown"))
        self.lblDelete.setText(_translate("Dialog", "Delete"))
        self.btnOK.setText(_translate("Dialog", "OK"))
        self.txtbInterfaces.setText(showinterfaces(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port)))

