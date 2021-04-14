from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog
import config
import GUI_config

class Ui_Dialog(QDialog):
    def __init__(self, dialog):
        super(Ui_Dialog, self).__init__(None)
        xpos = 0
        ypos = 0
        dialog.resize(GUI_config.mainwindowsize[0], GUI_config.mainwindowsize[1])
        
        for i in range(len(config.FEHLER)):
            self.textEdit = QtWidgets.QTextEdit(dialog)
            self.textEdit.setText(config.FEHLER[i])
            self.textEdit.setGeometry(QtCore.QRect(xpos, ypos, GUI_config.textEditsize[0], GUI_config.textEditsize[1]))
            ypos  += 1*GUI_config.textEditsize[1]
            print(ypos)
            
        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, Dialog):
        __translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(__translate("Dialog", "Fehler"))

def open_dialog(Dialog):
    Dialog.show()
    Dialog.exec_()
        
def create_dialog():
    Dialog = QtWidgets.QDialog()
    Ui_Dialog(Dialog)
    return Dialog