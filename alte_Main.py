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

def setze_pin_auf_high(adresse, aktion, pin):
    for stein in config.ADRESSEN_STEINE.values():
        if aktion == "A":
            pi_gpio_setup_as_out_and_high()
            bus.write_byte_data(stein, config.AKTION.get("GPPUA"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("GPPUB"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("DIRA"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("DIRB"), 0xFF)
            bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("DIRA"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
            bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("OUTA"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
        elif aktion=="B":
            pi_gpio_setup_as_out_and_high()
            bus.write_byte_data(stein, config.AKTION.get("GPPUA"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("GPPUB"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("DIRA"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("DIRB"), 0xFF)
            bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("DIRB"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
            bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("OUTB"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
        else:
           gpio.setup(int(pin), gpio.OUT) 
           gpio.output(int(pin), gpio.LOW)
    #sleep(0.5)

def string_zu_befehl(string):
    adresse = string[:1]
    aktion = string[1:2]
    pin = string[2:4]
    return adresse, aktion, pin

def checke_werte():
    werte1 = bus.read_byte_data(0x21, 0x12)
    werte2 = bus.read_byte_data(0x26, 0x12)
    werte3 = bus.read_byte_data(0x22, 0x12)
    werte4 = bus.read_byte_data(0x24, 0x12)
    werte5 = bus.read_byte_data(0x20, 0x12)
    werte6 = bus.read_byte_data(0x21, 0x13)
    werte7 = bus.read_byte_data(0x26, 0x13)
    werte8 = bus.read_byte_data(0x22, 0x13)
    werte9 = bus.read_byte_data(0x24, 0x13)
    werte10 = bus.read_byte_data(0x20, 0x13)
    print("stein1:", hex(werte1),"stein2:", hex(werte2),"stein3:", hex(werte3),"stein4:", hex(werte4),"stein5:", hex(werte5))
    print("stein1:", hex(werte6),"stein2:", hex(werte7),"stein3:", hex(werte8),"stein4:", hex(werte9),"stein5:", hex(werte10))
   

def pi_gpio_setup_as_out_and_high():
    gpio.setwarnings(False)
    for i in range( len(config.GPIOS)):
        gpio.setup(config.GPIOS[i], gpio.OUT)
        gpio.output(config.GPIOS[i], gpio.HIGH)
        
        
def iteration():
    steinnummer = 1
    pinnummer = 0
    pinnummerb = 0 
    litzenzahl = 100  #kommt später von GUI
    gpio_nummer= 0
    for i in range(litzenzahl):
        if steinnummer == 4:
            if pinnummer < 2:
                pinnummer +=1
                string = str(steinnummer) + "A" + str(pinnummer)
                #Wenn alle 5 Steine durch, dann muss der Pi herhalten
            else:
                if gpio_nummer <=20: #alle 20 pins durchgehen
                    string = "r" + "p" + str(config.GPIOS[gpio_nummer])
                    gpio_nummer +=1    
                else:
                    break
        else:  
            if pinnummer <= 7: # Pin 1-7 auf Reihe A durchgehen
                pinnummer +=1
                string = str(steinnummer) + "A" + str(pinnummer)
            elif pinnummerb <= 7: # Pin 8-16 auf Reihe B durchgehen
                pinnummerb +=1
                string = str(steinnummer) + "B" + str(pinnummerb)   
            else:
                steinnummer += 1
                pinnummer = 1
                pinnummerb = 0
                string = str(steinnummer) + "A" + str(pinnummer)
        
        adresse, aktion, pin = string_zu_befehl(string)
        print(steinnummer, adresse, aktion,pin)
        setze_pin_auf_high(adresse, aktion, pin)
        checke_werte()    
       
bus = setup()
# Reihentests funktionieren
#led_test_Reihe_A("1", "3") 
#led_test_Reihe_B("1", "4")
#setze_pin_auf_high("1", "OUTA", "1") #Stein, "OUTA" oder "OUTB", Pinnummer
#adresse, aktion, pin = string_zu_befehl("1OUTA5") # zieht String auseinander in die Teilstrings
#setze_pin_auf_high(adresse, aktion, pin) #übergibt Einzelstrings an Methode wie oben
iteration()