#include <WiFi.h>
#include <FirebaseESP32.h>
#include "esp_bt_main.h"
#include "esp_bt_device.h"
#include "BluetoothSerial.h"


#define BT1 12
#define BT2 14
#define BT3 27
#define BT4 26
#define BT5 25
#define BT6 33

#define WIFI_NOME ""
#define WIFI_SENHA ""

#define FB_HOST "" // Link Firebase
#define FB_AUTH "" // Segredo Firebase

FirebaseJson json;
FirebaseData firebaseData;

BluetoothSerial SerialBT;

void printAdd()
{
  const uint8_t* point = esp_bt_dev_get_address();

  for (int i = 0; i < 6; i++)
  {
    char str[3];
    sprintf(str, "%02X", (int)point[i]);
    Serial.print(str);

    if (i < 5)
    {
      Serial.print(":");
    }
  }
}

void setup() {
  pinMode(BT1, INPUT_PULLDOWN);
  pinMode(BT2, INPUT_PULLDOWN);
  pinMode(BT3, INPUT_PULLDOWN);
  pinMode(BT4, INPUT_PULLDOWN);
  pinMode(BT5, INPUT_PULLDOWN);
  pinMode(BT6, INPUT_PULLDOWN);
  
  Serial.begin(115200);
  SerialBT.begin("ESP32Bluetooth - Flauta");

  WiFi.mode(WIFI_STA);
  WiFi.disconnect(); // boa prática

  WiFi.begin(WIFI_NOME, WIFI_SENHA);

  Serial.print("Conectando");

  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(100);
  }

  Firebase.begin(FB_HOST, FB_AUTH);

  Firebase.reconnectWiFi(true);
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  Firebase.setwriteSizeLimit(firebaseData, "tiny");
  
  printAdd();
}

void loop() {
  byte controlSignal = 0b00000000;
  Serial.println(digitalRead(BT1));
  if (digitalRead(BT1))
    controlSignal |= 0b000001;
  if (digitalRead(BT2))
    controlSignal |= 0b000010;
  if (digitalRead(BT3))
    controlSignal |= 0b000100;
  if (digitalRead(BT4))
    controlSignal |= 0b001000;
  if (digitalRead(BT5))
    controlSignal |= 0b010000;
  if (digitalRead(BT6))
    controlSignal |= 0b100000;

    json.set("/Notas");
    Firebase.updateNode(firebaseData, "/Otamabosch", json);
  
  SerialBT.write(controlSignal);
  delay(10);
}