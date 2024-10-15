import pyaudio
import socket
import wave
import time

UDP_IP = "192.168.1.8"
UDP_PORT = 1234

FORMAT = 32
CHANNELS = 1
RATE = 11111
PACKAGE_SIZE = 1024
SECONDS_PACKAGE_TIME = 30

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

p = pyaudio.PyAudio()

#stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True) #Reproduccion local

output_file1 = 'files/source/output1.wav'
output_file2 = 'files/source/output2.wav'

audio_flag = True

try:
    while True:
        if audio_flag:
            output_file = output_file1
            audio_flag = False
        else:
            output_file = output_file2
            audio_flag = True

        wf = wave.open(output_file, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(11111)

        start_time = time.time()

        while True:
            data, addr = sock.recvfrom(PACKAGE_SIZE)
            #stream.write(data) #Reproduccion local
            wf.writeframes(data)

            if time.time() - start_time >= SECONDS_PACKAGE_TIME:
                break

        wf.close
                
except KeyboardInterrupt:
    print("Closing...")
    #stream.stop_stream() #Reproduccion local
    #stream.close() #Reproduccion local
    wf.close
    p.terminate()