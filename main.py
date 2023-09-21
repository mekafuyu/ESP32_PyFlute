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

count = 0

try:
    while(1):
        noteESP = list(btconn.getPressedFromBT())[0]
        print(noteESP)
        if(flute.isPlaying(noteESP)):
            count += 1
        else:
            count = 0
            Instrument.stopAll()
            flute.play(noteESP)
except:
    Instrument.stopAll()
    
