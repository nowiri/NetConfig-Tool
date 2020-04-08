from telnet_cmds import *
import time
import _thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import ping3
from datetime import datetime
from login import *
from telnetlib import Telnet
import socket #ip validation

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(586, 584)
        MainWindow.setMinimumSize(QtCore.QSize(586, 584))
        MainWindow.setMaximumSize(QtCore.QSize(586, 584))
        MainWindow.setDocumentMode(False)
        ico = QtGui.QIcon('gear-icon-32295.png')
        MainWindow.setWindowIcon(ico)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(20, 30, 551, 61))
        self.frame.setToolTip("")
        self.frame.setStatusTip("")
        self.frame.setAccessibleName("")
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.lblConnection = QtWidgets.QLabel(self.centralwidget)
        self.lblConnection.setGeometry(QtCore.QRect(20, 10, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblConnection.setFont(font)
        self.lblConnection.setObjectName("lblConnection")
        self.lblHistory = QtWidgets.QLabel(self.centralwidget)
        self.lblHistory.setGeometry(QtCore.QRect(20, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblHistory.setFont(font)
        self.lblHistory.setObjectName("lblHistory")
        self.tblHistory = QtWidgets.QTableWidget(self.centralwidget)
        self.tblHistory.setGeometry(QtCore.QRect(20, 120, 551, 191))
        self.tblHistory.setMinimumSize(QtCore.QSize(551, 0))
        self.tblHistory.setMaximumSize(QtCore.QSize(551, 16777215))
        self.tblHistory.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tblHistory.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tblHistory.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblHistory.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblHistory.setAlternatingRowColors(True)
        self.tblHistory.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblHistory.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblHistory.setGridStyle(QtCore.Qt.SolidLine)
        self.tblHistory.setWordWrap(True)
        self.tblHistory.setCornerButtonEnabled(True)
        self.tblHistory.setRowCount(0)
        self.tblHistory.setColumnCount(4)
        self.tblHistory.setObjectName("tblHistory")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tblHistory.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblHistory.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tblHistory.horizontalHeader().setVisible(True)
        self.tblHistory.horizontalHeader().setCascadingSectionResizes(True)
        self.tblHistory.horizontalHeader().setHighlightSections(True)
        self.tblHistory.horizontalHeader().setStretchLastSection(True)
        self.lblMonitor = QtWidgets.QLabel(self.centralwidget)
        self.lblMonitor.setGeometry(QtCore.QRect(20, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMonitor.setFont(font)
        self.lblMonitor.setObjectName("lblMonitor")
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(470, 470, 75, 23))
        self.btnNew.setObjectName("btnNew")

        self.lblNick = QtWidgets.QLabel(self.centralwidget)
        self.lblNick.setGeometry(QtCore.QRect(475, 360, 62, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblNick.setFont(font)
        self.lblNick.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNick.setObjectName("lblNick")
        self.lblNick.setText("Nickname")

        self.lblip = QtWidgets.QLabel(self.centralwidget)
        self.lblip.setGeometry(QtCore.QRect(475, 412, 62, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblip.setFont(font)
        self.lblip.setAlignment(QtCore.Qt.AlignCenter)
        self.lblip.setObjectName("lblip")
        self.lblip.setText("IP")

        self.lblNetConf = QtWidgets.QLabel(self.centralwidget)
        self.lblNetConf.setGeometry(QtCore.QRect(460, 505, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblNetConf.setFont(font)
        self.lblNetConf.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNetConf.setObjectName("lblNetConf")

        self.txtNick = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNick.setGeometry(QtCore.QRect(450, 382, 121, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtNick.sizePolicy().hasHeightForWidth())
        self.txtNick.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtNick.setFont(font)
        self.txtNick.setObjectName("txtNick")

        self.lblAuthor = QtWidgets.QLabel(self.centralwidget)
        self.lblAuthor.setGeometry(QtCore.QRect(460, 525, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblAuthor.setFont(font)
        self.lblAuthor.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAuthor.setObjectName("lblAuthor")
        self.lblMatricula = QtWidgets.QLabel(self.centralwidget)
        self.lblMatricula.setGeometry(QtCore.QRect(460, 545, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMatricula.setFont(font)
        self.lblMatricula.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMatricula.setObjectName("lblMatricula")
        self.txtNew = QtWidgets.QLineEdit(self.centralwidget)
        self.txtNew.setGeometry(QtCore.QRect(450, 435, 121, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtNew.sizePolicy().hasHeightForWidth())
        self.txtNew.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtNew.setFont(font)
        self.txtNew.setObjectName("txtNew")
        self.lblNew = QtWidgets.QLabel(self.centralwidget)
        self.lblNew.setGeometry(QtCore.QRect(453, 325, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblNew.setFont(font)
        self.lblNew.setAlignment(QtCore.Qt.AlignCenter)
        self.lblNew.setObjectName("lblNew")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(30, 50, 530, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.lblIP = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblIP.setFont(font)
        self.lblIP.setObjectName("lblIP")
        self.txtIP = QtWidgets.QLineEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtIP.sizePolicy().hasHeightForWidth())
        self.txtIP.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtIP.setFont(font)
        self.txtIP.setObjectName("txtIP")
        self.lblPort = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPort.setFont(font)
        self.lblPort.setObjectName("lblPort")
        self.txtPORT = QtWidgets.QLineEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtPORT.sizePolicy().hasHeightForWidth())
        self.txtPORT.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtPORT.setFont(font)
        self.txtPORT.setObjectName("txtPORT")

        self.btnCon = QtWidgets.QPushButton(self.splitter)
        self.btnCon.setObjectName("btnCon")
        self.rbtnRemember = QtWidgets.QRadioButton(self.splitter)
        self.rbtnRemember.setObjectName("rbtnRemember")

        self.tblMonitor = QtWidgets.QTableWidget(self.centralwidget)
        self.tblMonitor.setGeometry(QtCore.QRect(20, 350, 421, 213))
        self.tblMonitor.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tblMonitor.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblMonitor.setAlternatingRowColors(True)
        self.tblMonitor.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tblMonitor.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblMonitor.setObjectName("tblMonitor")

        self.tblMonitor.setColumnCount(4)
        self.tblMonitor.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblMonitor.setItem(0, 3, item)
        self.tblMonitor.horizontalHeader().setStretchLastSection(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 586, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btnNew.clicked.connect(self.newMonitor)
        self.tblHistory.doubleClicked.connect(self.click_table)
        self.btnCon.clicked.connect(self.connect)


    def validate_ip(self,s):
        a = s.split('.')
        if len(a) != 4:
            return False
        for x in a:
            if not x.isdigit():
                return False
            i = int(x)
            if i < 0 or i > 255:
                return False
        return True

    def newMonitor(self):
        ip = self.txtNew.text()
        nick = self.txtNick.text()

        if veriftIP(ip)==False or nick=="":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error Critico")
            msg.setInformativeText('Favor verificar datos')
            msg.setWindowTitle("Error")
            msg.exec_()

        elif ping3.ping(ip) is None:
            pass
        else:
            rows = self.tblMonitor.rowCount()
            self.tblMonitor.setRowCount(rows+1)
            for i in range(4):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tblMonitor.setItem(rows, i, item)
                item = self.tblMonitor.item(rows,i)
                if i == 0:
                    item.setText(nick)
                    pass
                if i == 1:
                    item.setText(ip)
                if i == 2: #uptime
                    _thread.start_new_thread(self.monitor, (rows,i,ip))
                    pass
                if i == 3:
                    item.setText("NEVER")
                    pass
        self.txtNew.clear()
        self.txtNick.clear()

    def click_table(self):
        print("\n")
        ip = self.tblHistory.selectedItems()[1].text()
        port = self.tblHistory.selectedItems()[2].text()
        self.txtIP.setText(ip)
        self.txtPORT.setText(port)

        #just as a reminder I'll leave this code here:
        #for currentQTableWidgetItem in self.tblHistory.selectedItems():
        #    print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def connect(self):
        ip = self.txtIP.text()
        port = self.txtPORT.text()
        if ip == "" or port == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Campo Vacio")
            msg.setInformativeText('Ningun campo puede estar vacio!')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            try:
                if self.validate_ip(ip) == False:
                    raise socket.error
                socket.inet_aton(ip)
                if ping3.ping(ip) is None:
                    raise socket.error
                if self.rbtnRemember.isChecked():
                    rows = self.tblHistory.rowCount() #2
                    self.tblHistory.setRowCount(rows + 1)
                    for i in range(4):
                        item = QtWidgets.QTableWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tblHistory.setItem(rows, i, item)
                        item = self.tblHistory.item(rows, i)
                        if i == 0:
                            item.setText("HOSTNAME")
                        if i == 1:
                            item.setText(ip)
                        if i == 2:
                            item.setText(port)
                        if i == 3:
                            item.setText(str(datetime.now()))

                self.log = QtWidgets.QDialog()
                self.ui = Login()
                self.ui.setupUi(self.log,ip,port)
                self.log.show()

                self.txtIP.clear()
                self.txtPORT.setText("23")

            except socket.error:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error de conexion")
                msg.setInformativeText('No se puede conectar con el host!')
                msg.setWindowTitle("Error")
                msg.exec_()
                self.txtIP.clear()
                self.txtPORT.setText("23")


        pass

    def monitor(self, row, col, ip):

        days = 0
        hours = 0
        mins = 0
        secs = 0
        flag = False

        while True:

            if ping3.ping(ip) is not None:
                if not flag:
                    item = self.tblMonitor.item(row, col)
                    flag = True

                if secs == 60:
                    mins += 1
                    secs = 0
                if mins == 60:
                    hours += 1
                    mins = 0
                if hours == 24:
                    days += 1
                    hours = 0

                formatime = str(days)+"d "+str(hours)+"h "+str(mins)+"m "+str(secs)+"s"
                item.setText(formatime)
                self.tblMonitor.viewport().update()
                time.sleep(1)
                secs += 1
            elif flag:
                item.setText("Down!")
                hours = days = mins = secs = 0
                item = self.tblMonitor.item(row, col + 1)
                item.setText(str(datetime.now()))
                flag = False
                self.tblMonitor.viewport().update()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NetConfig Tool v0.1"))
        self.lblConnection.setText(_translate("MainWindow", "CONNECTION"))
        self.lblHistory.setText(_translate("MainWindow", "HISTORY"))
        item = self.tblHistory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "HOSTNAME"))
        item = self.tblHistory.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tblHistory.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PORT"))
        item = self.tblHistory.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "LAST SEEN"))
        __sortingEnabled = self.tblHistory.isSortingEnabled()
        self.tblHistory.setSortingEnabled(False)
        self.tblHistory.setSortingEnabled(__sortingEnabled)
        self.lblMonitor.setText(_translate("MainWindow", "MONITOR"))
        self.btnNew.setText(_translate("MainWindow", "ADD"))
        self.lblNetConf.setText(_translate("MainWindow", "NetConfig Tool"))
        self.lblAuthor.setText(_translate("MainWindow", "By: Jesús Rosario"))
        self.lblMatricula.setText(_translate("MainWindow", "20160277"))
        self.lblNew.setText(_translate("MainWindow", "New"))
        self.lblIP.setText(_translate("MainWindow", "IP ADDRESS"))
        self.lblPort.setText(_translate("MainWindow", "PORT"))
        self.txtPORT.setText("23")
        self.btnCon.setText(_translate("MainWindow", "CONNECT"))
        self.rbtnRemember.setText(_translate("MainWindow", "Remember IP"))
        item = self.tblMonitor.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NICKNAME"))
        item = self.tblMonitor.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "IP"))
        item = self.tblMonitor.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UPTIME"))
        item = self.tblMonitor.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "LAST DOWN"))
        __sortingEnabled = self.tblMonitor.isSortingEnabled()
        self.tblMonitor.setSortingEnabled(False)
        self.tblMonitor.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
