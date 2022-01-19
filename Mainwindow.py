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
        
        # mit self. vorne dran, sind die Variablen auch in Methoden aufrufbar, denen sie nicht übergeben wurden, wegen Instanz
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
        self.textEdit.setGeometry(QtCore.QRect(0, 0,GUI_config.mainwindowsize[0], GUI_config.label_size_in_fehleranzeige[1]*2))

    def create_pushbuttons(self): #erstellt für jedes Kabel in Kabel.py im Hauptfenster einen Knopf und verschiebt die Knopfposition entsprechend, damit sie nicht direkt übereinander landen
        posy = GUI_config.y_position_knoepfe 
        for cable in range(len(list(KABEL))):
            posx = cable*GUI_config.buttonsize[0]
            if cable >= 5: #passen bloß jeweils 5 in eine Zeile
                posx = (cable-5)*GUI_config.buttonsize[0]
                posy = GUI_config.y_position_knoepfe   + 1*GUI_config.buttonsize[1]
            if cable >= 10:
                posx = (cable-10)*GUI_config.buttonsize[0]
                posy = GUI_config.y_position_knoepfe   + 2*GUI_config.buttonsize[1]
            if cable >= 15:
                posx = (cable-15)*GUI_config.buttonsize[0]
                posy = GUI_config.y_position_knoepfe   + 3*GUI_config.buttonsize[1]
            if cable >= 20:
                posx = (cable-20)*GUI_config.buttonsize[0]
                posy = GUI_config.y_position_knoepfe   + 4*GUI_config.buttonsize[1]
            if cable >= 25:
                posx = (cable-25)*GUI_config.buttonsize[0]
                posy = GUI_config.y_position_knoepfe   + 5*GUI_config.buttonsize[1]
                
            self.name = list(KABEL)[cable] #holt sich den Kabelnahmen
            self.pushButton = QtWidgets.QPushButton(self.MainWindow) #erstellt Knopf
            self.pushButton.setGeometry(QtCore.QRect(posx, posy, GUI_config.buttonsize[0], GUI_config.buttonsize[1])) # legt Position und Größe des Knopfes fest
            self.pushButton.setText(self.name) # auf Knopf steht damit der Kabelname
            self.pushButton.clicked.connect(lambda checked, name = list(KABEL)[cable]: self.pruefung(name)) # verbindet Knopf mit Funktion
    
    # Methode, die nach jedem Knopfdruck ausgeführt wird.
    def pruefung(self, name):
        config.FEHLER = []
        config.QUERSCHLUSS_PINS = []
        self.pruefungsinstanz.iteration(KABEL.get(name)) # Prüfprogramm
        self.pruefungsinstanz.vergleiche_soll_ist(KABEL.get(name)) # checkt auf Fehler
        dialogfenster = ergebnisfenster.create_dialog(name, KABEL.get(name)) #erstellt Ergebnisfenster
        ergebnisfenster.open_dialog(dialogfenster) # öffnet Ergebnisfenster