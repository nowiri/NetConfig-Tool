# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from telnet_cmds import *
from newhostname import *
from ospfconf import *
from staticroutes import *
from interfaceConfig import *
from confRip import *
from confDHCP import *
import os

class ConfWindow(object):
    def setupUi(self, MainWindow,ip,port,user,passw, enpassw):
        self.ip = ip
        self. port = port
        self. user = user
        self.passw = passw
        self.enpassw = enpassw
        ico = QtGui.QIcon('gear-icon-32295.png')
        MainWindow.setWindowIcon(ico)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 256)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtbSHOW = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtbSHOW.setGeometry(QtCore.QRect(200, 40, 371, 171))
        self.txtbSHOW.setObjectName("txtbSHOW")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(20, 10, 161, 201))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.lblHostname = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblHostname.setFont(font)
        self.lblHostname.setObjectName("lblHostname")
        self.txtbDETAILS = QtWidgets.QTextBrowser(self.splitter_2)
        self.txtbDETAILS.setObjectName("txtbDETAILS")
        self.lblShow = QtWidgets.QLabel(self.centralwidget)
        self.lblShow.setGeometry(QtCore.QRect(210, 10, 59, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblShow.setFont(font)
        self.lblShow.setObjectName("lblShow")
        self.cboxSelect = QtWidgets.QComboBox(self.centralwidget)
        self.cboxSelect.setGeometry(QtCore.QRect(274, 10, 91, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cboxSelect.setFont(font)
        self.cboxSelect.setObjectName("cboxSelect")
        self.cboxSelect.addItem("")
        self.cboxSelect.addItem("")
        self.cboxSelect.addItem("")
        self.cboxSelect.addItem("")
        self.cboxSelect.addItem("")
        self.cboxSelect.addItem("")
        self.cboxSelect.addItem("")
        self.btnCLI = QtWidgets.QPushButton(self.centralwidget)
        self.btnCLI.setGeometry(QtCore.QRect(370, 10, 75, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCLI.setFont(font)
        self.btnCLI.setObjectName("btnCLI")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 21))
        self.menubar.setObjectName("menubar")
        self.menuConfig = QtWidgets.QMenu(self.menubar)
        self.menuConfig.setObjectName("menuConfig")
        self.menuRouting = QtWidgets.QMenu(self.menubar)
        self.menuRouting.setObjectName("menuRouting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStatic_Routes = QtWidgets.QAction(MainWindow)
        self.actionStatic_Routes.setObjectName("actionStatic_Routes")
        self.actionOSPF = QtWidgets.QAction(MainWindow)
        self.actionOSPF.setObjectName("actionOSPF")
        self.actionHostname = QtWidgets.QAction(MainWindow)
        self.actionHostname.setObjectName("actionHostname")
        self.actionInterface = QtWidgets.QAction(MainWindow)
        self.actionInterface.setObjectName("actionInterface")
        self.actionRIP = QtWidgets.QAction(MainWindow)
        self.actionRIP.setObjectName("actionRIP")
        self.actionDHCP = QtWidgets.QAction(MainWindow)
        self.actionDHCP.setObjectName("actionDHCP")
        self.menuConfig.addAction(self.actionHostname)
        self.menuConfig.addAction(self.actionInterface)
        self.menuRouting.addSeparator()
        self.menuRouting.addAction(self.actionStatic_Routes)
        self.menuRouting.addAction(self.actionOSPF)
        self.menuRouting.addAction(self.actionRIP)
        self.menuRouting.addAction(self.actionDHCP)
        self.menubar.addAction(self.menuConfig.menuAction())
        self.menubar.addAction(self.menuRouting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnCLI.clicked.connect(self.opencli)
        self.actionHostname.triggered.connect(self.openHostname)
        self.actionOSPF.triggered.connect(self.openOSPF)
        self.actionStatic_Routes.triggered.connect(self.openSROUTE)
        self.actionInterface.triggered.connect(self.openIntconf)
        self.cboxSelect.currentIndexChanged.connect(self.SHOWS)
        self.actionRIP.triggered.connect(self.openRIP)
        self.actionDHCP.triggered.connect(self.openDHCP)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.lblHostname.setText(gethostname(conection(self.user,self.passw, self.enpassw, self.ip,1,self.port)))
        self.txtbDETAILS.setText(showver(conection(self.user,self.passw,self.enpassw,self.ip,1,self.port)))
        MainWindow.setWindowTitle(_translate("MainWindow", "Configuration Window"))
        self.lblShow.setText(_translate("MainWindow", "Show ..."))
        self.cboxSelect.setItemText(0, _translate("MainWindow", "<Select>"))
        self.cboxSelect.setItemText(1, _translate("MainWindow", "Ip route"))
        self.cboxSelect.setItemText(2, _translate("MainWindow", "Interface"))
        self.cboxSelect.setItemText(3, _translate("MainWindow", "Vlan"))
        self.cboxSelect.setItemText(4, _translate("MainWindow", "Arp"))
        self.cboxSelect.setItemText(5, _translate("MainWindow", "Run"))
        self.cboxSelect.setItemText(6, _translate("MainWindow", "ip protocols"))
        self.btnCLI.setText(_translate("MainWindow", "Open CLI"))
        self.menuConfig.setTitle(_translate("MainWindow", "Config"))
        self.menuRouting.setTitle(_translate("MainWindow", "Routing"))
        self.actionStatic_Routes.setText(_translate("MainWindow", "New static route"))
        self.actionOSPF.setText(_translate("MainWindow", "OSPF"))
        self.actionHostname.setText(_translate("MainWindow", "Hostname"))
        self.actionInterface.setText(_translate("MainWindow", "Interface"))
        self.actionRIP.setText(_translate("MainWindow", "RIP"))
        self.actionDHCP.setText(_translate("MainWindow", "DHCP"))

    def SHOWS(self):
        option = self.cboxSelect.currentIndex()
        if option == 0:
            pass
        elif option == 1:
            sh = showroutes(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port))
            self.txtbSHOW.setText(sh)
            self.cboxSelect.setCurrentIndex(0)
        elif option == 2:
            sh = showinterfaces(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port))
            self.txtbSHOW.setText(sh)
            self.cboxSelect.setCurrentIndex(0)
        elif option == 3:
            sh = showvlan(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port))
            self.txtbSHOW.setText(sh)
            self.cboxSelect.setCurrentIndex(0)
            pass
        elif option == 4:
            sh = showarp(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port))
            self.txtbSHOW.setText(sh)
            self.cboxSelect.setCurrentIndex(0)
        elif option == 5:
            sh = showrun(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port))
            self.txtbSHOW.setText(sh)
            self.cboxSelect.setCurrentIndex(0)
        elif option == 6:
            sh = showIPPROTO(conection(self.user, self.passw, self.enpassw, self.ip, 1, self.port))
            self.txtbSHOW.setText(sh)
            self.cboxSelect.setCurrentIndex(0)

    def openHostname(self):
        self.ht = QtWidgets.QDialog()
        self.ui = HTDialog()
        self.ui.HT(self.ht,self.ip,self.port, self.user, self.passw, self.passw, self.lblHostname)
        self.ht.show()

    def openOSPF(self):
        self.ospf = QtWidgets.QDialog()
        self.ui = Ui_ospfconf()
        self.ui.setupOspfUi(self.ospf, self.ip, self.port, self.user, self.passw, self.passw,)
        self.ospf.show()

    def openRIP(self):
        self.rip = QtWidgets.QDialog()
        self.ui = Ui_confrip()
        self.ui.setupconfripUi(self.rip, self.ip, self.port, self.user, self.passw, self.passw)
        self.rip.show()

    def openSROUTE(self):
        self.route = QtWidgets.QDialog()
        self.ui = Ui_SROUTE()
        self.ui.setupSROUTEUi(self.route, self.ip, self.port, self.user, self.passw, self.passw, )
        self.route.show()

    def openIntconf(self):
        self.int = QtWidgets.QDialog()
        self.ui = Ui_intconf()
        self.ui.setupintconfUi(self.int, self.ip, self.port, self.user, self.passw, self.passw )
        self.int.show()

    def openDHCP(self):
        self.dhcp = QtWidgets.QDialog()
        self.ui = Ui_confDHCP()
        self.ui.setupconfDHCPUi(self.dhcp, self.ip, self.port, self.user, self.passw, self.passw)
        self.dhcp.show()

    def opencli(self):
        command = "telnet " + self.ip
        os.system(f"start /wait cmd /c {command}")
