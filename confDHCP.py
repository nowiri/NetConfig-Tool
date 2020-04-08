# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'confDHCP.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from telnet_cmds import conection,veriftIP,confDHCP,showDHCP


class Ui_confDHCP(object):
    def setupconfDHCPUi(self, Dialog, ip, port, user, passw, enpassw):
        self.Diag = Dialog
        self.ip = ip
        self.port = port
        self.user = user
        self.passw = passw
        self.enpassw = enpassw
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 255)
        ico = QtGui.QIcon('gear-icon-32295.png')
        Dialog.setWindowIcon(ico)
        self.txtPool = QtWidgets.QLineEdit(Dialog)
        self.txtPool.setGeometry(QtCore.QRect(90, 10, 121, 20))
        self.txtPool.setObjectName("txtPool")
        self.rdbtnExclude = QtWidgets.QRadioButton(Dialog)
        self.rdbtnExclude.setGeometry(QtCore.QRect(230, 13, 16, 17))
        self.rdbtnExclude.setText("")
        self.rdbtnExclude.setAutoExclusive(False)
        self.rdbtnExclude.setObjectName("rdbtnExclude")
        self.lblPool = QtWidgets.QLabel(Dialog)
        self.lblPool.setGeometry(QtCore.QRect(20, 12, 71, 16))
        self.lblPool.setObjectName("lblPool")
        self.txtbDhcp = QtWidgets.QTextBrowser(Dialog)
        self.txtbDhcp.setGeometry(QtCore.QRect(10, 40, 201, 201))
        self.txtbDhcp.setObjectName("txtbDhcp")
        self.lblExclude = QtWidgets.QLabel(Dialog)
        self.lblExclude.setGeometry(QtCore.QRect(263, 13, 101, 16))
        self.lblExclude.setObjectName("lblExclude")
        self.lblFrom = QtWidgets.QLabel(Dialog)
        self.lblFrom.setGeometry(QtCore.QRect(230, 51, 31, 16))
        self.lblFrom.setObjectName("lblFrom")
        self.txtFrom = QtWidgets.QLineEdit(Dialog)
        self.txtFrom.setEnabled(False)
        self.txtFrom.setGeometry(QtCore.QRect(260, 50, 91, 20))
        self.txtFrom.setObjectName("txtFrom")
        self.txtTo = QtWidgets.QLineEdit(Dialog)
        self.txtTo.setEnabled(False)
        self.txtTo.setGeometry(QtCore.QRect(380, 50, 91, 20))
        self.txtTo.setObjectName("txtTo")
        self.lblTo = QtWidgets.QLabel(Dialog)
        self.lblTo.setGeometry(QtCore.QRect(360, 50, 21, 16))
        self.lblTo.setObjectName("lblTo")
        self.rdbtnNet = QtWidgets.QRadioButton(Dialog)
        self.rdbtnNet.setGeometry(QtCore.QRect(230, 79, 16, 17))
        self.rdbtnNet.setText("")
        self.rdbtnNet.setAutoExclusive(False)
        self.rdbtnNet.setObjectName("rdbtnNet")
        self.rdbtnDefault = QtWidgets.QRadioButton(Dialog)
        self.rdbtnDefault.setGeometry(QtCore.QRect(230, 141, 16, 17))
        self.rdbtnDefault.setText("")
        self.rdbtnDefault.setAutoExclusive(False)
        self.rdbtnDefault.setObjectName("rdbtnDefault")
        self.lblNet = QtWidgets.QLabel(Dialog)
        self.lblNet.setGeometry(QtCore.QRect(270, 80, 47, 13))
        self.lblNet.setObjectName("lblNet")
        self.lblMask = QtWidgets.QLabel(Dialog)
        self.lblMask.setGeometry(QtCore.QRect(380, 80, 47, 13))
        self.lblMask.setObjectName("lblMask")
        self.txtNet = QtWidgets.QLineEdit(Dialog)
        self.txtNet.setEnabled(False)
        self.txtNet.setGeometry(QtCore.QRect(260, 100, 91, 20))
        self.txtNet.setObjectName("txtNet")
        self.txtMask = QtWidgets.QLineEdit(Dialog)
        self.txtMask.setEnabled(False)
        self.txtMask.setGeometry(QtCore.QRect(380, 100, 91, 20))
        self.txtMask.setObjectName("txtMask")
        self.lblDefault = QtWidgets.QLabel(Dialog)
        self.lblDefault.setGeometry(QtCore.QRect(260, 141, 71, 16))
        self.lblDefault.setObjectName("lblDefault")
        self.txtDefault = QtWidgets.QLineEdit(Dialog)
        self.txtDefault.setEnabled(False)
        self.txtDefault.setGeometry(QtCore.QRect(340, 140, 131, 20))
        self.txtDefault.setObjectName("txtDefault")
        self.txtDNS = QtWidgets.QLineEdit(Dialog)
        self.txtDNS.setEnabled(False)
        self.txtDNS.setGeometry(QtCore.QRect(340, 179, 131, 20))
        self.txtDNS.setObjectName("txtDNS")
        self.lblDNS = QtWidgets.QLabel(Dialog)
        self.lblDNS.setGeometry(QtCore.QRect(260, 180, 71, 16))
        self.lblDNS.setObjectName("lblDNS")
        self.rdbtnDNS = QtWidgets.QRadioButton(Dialog)
        self.rdbtnDNS.setGeometry(QtCore.QRect(230, 180, 16, 17))
        self.rdbtnDNS.setText("")
        self.rdbtnDNS.setAutoExclusive(False)
        self.rdbtnDNS.setObjectName("rdbtnDNS")
        self.rdbtnDelete = QtWidgets.QRadioButton(Dialog)
        self.rdbtnDelete.setGeometry(QtCore.QRect(230, 214, 16, 17))
        self.rdbtnDelete.setText("")
        self.rdbtnDelete.setAutoExclusive(False)
        self.rdbtnDelete.setObjectName("rdbtnDelete")
        self.btnOK = QtWidgets.QPushButton(Dialog)
        self.btnOK.setGeometry(QtCore.QRect(360, 210, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.lblDelete = QtWidgets.QLabel(Dialog)
        self.lblDelete.setGeometry(QtCore.QRect(260, 214, 71, 16))
        self.lblDelete.setObjectName("lblDelete")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.rdbtnExclude.clicked.connect(self.actExclude)
        self.rdbtnNet.clicked.connect(self.actNet)
        self.rdbtnDefault.clicked.connect(self.actDefault)
        self.rdbtnDNS.clicked.connect(self.actDNS)
        self.btnOK.clicked.connect(self.DHCP)

    def actExclude(self):
        if self.rdbtnExclude.isChecked():
            self.txtFrom.setEnabled(True)
            self.txtTo.setEnabled(True)
        else:
            self.txtFrom.setEnabled(False)
            self.txtTo.setEnabled(False)

    def actNet(self):
        if self.rdbtnNet.isChecked():
            self.txtNet.setEnabled(True)
            self.txtMask.setEnabled(True)
        else:
            self.txtNet.setEnabled(False)
            self.txtMask.setEnabled(False)

    def actDefault(self):
        if self.rdbtnDefault.isChecked():
            self.txtDefault.setEnabled(True)
        else:
            self.txtDefault.setEnabled(False)

    def actDNS(self):
        if self.rdbtnDNS.isChecked():
            self.txtDNS.setEnabled(True)
        else:
            self.txtDNS.setEnabled(False)

    def DHCP(self):
        pool = fro = to = net = mask = default = dns = ""
        addexc = addnet = adddefault = adddns = no = False
        pool = self.txtPool.text()
        if self.rdbtnExclude.isChecked():
            addexc = True
            fro = self.txtFrom.text()
            to = self.txtTo.text()
        if self.rdbtnNet.isChecked():
            addNet = True
            net = self.txtNet.text()
            mask = self.txtMask.text()
        if self.rdbtnDefault.isChecked():
            adddefault = True
            default = self.txtDefault.text()
        if self.rdbtnDNS.isChecked():
            adddns = True
            dns = self.txtDNS.text()
        if self.rdbtnDelete.isChecked():
            no = True

        confDHCP(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port),pool,fro,to,net,mask,default,dns,no,addexc,addnet,adddefault,adddns)
        self.Diag.close()
        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "DHCP"))
        self.lblPool.setText(_translate("Dialog", "IP DHCP Pool"))
        self.lblExclude.setText(_translate("Dialog", "Exclude IP Adresses"))
        self.lblFrom.setText(_translate("Dialog", "From"))
        self.lblTo.setText(_translate("Dialog", "To"))
        self.lblNet.setText(_translate("Dialog", "Network"))
        self.lblMask.setText(_translate("Dialog", "Mask"))
        self.lblDefault.setText(_translate("Dialog", "Defaut Router"))
        self.lblDNS.setText(_translate("Dialog", "DNS-Server"))
        self.btnOK.setText(_translate("Dialog", "OK"))
        self.lblDelete.setText(_translate("Dialog", "Delete"))
        self.txtbDhcp.setText(showDHCP(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port)))
