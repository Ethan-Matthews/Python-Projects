# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\EMatt\OneDrive - Nova Scotia Community College\w0420789-MatthewsE\Programming\Git Repository\w0420789-MatthewsE\GUI\loadpeople.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(25, 20, 291, 521))
        self.listWidget.setObjectName("listWidget")
        self.LoadPeopleButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoadPeopleButton.setGeometry(QtCore.QRect(450, 240, 241, 61))
        self.LoadPeopleButton.setObjectName("LoadPeopleButton")
        self.NameField = QtWidgets.QLineEdit(self.centralwidget)
        self.NameField.setGeometry(QtCore.QRect(450, 111, 231, 31))
        self.NameField.setObjectName("NameField")
        self.AgeField = QtWidgets.QLineEdit(self.centralwidget)
        self.AgeField.setGeometry(QtCore.QRect(450, 160, 231, 31))
        self.AgeField.setObjectName("AgeField")
        self.NameLabel = QtWidgets.QLabel(self.centralwidget)
        self.NameLabel.setGeometry(QtCore.QRect(400, 110, 41, 31))
        self.NameLabel.setObjectName("NameLabel")
        self.AgeLabel = QtWidgets.QLabel(self.centralwidget)
        self.AgeLabel.setGeometry(QtCore.QRect(400, 160, 41, 31))
        self.AgeLabel.setObjectName("AgeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.LoadPeopleButton.setText(_translate("MainWindow", "Load People"))
        self.NameLabel.setText(_translate("MainWindow", "NAME:"))
        self.AgeLabel.setText(_translate("MainWindow", "AGE:"))

