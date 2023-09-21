from pydub import AudioSegment
import simpleaudio

WAVE = 0
PLAY = 1

class Instrument():
    def __init__(self) -> None:   
        # vetor com a seguinte estrutura
        #   index = numero_da_nota
        #   conteudo = [ WaveObject, PlayObject ]
        self._notes = [None]*64
    
    def isPlaying(self, note:int):
        if (not self._notes[note]):
            return False
        return self._notes[note][PLAY].is_playing()
    
    def play(self, note:int):
        try:
            self._notes[note][PLAY] = self._notes[note][WAVE].play()
        except:
            return "Not attached note."

    def stop(self, note:int):
        self._notes[note][PLAY].stop()
        
    def addNote(self, note:int, file:str):
        waveObject = simpleaudio.WaveObject.from_wave_file(file)
        self._notes[note] = [waveObject, waveObject.play()]
        self._notes[note][PLAY].stop()
        
    @staticmethod
    def stopAll():
        simpleaudio.stop_all()
        
        
        
        
        
        
        
        
    # def setAudioBuffer(self):
    #     return simpleaudio.play_buffer(
    #         self.audio.raw_data,
    #         self.audio.channels,
    #         self.audio.sample_width,
    #         self.audio.frame_rate
    #     )
    
    # def resetAudioBuffer(self):
    #     self.audioBuffer = self.setAudioBuffer()
    
    
    # def playWav(self ):
    #     try:
    #         self.audioBuffer = self.audio.play()
    #     except KeyboardInterrupt:
    #         self.audio.stop()
        

    #     return
    

