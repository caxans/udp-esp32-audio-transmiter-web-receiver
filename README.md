# udp-esp32-audio-transmiter-web-receiver
This project allows you to transmit audio through a jack connection to the esp32 to a website with flask. UDP packets are used to transmit the live audio signal to the local network.

###How run the project

####Arduino configuration
The project works with esp32 module and need wifi connections on 2,4Ghz

1. Configure the arduino transmisor values:

- ssid: String with network name
- password: String with network password
- host: String with the internet domain where receiver the UPD packages
- port: Int with the internet port where receiver the UPD packages

Note: If you need test in local, uncomment lines with the descriptions

2. Upload the "transmisor_audio_esp32" to ESP32 develop module

Note: Check logs conections in the console

####Python configurations

1. Configure the udp audio receiver with the next environments:
 
- UDP_IP: Environment system with the IP value of host or you can set value 0.0.0.0 for general host on the running application
- UDP_PORT: Enviroment system with the port value of the channel receive the UDP package, same the arduino configuration port
- AUDIO_PATH_OUTPUT1: Path will be save the audio files .wav, for example: "/files/output/output1.wav"
- AUDIO_PATH_OUTPUT2: Path will be save the audio files .wav, for example: "/files/output/output2.wav"

Note: AUDIO_PATH_OUTPUT1 and AUDIO_PATH_OUTPUT2 the same path to server

2. Configure the server with the next environments:

- TEMPLATE_DIR: The index.html folder or other files, for example: "templates"
- AUDIO_PATH_OUTPUT1: Path will be save the audio files .wav, for example: "/files/output/output1.wav"
- AUDIO_PATH_OUTPUT2: Path will be save the audio files .wav, for example: "/files/output/output2.wav"

Note: AUDIO_PATH_OUTPUT1 and AUDIO_PATH_OUTPUT2 udp audio receiver

3. Run the server file with command:

```bash
uvicorn server:app --host 0.0.0.0 --port 5000
```

Note: The command path execution must be the "server.py" file

4. If the command print errors, it could be a Python dependencies, the solution is install the requirements