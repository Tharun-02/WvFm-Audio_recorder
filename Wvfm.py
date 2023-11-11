import pyaudio
import wave
import keyboard
from datetime import datetime

audio = pyaudio.PyAudio()
format= pyaudio.paInt16
stream = audio.open(format=format,
                    channels= 1,
                    rate=44100,
                    input=True,
                    frames_per_buffer=1024)
print("""--/Recording Started... 
      Press 'Space' to stop recording.""")
frames=[]

try:
    while True:
        data= stream.read(1024)
        frames.append(data)
        
        if keyboard.is_pressed("space"):
            break
except KeyboardInterrupt:
    pass
finally:
    print("--/Recording finished.")
    
stream.stop_stream()
stream.close()
audio.terminate()

timestamp = datetime.now().strftime("%y%m%d%H%M%S")
file_name = f"Recording_{timestamp}.wav"

sound_file = wave.open(file_name,"wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(format))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()


