# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\EMatt\OneDrive - Nova Scotia Community College\w0420789-MatthewsE\Programming\Git Repository\w0420789-MatthewsE\GUI\ColoursDemo\ColoursDemo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1313, 840)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxColours = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxColours.setGeometry(QtCore.QRect(460, 260, 120, 114))
        self.groupBoxColours.setObjectName("groupBoxColours")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxColours)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButtonRed = QtWidgets.QRadioButton(self.groupBoxColours)
        self.radioButtonRed.setObjectName("radioButtonRed")
        self.gridLayout.addWidget(self.radioButtonRed, 0, 0, 1, 1)
        self.radioButtonBlue = QtWidgets.QRadioButton(self.groupBoxColours)
        self.radioButtonBlue.setObjectName("radioButtonBlue")
        self.gridLayout.addWidget(self.radioButtonBlue, 1, 0, 1, 1)
        self.radioButtonGreen = QtWidgets.QRadioButton(self.groupBoxColours)
        self.radioButtonGreen.setObjectName("radioButtonGreen")
        self.gridLayout.addWidget(self.radioButtonGreen, 2, 0, 1, 1)
        self.PushButtonDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.PushButtonDisplay.setGeometry(QtCore.QRect(459, 390, 120, 28))
        self.PushButtonDisplay.setObjectName("PushButtonDisplay")
        self.labeluserLabel = QtWidgets.QLabel(self.centralwidget)
        self.labeluserLabel.setGeometry(QtCore.QRect(460, 500, 120, 16))
        self.labeluserLabel.setText("")
        self.labeluserLabel.setObjectName("labeluserLabel")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(460, 440, 120, 22))
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1313, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxColours.setTitle(_translate("MainWindow", "Colours"))
        self.radioButtonRed.setText(_translate("MainWindow", "Red"))
        self.radioButtonBlue.setText(_translate("MainWindow", "Blue"))
        self.radioButtonGreen.setText(_translate("MainWindow", "Green"))
        self.PushButtonDisplay.setText(_translate("MainWindow", "PushButton"))

