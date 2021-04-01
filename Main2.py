#! /usr/bin/python
import smbus
from time import sleep
import config
from Kabel import KABEL
import RPi.GPIO as gpio

def setup():
    # Instanz von SMbus anlegen, ist nur einmal notwendig
    bus = smbus.SMBus(1)
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    return bus

# # lässt testhalber alle LEDs von Reihe B aus für 3 Sek leuchten am übergebenen Stein
# def led_test_Reihe_B(stein, pin):
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x00, 0x00)
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x01, 0x00)
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x15, config.PINNUMMERN.get(pin))
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x14, 0x00)
#     sleep(3)
#     bus. write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x15, 0x00)
#     
# # lässt testhalber alle LEDs von Reihe A aus für 3 Sek leuchten am übergebenen Stein
# def led_test_Reihe_A(stein, pin):
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x00, 0x00)
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x01, 0x00)
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x14, config.PINNUMMERN.get(pin))
#     bus.write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x15, 0x00)
#     sleep(3)
#     bus. write_byte_data(config.ADRESSEN_STEINE.get(stein), 0x14, 0x00)
#     
# # von bin zu hex (nicht benötigt)
# def bin2hex(b):
#     i = int(b, 2)
#     h = hex(i)
#     return h
def setze_pin_auf_low(adresse, aktion, pin):
    setze_pullup_und_output()
    setze_pi_pins_zurueck()
    if aktion == "A":
        bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("DIRA"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
        bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("OUTA"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
    elif aktion=="B":
        bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("DIRB"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
        bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("OUTB"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
    else:
        pi_gpio_setup_as_out_and_high(int(pin))
    #sleep(0.5)

def string_zu_befehl(string):
    adresse = string[:1]
    aktion = string[1:2]
    pin = string[2:4]
    return adresse, aktion, pin

def checke_werte():#adresse, aktion):
    werte1a = bus.read_byte_data(0x21, 0x12)
    werte2a = bus.read_byte_data(0x26, 0x12)
    werte3a = bus.read_byte_data(0x22, 0x12)
    werte4a = bus.read_byte_data(0x24, 0x12)
    werte5a = bus.read_byte_data(0x20, 0x12)
    werte1b = bus.read_byte_data(0x21, 0x13)
    werte2b = bus.read_byte_data(0x26, 0x13)
    werte3b = bus.read_byte_data(0x22, 0x13)
    werte4b = bus.read_byte_data(0x24, 0x13)
    werte5b = bus.read_byte_data(0x20, 0x13)
    lese_gpios_aus()    
    print("stein1a:", hex(werte1a),"stein2a:", hex(werte2a),"stein3a:", hex(werte3a),"stein4a:", hex(werte4a),"stein5a:", hex(werte5a))
    print("stein1b:", hex(werte1b),"stein2b:", hex(werte2b),"stein3b:", hex(werte3b),"stein4b:", hex(werte5b),"stein5b:", hex(werte5b))
    
def pi_gpio_setup_as_out_and_high(pin):
    gpio.setup(pin, gpio.OUT) 
    gpio.output(pin, gpio.LOW)

def setze_pi_pins_zurueck():
    for pin in config.GPIOS:
        gpio.setup(pin, gpio.IN, pull_up_down = gpio.PUD_UP) 
        #gpio.output(pin, gpio.LOW)

def lese_gpios_aus():
    liste = []
    l = []
    for pin in range(20):
        liste.append(gpio.input(config.GPIOS[pin]))
        l.append(config.GPIOS[pin])
        #print(config.GPIOS[pin],gpio.input(config.GPIOS[pin]))
    print(l,liste)   
def setze_pullup_und_output():
    for stein in config.ADRESSEN_STEINE.values():
        bus.write_byte_data(stein, config.AKTION.get("GPPUA"), 0xFF)
        bus.write_byte_data(stein, config.AKTION.get("GPPUB"), 0xFF)
        bus.write_byte_data(stein, config.AKTION.get("DIRA"), 0xFF)
        bus.write_byte_data(stein, config.AKTION.get("DIRB"), 0xFF)

def iteration():
    steinnummer = 1
    pinnummer = 0
    pinnummerb = 0 
    litzenzahl = 100  #kommt später von GUI
    gpio_nummer= 0
    for i in range(litzenzahl):
        if steinnummer < 4:
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
        else: # steinnummer = 4
            if pinnummer < 2: # muss nur bis Pin2 gehen und dann auf Pi switchen
                pinnummer +=1
                string = str(steinnummer) + "A" + str(pinnummer)   
            else: # switche auf Pi
                if gpio_nummer < 20: #alle 20 pins durchgehen
                    string = "r" + "p" + str(config.GPIOS[gpio_nummer])
                    gpio_nummer +=1    
                else:
                    break
        adresse, aktion, pin = string_zu_befehl(string)
        print(adresse, aktion, pin)
        setze_pin_auf_low(adresse, aktion, pin)
        checke_werte()
       
bus = setup()
# Reihentests funktionieren
#led_test_Reihe_A("1", "3") 
#led_test_Reihe_B("1", "4")
#setze_pin_auf_high("1", "OUTA", "1") #Stein, "OUTA" oder "OUTB", Pinnummer
#adresse, aktion, pin = string_zu_befehl("1OUTA5") # zieht String auseinander in die Teilstrings
#setze_pin_auf_high(adresse, aktion, pin) #übergibt Einzelstrings an Methode wie oben
iteration()
