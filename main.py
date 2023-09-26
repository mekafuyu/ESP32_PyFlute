from instrument import Instrument
from bluetoothConnection import BluetoothConnection
from firebaseConnection import ref
import notesMap

FLUTE_LIKE_NOTES = {0 : "Dó",
                    1 : "Ré",
                    3 : "Mi",
                    4 : "Fá",
                    15 : "Sol",
                    31 : "Lá",
                    63 : "Si"}

FLUTE_LIKE_NOTES_SHARP = { 63 : "Dó",
                     62 : "Dó#",
                     61 : "Ré",
                     60 : "Ré#",
                     56 : "Mi",
                     57 : "Fá",
                     58 : "Sol",
                     59 : "Lá",
                     48 : "Si"}

PIANO_LIKE_NOTES = {1 : "Dó",
                    2 : "Ré",
                    3 : "Mi",
                    4 : "Fá",
                    8 : "Sol",
                    16 : "Lá",
                    32 : "Si"}

# Select the sounds of Notes:
#   notesMap.fluteLikeMap    => NOTES = FLUTE_LIKE_NOTES
#   notesMap.fluteLikeMapSharp => NOTES = FLUTE_LIKE_NOTES_SHARP
#   notesMap.pianoLikeMap    => NOTES = PIANO_LIKE_NOTES
#   notesMap.pplFluteLikeMap => NOTES = FLUTE_LIKE_NOTES
PRESET = notesMap.fluteLikeMapSharp
NOTES = FLUTE_LIKE_NOTES_SHARP

BLUETOOTH_ADDRESS = '58:BF:25:9F:6A:86'
btconn = BluetoothConnection(BLUETOOTH_ADDRESS, 1, 1)
btconn.connect()
print(btconn.connection())

flute = Instrument()

for note in PRESET:
    flute.addNote(note , PRESET[note])

noteESP = 0

try:
    while(1):
        prevNote = noteESP
        noteESP = list(btconn.getPressedFromBT())[0]
          
        if (prevNote != noteESP):
            try:
                print(NOTES[noteESP])
                ref.update({ "Nota" : NOTES[noteESP] })
            except:
                pass

        if(not flute.isPlaying(noteESP)):
            Instrument.stopAll()
            flute.play(noteESP)
except:
    Instrument.stopAll()
    
