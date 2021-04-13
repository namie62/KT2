#! /usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Kabel import KABEL
from pprint import pprint
import GUI_config
from pruefprogramm import pruefung


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.pruefungsinstanz = pruefung()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(GUI_config.mainwindowsize[0], GUI_config.mainwindowsize[1])
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
    
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 131, 31))
        self.textBrowser.setObjectName("textBrowser")
        
        
        self.create_pushButton()
            
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
        
    def create_pushButton(self):
        button_liste = []
        posy = GUI_config.mainwindowsize[1]/5 
        for cable in range(len(list(KABEL))):
            posx = cable*GUI_config.buttonsize[0]
            if cable > 4:
                posx = (cable-5)*GUI_config.buttonsize[0]
                posy = GUI_config.mainwindowsize[1]/5  + 1*GUI_config.buttonsize[1]
            if cable >9:
                posx = (cable-10)*GUI_config.buttonsize[0]
                posy = GUI_config.mainwindowsize[1]/5  + 2*GUI_config.buttonsize[1]
            name = list(KABEL)[cable]
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(posx, posy, GUI_config.buttonsize[0], GUI_config.buttonsize[1]))
            #self.pushButton.setObjectName(list(KABEL)[kabel])
            self.pushButton.setText(name)
            self.pushButton.clicked.connect(self.starte_pruefung)
            #button_liste.append(self.pushButton)
        #return button_liste
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Kabel auswählen:</span></p></body></html>"))
        #self.pushButton.setText(_translate("MainWindow", "PushButton"))
        #self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        #self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
    def starte_pruefung(self):
        self.pruefungsinstanz.iteration()
        self.pruefungsinstanz.vergleiche_soll_ist()