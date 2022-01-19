from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QHBoxLayout, QWidget, QScrollArea
import config
import GUI_config

# Hier ist das Fenster implementiert, das aufgeht und die Fehler anzeigt
class Ui_Dialog(QDialog): # Ergebnisfenster ist ein Dialog von PyQt5 und geht auf nachdem das Prüfprogramm durchgelaufen ist.
    def __init__(self, dialog, Kabel, litzenzahl):
        super(Ui_Dialog, self).__init__(None)
        
        # sind die Koordinaten der einzelnen Fehlermeldungszeilen, die werden später entsprechend verschoben, damit die nicht unleserlich übereinander geschrieben werden
        xpos = 0
        ypos = GUI_config.fehlermeldungs_position[1]
        
        # legt namen des Fensters auf den Kabelnamen fest   
        dialog.setWindowTitle(Kabel)
        dialog.resize(GUI_config.mainwindowsize[0],GUI_config.mainwindowsize[1]) #legt Größe auf die selbe Größe wie Hauptfenster fest
        
        self.checke_ob_fehler_vorhanden() # wenn Fehler vorhanden, dann ist der toggle 1 und das Männchen mit Haken hat Urlaub
            
        if self.toggle == 1:
            #schreibt ein Textfeld für jeden Fehler und variiert die Position vom Label entsprechend
            for i in range(len(config.FEHLER)):
                if i > 18:
                    xpos = 255
                    ypos = (i-19)*GUI_config.label_size_in_fehleranzeige[1]
                if i > 36:
                    xpos = 505
                    ypos = (i-37)*GUI_config.label_size_in_fehleranzeige[1]
                if i > 54: #wenn mehr als 54 Fehler, dann ist eh mehr kaputt
                    xpos = 755
                    ypos = (i-55)*GUI_config.label_size_in_fehleranzeige[1]
                
                if config.FEHLER[i] == "Alles supi": #wenn bei einem bestimmten Pin kein Fehler erscheint, dann soll da in der Zeile im Ergebnisfenster auch nichts stehen
                    pass
                
                else: #wenn Fehler erscheint, schreibt er den ins Ergebnisfenster rein
                    self.label = QtWidgets.QLabel(dialog)
                    self.label.setText(config.FEHLER[i])
                    self.label.setGeometry(QtCore.QRect(xpos, ypos, GUI_config.label_size_in_fehleranzeige[0], GUI_config.label_size_in_fehleranzeige[1])) # legt Position und Größe der Fehlermeldung fest
                    ypos  += 1*GUI_config.label_size_in_fehleranzeige[1] # verschiebt die nächste Fehlermeldung dann um 1 nach unten
        else: #wenn kein Fehler, dann zeige Männchen mit Haken
            self.label = QtWidgets.QLabel(dialog)
            pixmap = QPixmap("/home/pi/KT2/Haken.jpg")
            self.label.setPixmap(pixmap)
                
    def checke_ob_fehler_vorhanden(self):
        #der Toggle wird zu 1 wenn ein Fehler auftritt, ansonsten bleibt er 0
        #wenn toggle 0 ist, dann trat kein Fehler auf und der Haken wird angezeigt statt der Fehlermeldungen
        self.toggle = 0
        for i in range(len(config.FEHLER)):
            print(config.FEHLER[i])
            if config.FEHLER[i] != "Alles supi":
                self.toggle = 1
            print(self.toggle)
            
# die nächsten beiden Methoden werden im Mainwindow aufgerufen, nachdem die Prüfung fertig ist
def open_dialog(Dialog):
    Dialog.show()
    Dialog.exec_()
        
def create_dialog(Kabel, litzenzahl):
    Dialog = QtWidgets.QDialog()
    Ui_Dialog(Dialog, Kabel, litzenzahl)
    return Dialog