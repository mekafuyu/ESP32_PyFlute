import socket as Socket

class addressNotFound(Exception):
    pass

class alreadyConnected(Exception):
    pass

class BluetoothConnection:
    def __init__(self, address:str, port:int=None, wordSize:int=1) -> None:
        self.address = address
        self.port = port
        self._socket = Socket.socket(Socket.AF_BLUETOOTH, Socket.SOCK_STREAM, Socket.BTPROTO_RFCOMM)
        self._connected:bool = False
        self.wordSize = wordSize
    
    def tryFindPort(self):
        for i in range(99999):
            try:
                self._socket.connect((self.address, i))
                self._connected = True
                
                return i
            except:
                pass
        raise addressNotFound("Couldn't connect to the given address.")  
    
    def connect(self):
        if (self._connected):
            raise alreadyConnected("Device already connected.")
        
        if (self.port != None):
            try:
                self._socket.connect((self.address, self.port))
                self._connected = True
                return
            except:
                raise addressNotFound("Couldn't connect to the given address.")
        
        raise addressNotFound("Bluetooth connection does not have any port.")
    
    def connection(self):
        if (self._connected):
            return ("Connected to: " + str(self.address) + " : "  + str(self.port))
        return "not connected yet."
            
    def getPressedFromBT(self):
        return self._socket.recv(self.wordSize)
