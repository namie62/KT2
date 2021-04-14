from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QWidget, QScrollArea
import config
import GUI_config

class Ui_Dialog(QDialog):
    def __init__(self, dialog, Kabel, litzenzahl):
        super(Ui_Dialog, self).__init__(None)
        xpos = 0
        ypos = GUI_config.fehlermeldungs_position[1]
        
        # legt namen des Fensters auf den Kabelnamen fest   
        dialog.setWindowTitle(Kabel)
        dialog.resize(GUI_config.mainwindowsize[0],GUI_config.mainwindowsize[1])
        
        #schreibt ein Textfeld für jeden Fehler
        
        for i in range(len(config.FEHLER)):
            if i > 18:
                xpos = 250
                ypos = (i-19)*GUI_config.textedit_size_in_fehleranzeige[1]
            if i > 36:
                xpos = 500
                ypos = (i-37)*GUI_config.textedit_size_in_fehleranzeige[1]
            if i > 54:
                xpos = 750
                ypos = (i-55)*GUI_config.textedit_size_in_fehleranzeige[1]
            
            self.textEdit = QtWidgets.QLabel(dialog)
            self.textEdit.setText(config.FEHLER[i])
            self.textEdit.setGeometry(QtCore.QRect(xpos, ypos, GUI_config.textedit_size_in_fehleranzeige[0], GUI_config.textedit_size_in_fehleranzeige[1]))
            ypos  += 1*GUI_config.textedit_size_in_fehleranzeige[1]
            
def open_dialog(Dialog):
    Dialog.show()
    Dialog.exec_()
        
def create_dialog(Kabel, litzenzahl):
    Dialog = QtWidgets.QDialog()
    Ui_Dialog(Dialog, Kabel, litzenzahl)
    return Dialog