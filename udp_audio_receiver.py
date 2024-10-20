#import pyaudio #Local play
import socket
import wave
import time
import os

async def udp_audio_receiver():
    UDP_IP = os.environ.get('UDP_IP')
    UDP_PORT = int(os.environ.get('UDP_PORT'))

    #FORMAT = 32 #Local play
    WF_FORMAT = 1
    CHANNELS = 1
    RATE = 11111
    PACKAGE_SIZE = 1024
    SECONDS_PACKAGE_TIME = 30

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))

    #p = pyaudio.PyAudio() #Local play

    #stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True) #Local play

    output_file1 = os.environ.get('AUDIO_PATH_OUTPUT1')
    output_file2 = os.environ.get('AUDIO_PATH_OUTPUT2')

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
            wf.setnchannels(CHANNELS)
            #wf.setsampwidth(p.get_sample_size(FORMAT)) #Local play
            wf.setsampwidth(WF_FORMAT) #Online play
            wf.setframerate(RATE)

            start_time = time.time()

            while True:
                data, addr = sock.recvfrom(PACKAGE_SIZE)
                #stream.write(data) #Local play
                wf.writeframes(data)

                if time.time() - start_time >= SECONDS_PACKAGE_TIME:
                    break

            wf.close
                    
    except KeyboardInterrupt:
        print("Closing...")
        #stream.stop_stream() #Local play
        #stream.close() #Local play
        wf.close
        #p.terminate() #Local play