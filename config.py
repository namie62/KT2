# Alle Steinadressen auf Variablen legen (Aufgrund von unpraktischer Hardware-Addressierung sind die nicht in der richtigen Reihenfolge) 

ADRESSEN_STEINE = {
    "1" : 0x21,
    "2" : 0x26,
    "3" : 0x22,
    "4" : 0x24,
    "5" : 0x20}

# von jedem Stein einzeln iterierbar
PINNUMMERN = {
    "1" : 0xFE,
    "2" : 0xFD,
    "3" : 0xFB,
    "4" : 0xF7,
    "5" : 0xEF,
    "6" : 0xDF,
    "7" : 0xBF,
    "8" : 0x7F}

PINNUMMERN2 = {
    "1" : 0x01,
    "2" : 0x02,
    "3" : 0x04,
    "4" : 0x08,
    "5" : 0x10,
    "6" : 0x20,
    "7" : 0x40,
    "8" : 0x80}

GPIOS = [4,14,15,17,18,27,22,23,24,8,7,0,1,5,6,12,13,19,16,26,20,21]

AKTION = {
    "DIRA" : 0x00,
    "DIRB" : 0x01,
    "OUTA" : 0x14,
    "OUTB" : 0x15,
    "GPPUA" : 0x0C,
    "GPPUB" : 0x0D}
    