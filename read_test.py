#! /usr/bin/python
import smbus
from time import sleep
import config
from Kabel import KABEL

# def setup():
#     # Instanz von SMbus anlegen, ist nur einmal notwendig
#     bus = smbus.SMBus(1)
#     return bus
# 
# bus=setup()
# 
# bus.write_byte_data(0x21, 0x00, 0xFF)
# bus.write_byte_data(0x21, 0x01, 0x00)
# 
# #bus.write_byte_data(0x21, 0x14, 0x00)
# bus.write_byte_data(0x21, 0x15, 0xFF)
# #sleep(2)
# werte = bus.read_byte_data(0x21, 0x12)
# print(hex(werte))  #A wurde als input verwendet, B als Output
# # bei Verbindung von reihe a und reihe b wird ausgegeben an welchem Pin von A was anliegt
# #print(werte)

b = "00000001"

print(hex(int("00000001")))

def setze_pin_auf_high(adresse, aktion, pin):
    for stein in config.ADRESSEN_STEINE.values():
        if aktion == "A":
            bus.write_byte_data(stein, config.AKTION.get("DIRA"), 0x00)
            bus.write_byte_data(stein, config.AKTION.get("DIRB"), 0x00)
            bus.write_byte_data(stein, config.AKTION.get("OUTA"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("OUTB"), 0xFF)
            #bus.write_byte_data(stein, config.AKTION.get("GPPUA"), 0xFF)
            #bus.write_byte_data(stein, config.AKTION.get("GPPUB"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("DIRA"), 0xFF)
            bus.write_byte_data(stein, config.AKTION.get("DIRB"), 0xFF)
       # bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("GPPUA"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
        bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse),config.AKTION.get("OUTA"), config.PINNUMMERN.get(pin))#config.PINNUMMERN.get(pin))
    sleep(2)
    bus.write_byte_data(config.ADRESSEN_STEINE.get(adresse), config.AKTION.get("OUTA"), 0x00)