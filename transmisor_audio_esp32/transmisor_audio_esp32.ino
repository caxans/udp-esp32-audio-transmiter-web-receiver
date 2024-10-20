#include <WiFi.h>
#include <WiFiUdp.h>

const char* ssid = ""; //Wifi SSID
const char* password = ""; //Wifi password
const char* host = ""; //Domain
unsigned int port = 12345; //Port

WiFiUDP Udp;
IPAddress remoteIP;

void setup() {
  Serial.begin(115200);
  Serial.println();

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  if (WiFi.hostByName(host, remoteIP)) {
    Serial.println("Resolved domain: " + String(remoteIP));
  } else {
    Serial.println("Error resolving domain");
  }
}

void loop() {
  //Udp.beginPacket(IPAddress(192, 168, 1, 8), port); //Local execution
  Udp.beginPacket(remoteIP, port);

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