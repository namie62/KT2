#! /usr/bin/python
import smbus
from time import sleep
import config
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from Mainwindow import Ui_MainWindow
import pruefprogramm

def createWindow():
    app = QtWidgets.QApplication(sys.argv)
    Hauptfenster = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    return app, ui, Hauptfenster

def open_and_execute_window(app, ui, Hauptfenster, pruefungsinstanz):
    ui.setupUi(Hauptfenster, pruefungsinstanz)
    Hauptfenster.show()
    sys.exit(app.exec_())
    
# Hier beginnt das Hauptprogramm 
if __name__ == "__main__":
    app, ui, Hauptfenster = createWindow()  #erstellt das Hauptfenster und dessen Instanz
    pruefungsinstanz = pruefprogramm.pruefung()  #erstellt die Instanz des Prüfprogramms
    open_and_execute_window(app, ui, Hauptfenster, pruefungsinstanz) #öffnet das Hauptfenster und übergibt die Prüfungsinstanz
