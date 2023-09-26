// DEPENDENCIES
#include "BluetoothSerial.h"

// HARDWARE MAPPING
const uint8_t BUTTONS[] = {12, 14, 27, 26, 25, 33};
const uint8_t BUTTONS_SIZE = 6;

// CONSTANTS
BluetoothSerial SerialBT;

// VARIABLES

// SETUP
void setup() {
  for (uint8_t i = 0; i < 6; i ++)
    pinMode(BUTTONS[i], INPUT_PULLDOWN);
  
  Serial.begin(115200);
  SerialBT.begin("ESP32-Flauta");
}

// LOOP
void loop() {
  byte controlSignal = 0b0;
  byte shiftLeft = 0b1;

  for (uint8_t i = 0; i < BUTTONS_SIZE; i++)
    if (digitalRead(BUTTONS[i]))
      controlSignal |= ( 0b1 << i);

  SerialBT.write(controlSignal);
  delay(10);
}