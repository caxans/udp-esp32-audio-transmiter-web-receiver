#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = ""; //Wifi SSID
const char* password = ""; //Wifi password

WiFiUDP Udp; 

void setup() {
  Serial.begin(115200);
  Serial.println();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  IPAddress Ip(192, 168, 1, 180);
  IPAddress Gateway(192, 168, 1, 1);
  IPAddress Subnet(255, 255, 255, 0);
  WiFi.config(Ip, Gateway, Subnet);

  Serial.println("");
  Serial.println("WiFi conectado");
  Serial.println(WiFi.localIP());
}

void loop() {
  Udp.beginPacket(IPAddress(192, 168, 1, 8), 1234);

  for (int i = 0; i < 1024; i++) {
    int old = micros();

    float analogValue = analogRead(34);

    analogValue = constrain(analogValue, 0, 4095);
    analogValue = map(analogValue, 0, 4095, 0, 255);

    Udp.write((uint8_t)analogValue);

    while (micros() - old < 87);
  }

  Udp.endPacket();
  //delay(1); //Only for test
}