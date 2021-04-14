# Alle Steinadressen auf Variablen legen (Aufgrund von unpraktischer Hardware-Addressierung sind die nicht in der richtigen Reihenfolge) 

ADRESSEN_STEINE = {
    "1" : 0x21,
    "2" : 0x26,
    "3" : 0x22,
    "4" : 0x24,
    "5" : 0x20}

# setzt den jeweiligen pin auf low
PINNUMMERN = {
    "1" : 0xFE,
    "2" : 0xFD,
    "3" : 0xFB,
    "4" : 0xF7,
    "5" : 0xEF,
    "6" : 0xDF,
    "7" : 0xBF,
    "8" : 0x7F}

PINNUMMERN2 = { #setzt den jeweiligen pin auf high
    "1" : 0x01,
    "2" : 0x02,
    "3" : 0x04,
    "4" : 0x08,
    "5" : 0x10,
    "6" : 0x20,
    "7" : 0x40,
    "8" : 0x80}

GPIOS = [4,14,15,17,18,27,22,23,24,8,7,0,1,5,6,12,13,19,16,26]#,20,21]

AKTION = {
    "DIRA" : 0x00,
    "DIRB" : 0x01,
    "OUTA" : 0x14,
    "OUTB" : 0x15,
    "GPPUA" : 0x0C,
    "GPPUB" : 0x0D}


OUTPUTS =  {
1: '1A1',
 2: '1A2',
 3: '1A3',
 4: '1A4',
 5: '1A5',
 6: '1A6',
 7: '1A7',
 8: '1A8',
 9: '1B1',
 10: '1B2',
 11: '1B3',
 12: '1B4',
 13: '1B5',
 14: '1B6',
 15: '1B7',
 16: '1B8',
 17: '2A1',
 18: '2A2',
 19: '2A3',
 20: '2A4',
 21: '2A5',
 22: '2A6',
 23: '2A7',
 24: '2A8',
 25: '2B1',
 26: '2B2',
 27: '2B3',
 28: '2B4',
 29: '2B5',
 30: '2B6',
 31: 'rp4',
 32: 'rp14',
 33: 'rp15',
 34: 'rp17',
 35: 'rp18',
 36: 'rp27',
 37: 'rp22',
 38: 'rp23',
 39: 'rp24',
 40: 'rp8',
 41: 'rp7',
 42: 'rp0',
 43: 'rp1',
 44: 'rp5',
 45: 'rp6',
 46: 'rp12',
 47: 'rp13',
 48: 'rp19',
 49: 'rp16',
 50: 'rp26'}

INPUTS = {
 1: '2B7',
 2: '2B8',
 3: '3A1',
 4: '3A2',
 5: '3A3',
 6: '3A4',
 7: '3A5',
 8: '3A6',
 9: '3A7',
 10: '3A8',
 11: '3B1',
 12: '3B2',
 13: '3B3',
 14: '3B4',
 15: '3B5',
 16: '3B6',
 17: '3B7',
 18: '3B8',
 19: '4A1',
 20: '4A2',
 21: '4A3',
 22: '4A4',
 23: '4A5',
 24: '4A6',
 25: '4A7',
 26: '4A8',
 27: '4B1',
 28: '4B2',
 29: '4B3',
 30: '4B4',
 31: '4B5',
 32: '4B6',
 33: '4B7',
 34: '4B8',
 35: '5A1',
 36: '5A2',
 37: '5A3',
 38: '5A4',
 39: '5A5',
 40: '5A6',
 41: '5A7',
 42: '5A8',
 43: '5B1',
 44: '5B2',
 45: '5B3',
 46: '5B4',
 47: '5B5',
 48: '5B6',
 49: '5B7',
 50: '5B8'}

VERGLEICH_PINS ={}

ABSCHLUSSMELDUNGEN = {
    1 : "Falsch verdrahtet: richtig/falsch ..",
    2 : "Interner ERROR1",
    3 : "Interner ERROR2",
    4 : "Keine Verbindung: ",
    5: "Querschluss: ",
    6 : "Alles supi"}

FEHLER = []
QUERSCHLUSS_PINS = []