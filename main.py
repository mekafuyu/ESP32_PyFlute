from instrument import Instrument
from bluetoothConnection import BluetoothConnection
import keyboard

NOTES_FILES = [
    [0, ]
]

BLUETOOTH_ADDRESS = '58:BF:25:9F:6A:86'

btconn = BluetoothConnection(BLUETOOTH_ADDRESS, 1, 1)
btconn.connect()
print(btconn.connection())

flute = Instrument()
flute.addNote(0, "./Sound/flute/c4.wav")
flute.addNote(1, "./Sound/flute/d4.wav")
flute.addNote(3, "./Sound/flute/e4.wav")
flute.addNote(4, "./Sound/flute/f4.wav")
flute.addNote(15, "./Sound/flute/g4.wav")
flute.addNote(31, "./Sound/flute/a4.wav")
flute.addNote(63, "./Sound/flute/b4.wav")

# flute.addNote(1, "./Sound/flute/c4.wav")
# flute.addNote(2, "./Sound/flute/d4.wav")
# flute.addNote(3, "./Sound/flute/e4.wav")
# flute.addNote(4, "./Sound/flute/f4.wav")
# flute.addNote(8, "./Sound/flute/g4.wav")
# flute.addNote(16, "./Sound/flute/a4.wav")
# flute.addNote(32, "./Sound/flute/b4.wav")

# flute.addNote(0,  "./Sound/ppl/c2.wav")
# flute.addNote(1,  "./Sound/ppl/d2.wav")
# flute.addNote(3,  "./Sound/ppl/e2.wav")
# flute.addNote(4,  "./Sound/ppl/f2.wav")
# flute.addNote(15, "./Sound/ppl/g2.wav")
# flute.addNote(31, "./Sound/ppl/a2.wav")
# flute.addNote(63, "./Sound/ppl/b2.wav")


count = 0
noteESP = 0
try:
    while(1):
        prevNote = noteESP
        noteESP = list(btconn.getPressedFromBT())[0]
        
        if (prevNote != noteESP):
            print(noteESP)
        if(flute.isPlaying(noteESP)):
            count += 1
        else:
            count = 0
            Instrument.stopAll()
            flute.play(noteESP)
except:
    Instrument.stopAll()
    
