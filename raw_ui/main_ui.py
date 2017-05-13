# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Sat May 13 09:09:59 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(455, 366)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBoxKec = QtGui.QComboBox(self.centralwidget)
        self.comboBoxKec.setEditable(True)
        self.comboBoxKec.setObjectName(_fromUtf8("comboBoxKec"))
        self.gridLayout.addWidget(self.comboBoxKec, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.comboBoxProv = QtGui.QComboBox(self.centralwidget)
        self.comboBoxProv.setEditable(True)
        self.comboBoxProv.setObjectName(_fromUtf8("comboBoxProv"))
        self.gridLayout.addWidget(self.comboBoxProv, 1, 1, 1, 1)
        self.comboBoxKel = QtGui.QComboBox(self.centralwidget)
        self.comboBoxKel.setEditable(True)
        self.comboBoxKel.setObjectName(_fromUtf8("comboBoxKel"))
        self.gridLayout.addWidget(self.comboBoxKel, 4, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEditKodepos = QtGui.QLineEdit(self.centralwidget)
        self.lineEditKodepos.setObjectName(_fromUtf8("lineEditKodepos"))
        self.gridLayout.addWidget(self.lineEditKodepos, 5, 1, 1, 1)
        self.lineEditCari = QtGui.QLineEdit(self.centralwidget)
        self.lineEditCari.setObjectName(_fromUtf8("lineEditCari"))
        self.gridLayout.addWidget(self.lineEditCari, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.comboBoxKab = QtGui.QComboBox(self.centralwidget)
        self.comboBoxKab.setEditable(True)
        self.comboBoxKab.setObjectName(_fromUtf8("comboBoxKab"))
        self.gridLayout.addWidget(self.comboBoxKab, 2, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget, 6, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 455, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditCari, self.comboBoxProv)
        MainWindow.setTabOrder(self.comboBoxProv, self.comboBoxKab)
        MainWindow.setTabOrder(self.comboBoxKab, self.comboBoxKec)
        MainWindow.setTabOrder(self.comboBoxKec, self.comboBoxKel)
        MainWindow.setTabOrder(self.comboBoxKel, self.lineEditKodepos)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_5.setText(_translate("MainWindow", "Kodepos", None))
        self.label_4.setText(_translate("MainWindow", "Kelurahan", None))
        self.label.setText(_translate("MainWindow", "Provinsi", None))
        self.label_2.setText(_translate("MainWindow", "Kabupaten", None))
        self.label_3.setText(_translate("MainWindow", "Kecamatan", None))
        self.label_6.setText(_translate("MainWindow", "Cari Kodepos", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Provinsi", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Kabupaten", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kecamatan", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Kelurahan", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

