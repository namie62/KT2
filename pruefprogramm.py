#! /usr/bin/python
import smbus
from time import sleep
import config
from Kabel import KABEL
import RPi.GPIO as gpio
from pprint import pprint

class pruefung():
    def __init__(self):
        # Instanz von SMbus anlegen, ist nur einmal notwendig
        self.litzenzahl = 50
        self.bus = smbus.SMBus(1)
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)

    def setze_pin_auf_low(self, adresse, aktion, pin):
        self.setze_pullup_und_input()
        self.setze_pi_pins_zurueck()
        if aktion == "A":
            self.bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("DIRA"), config.PINNUMMERN.get(pin))
            self.bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("OUTA"), config.PINNUMMERN.get(pin))
        elif aktion=="B":
            self.bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("DIRB"), config.PINNUMMERN.get(pin))
            self.bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("OUTB"), config.PINNUMMERN.get(pin))
        else:
            self.pi_gpio_setup_as_out_and_low(int(pin))
     
    def string_zu_befehl(self,string):
        adresse = string[:1]
        aktion = string[1:2]
        pin = string[2:4]
        return adresse, aktion, pin

    def checke_auf_durchgang(self,i):
        self.erstelle_dic(i) # erstellt einmal das Dictionary, indem alle pins die low sind aufgeführt werden
        rpi_toggle = False 
        for stein in config.ADRESSEN_STEINE:
            adresse = config.ADRESSEN_STEINE[stein] # holt sich adresse des jeweiligen steins
            wertea = self.lese_werte(stein, adresse , "A") #Werte von jedem stein von reihe a
            werteb = self.lese_werte(stein, adresse , "B")

            bin_reihe_a = self.rechne_werte_um_in_bin(wertea)  # hex wert in bin string umwandeln
            bin_reihe_b = self.rechne_werte_um_in_bin(werteb)
            
            low_pinsa = self.ermittle_low_pins_aus_bin(bin_reihe_a) # bin string durchgehen und 0en
            low_pinsb = self.ermittle_low_pins_aus_bin(bin_reihe_b)# die 0en dann in liste abspeichern
                    
            for pin in low_pinsa: # Um jeden der Low pins den passenden String packen und ins Dictionary abspeichern
                a = str(stein) + "A" + str(pin)
                self.packe_low_pins_in_dic(i, a, rpi_toggle)
            for pin in low_pinsb:
                b = str(stein) + "B" + str(pin)
                self.packe_low_pins_in_dic(i, b, rpi_toggle )
        
        rpi_toggle = True
        gpio_liste =self.lese_gpios_aus() #hier gpio low pins finden und ebenfalls in liste packen
        low_gpio_index = self.ermittle_low_gpio_index(gpio_liste)
        for gpio in low_gpio_index:
            c = "r" + "p" + str(config.GPIOS[gpio])
            self.packe_low_pins_in_dic(i,c, rpi_toggle)

    def ermittle_low_gpio_index(self,gpio_liste):
        wdh = len(gpio_liste)
        low_gpios = []
        for i in range(wdh):
            gpio_liste[i] = str(gpio_liste[i])
            if gpio_liste[i] == "0":
                low_gpios.append(i)
        return low_gpios

    def hole_gpio_nummern(self,low_gpio_index):
        gpio_nummern = []
        for i in low_gpio_index:
            gpio_nummern.append(config.GPIOS[i])
        return gpio_nummern
                

    def lese_werte(self, i, adresse, reihe):
        if reihe  == "A":
            werte = self.bus.read_byte_data(adresse, 0x12)
        else: 
            werte = self.bus.read_byte_data(adresse, 0x13)
        return werte
       
    def rechne_werte_um_in_bin(self,wert):
        h = str(hex(wert))
        scale = 16
        num_of_bits= 8
        b = bin(int(h, scale))[2:].zfill(num_of_bits)
        return b

    def ermittle_low_pins_aus_bin(self,bin_reihe_a):#, bin_reihe_b, stein, i):
        low_pins = []
        for buchstabennummer in range(len(bin_reihe_a)):
            if bin_reihe_a[buchstabennummer] == "0":
                low_pins.append(8-buchstabennummer)
        return low_pins

    def erstelle_dic(self,i):
            config.VERGLEICH_PINS[i+1] = []
        
    def packe_low_pins_in_dic(self, i, low_pin, rpi_toggle):
        if rpi_toggle:
            config.VERGLEICH_PINS[i+1].insert(0, low_pin)
        else: 
            config.VERGLEICH_PINS[i+1].append(low_pin) 
            
    def pi_gpio_setup_as_out_and_low(self, pin):
        gpio.setup(pin, gpio.OUT) 
        gpio.output(pin, gpio.LOW)

    def setze_pi_pins_zurueck(self):
        for pin in config.GPIOS:
            gpio.setup(pin, gpio.IN, pull_up_down = gpio.PUD_UP) 
            #gpio.output(pin, gpio.LOW)

    def lese_gpios_aus(self):
        liste = []
        l = []
        for pin in range(20):
            liste.append(gpio.input(config.GPIOS[pin]))
            l.append(config.GPIOS[pin])
        return liste # liste mit 1en und 0en je nachdem welcher pin high
        
    def setze_pullup_und_input(self):
        for stein in config.ADRESSEN_STEINE.values():
            self.bus.write_byte_data(stein, config.AKTION.get("GPPUA"), 0xFF)
            self.bus.write_byte_data(stein, config.AKTION.get("GPPUB"), 0xFF)
            self.bus.write_byte_data(stein, config.AKTION.get("DIRA"), 0xFF)
            self.bus.write_byte_data(stein, config.AKTION.get("DIRB"), 0xFF)

    def iteration(self):
        litzenzahl = self.litzenzahl
        steinnummer = 1
        pinnummer = 0
        pinnummerb = 0 
        gpio_nummer= 0
        #erstelle_dic(litzenzahl)
        for i in range(litzenzahl):
            if steinnummer < 2:
                if pinnummer <= 7: # Pin 1-7 auf Reihe A durchgehen
                    pinnummer +=1
                    string = str(steinnummer) + "A" + str(pinnummer)
                elif pinnummerb <= 7: # Pin 8-16 auf Reihe B durchgehen
                    pinnummerb +=1
                    string = str(steinnummer) + "B" + str(pinnummerb)   
                else: # Wenn alle 16 Pins auf einem Stein durch, dann werden die Variablen resettet und der Stein gewechselt
                    steinnummer += 1
                    pinnummer = 1
                    pinnummerb = 0
                    string = str(steinnummer) + "A" + str(pinnummer)
            else: # steinnummer = 3
                if pinnummer <= 7:
                    pinnummer +=1
                    string = str(steinnummer) + "A" + str(pinnummer)
                elif pinnummerb < 6: # muss nur bis Pin6 gehen und dann auf Pi switchen
                    pinnummerb +=1
                    string = str(steinnummer) + "B" + str(pinnummerb)   
                else: # switche auf Pi
                    if gpio_nummer < 20: #alle 20 pins durchgehen
                        string = "r" + "p" + str(config.GPIOS[gpio_nummer])
                        gpio_nummer +=1    
                    else:
                        break
            adresse, aktion, pin = self.string_zu_befehl(string)
            self.setze_pin_auf_low(adresse, aktion, pin)
            self.checke_auf_durchgang(i)
            
    def ermittle_fehlende_verbindung(self, i):
        print(config.ABSCHLUSSMELDUNGEN.get(4)+ config.VERGLEICH_PINS[i+1][0])
                
    def ueberpruefe_verdrahtung(self,i):
        if config.VERGLEICH_PINS[i+1][0] != config.OUTPUTS[i+1]:
            print(config.ABSCHLUSSMELDUNGEN.get(2))
        elif config.VERGLEICH_PINS[i+1][0] != config.OUTPUTS[i+1]:
            print(config.ABSCHLUSSMELDUNGEN.get(2))
        elif config.VERGLEICH_PINS[i+1][1] != config.INPUTS[i+1]:
            print(config.ABSCHLUSSMELDUNGEN.get(1) + config.OUTPUTS[i+1] + "->" + config.INPUTS[i+1] + "/" +config.OUTPUTS[i+1] + "->" + config.VERGLEICH_PINS[i+1][1] )
        else: pass

    def ermittle_querschluss(self,i, anzahl_verbundener_pins):
        querschluss_liste = []
        if config.VERGLEICH_PINS[i+1][0] != config.OUTPUTS[i+1]:
                print(config.ABSCHLUSSMELDUNGEN.get(2))
        else:
            for j in range(anzahl_verbundener_pins):
                querschluss_liste.append(config.VERGLEICH_PINS[i+1][j])
            print(config.ABSCHLUSSMELDUNGEN.get(5)+config.OUTPUTS[i+1] + "->" + config.INPUTS[i+1] +"/" + config.OUTPUTS[i+1] + "->" )
            for k in range(len(querschluss_liste)):
                if k > 0:
                    print(querschluss_liste[k])
                
    def vergleiche_soll_ist(self):
        litzenzahl = self.litzenzahl
        for i in range(litzenzahl): 
            anzahl_verbundener_pins = len(config.VERGLEICH_PINS[i+1])
            if anzahl_verbundener_pins == 0:
                config.ABSCHLUSSMELDUNGEN.get(3)
            if anzahl_verbundener_pins == 1: # Nur der gesetzte Pin ist high -> keine 
                self.ermittle_fehlende_verbindung(i)
            elif anzahl_verbundener_pins == 2: # zwei verbundene Pins, also korrekt, muss aber geprüft werden auf falsche Verdrahtung
                self.ueberpruefe_verdrahtung(i)
            elif anzahl_verbundener_pins > 2: # mehr als zwei verbundene Pins -> Querschluss
                self.ermittle_querschluss(i, anzahl_verbundener_pins) 
        
#     def starte_pruefung(self):
#         self.iteration()
#         self.vergleiche_soll_ist()
    
   
