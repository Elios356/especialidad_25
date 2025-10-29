#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN 5
#define SS_PIN 53

MFRC522 mfrc522(SS_PIN, RST_PIN); 

byte LecturaUID[4];
byte Usuario1[4] = {0x90, 0x0E, 0xE4, 0xA4};
byte Usuario2[4] = {0x06, 0x76, 0x25, 0xD9};

void setup() {
  Serial.begin(9600);
  SPI.begin();
  mfrc522.PCD_Init();
  Serial.println("Listo"); // Esto debe aparecer al iniciar
}

void loop() {
  if (mfrc522.PICC_IsNewCardPresent())
     // Sale del loop si NO detecta la tarjeta
  // Si no ves nada en el monitor, el error está ANTES de aquí (en las conexiones).
  
  if (mfrc522.PICC_ReadCardSerial())
    {
  Serial.print("UID:"); 
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println();
  mfrc522.PICC_HaltA();
   }
  }