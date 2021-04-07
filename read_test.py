#! /usr/bin/python
import smbus
from time import sleep
import config
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Mainwindow import Ui_MainWindow

def createWindow():
    app = QtWidgets.QApplication(sys.argv)
    Hauptfenster = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    return app, ui, Hauptfenster

def open_and_execute_window(app, ui, Hauptfenster):
    ui.setupUi(Hauptfenster)
    Hauptfenster.show()
    sys.exit(app.exec_())
    
app, ui, Hauptfenster = createWindow()
open_and_execute_window(app, ui, Hauptfenster)
