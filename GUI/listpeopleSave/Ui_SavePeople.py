# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\EMatt\OneDrive - Nova Scotia Community College\w0420789-MatthewsE\Programming\Git Repository\w0420789-MatthewsE\GUI\listpeopleSave\SavePeople.ui'
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
        self.listWidgetFileList = QtWidgets.QListWidget(self.centralwidget)
        self.listWidgetFileList.setGeometry(QtCore.QRect(25, 20, 291, 521))
        self.listWidgetFileList.setObjectName("listWidgetFileList")
        self.UpdatePersonButton = QtWidgets.QPushButton(self.centralwidget)
        self.UpdatePersonButton.setGeometry(QtCore.QRect(450, 240, 241, 61))
        self.UpdatePersonButton.setObjectName("UpdatePersonButton")
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
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_People = QtWidgets.QAction(MainWindow)
        self.actionLoad_People.setObjectName("actionLoad_People")
        self.actionSave_to_File = QtWidgets.QAction(MainWindow)
        self.actionSave_to_File.setObjectName("actionSave_to_File")
        self.menuFile.addAction(self.actionLoad_People)
        self.menuFile.addAction(self.actionSave_to_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.UpdatePersonButton.setText(_translate("MainWindow", "Update Person"))
        self.NameLabel.setText(_translate("MainWindow", "NAME:"))
        self.AgeLabel.setText(_translate("MainWindow", "AGE:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_People.setText(_translate("MainWindow", "Load People"))
        self.actionSave_to_File.setText(_translate("MainWindow", "Save to File"))

