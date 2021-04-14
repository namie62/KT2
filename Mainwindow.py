#! /usr/bin/python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from Kabel import KABEL
from pprint import pprint
import GUI_config
import ergebnisfenster
import config

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, pruefungsinstanz):
        
        self.pruefungsinstanz = pruefungsinstanz 
        self.MainWindow = MainWindow  
        
        # Größe des Fensters auf unseren Bildschirm angepasst und Titel festlegen
        MainWindow.resize(GUI_config.mainwindowsize[0], GUI_config.mainwindowsize[1])
        MainWindow.setWindowTitle(GUI_config.mainwindowtitle)

        # erstellt das Textfeld oben
        self.create_textfeld()
        
        # erstellt für jedes Kabel im Dictionary in Kabel.py einen Knopf 
        self.create_pushbuttons()
        
    def create_textfeld(self):
        self.textEdit = QtWidgets.QTextEdit(self.MainWindow)
        self.textEdit.setText(GUI_config.mainwindow_textanzeige)         
        self.textEdit.setGeometry(QtCore.QRect(0, 0,GUI_config.mainwindowsize[0], GUI_config.textedit_size_in_fehleranzeige[1]))

    def create_pushbuttons(self):
        button_liste = []
        posy = GUI_config.y_position_knoepfe 
        for cable in range(len(list(KABEL))):
            posx = cable*GUI_config.buttonsize[0]
            if cable > 4:
                posx = (cable-5)*GUI_config.buttonsize[0]
                posy = GUI_config.y_position_knoepfe   + 1*GUI_config.buttonsize[1]
            if cable >9:
                posx = (cable-10)*GUI_config.buttonsize[0]
                posy = GUI_config.y_position_knoepfe   + 2*GUI_config.buttonsize[1]
            self.name = list(KABEL)[cable]
            self.pushButton = QtWidgets.QPushButton(self.MainWindow)
            self.pushButton.setGeometry(QtCore.QRect(posx, posy, GUI_config.buttonsize[0], GUI_config.buttonsize[1]))
            self.pushButton.setText(self.name)
            self.pushButton.clicked.connect(lambda checked, name = list(KABEL)[cable]: self.pruefung(name))

    def pruefung(self, name):
        config.FEHLER = []
        config.QUERSCHLUSS_PINS = []
        print(name, str(KABEL.get(name)))
        self.pruefungsinstanz.iteration(KABEL.get(name))
        self.pruefungsinstanz.vergleiche_soll_ist(KABEL.get(name))
        dialogfenster = ergebnisfenster.create_dialog(name, KABEL.get(name))
        ergebnisfenster.open_dialog(dialogfenster)