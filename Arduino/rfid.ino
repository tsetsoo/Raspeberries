*
#include  <Wire.h>
#include  <LiquidCrystal_I2C.h>

  // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup()
{
  lcd.init();                      // initialize the lcd 
  lcd.backlight();
  Serial.begin(9600);
}

void loop()
{
  // when characters arrive over the serial port...
  if (Serial.available()) {
    // wait a bit for the entire message to arrive
    delay(100);
    // clear the screen
    lcd.clear();
    // read all the available characters
    while (Serial.available() > 0) {
      // display each character to the LCD
      lcd.write(Serial.read());
    }
  }
}

*/
#include <SPI.h>
#include <MFRC522.h>
#include  <Wire.h>
#include  <LiquidCrystal_I2C.h>


#define RLED 2
#define YLED 4
#define BLED 7
 
#define SS_PIN 10
#define RST_PIN 9
MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

LiquidCrystal_I2C lcd(0x27,20,4);
 
void LedClear()
{
  digitalWrite(RLED,LOW);
  digitalWrite(YLED,LOW);
  digitalWrite(BLED,LOW);
}

void setup() 
{

  digitalWrite(RLED,HIGH); //Power on RLED
  lcd.init();        //Initiate the LCD display      
  lcd.backlight();
  Serial.begin(9600);   // Initiate a serial communication
  SPI.begin();      // Initiate  SPI bus
  mfrc522.PCD_Init();   // Initiate MFRC522
  delay(1000);
  LedClear();
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("Residence");
  lcd.setCursor(0,1);
  lcd.print("Raspeberries");

  Serial.setTimeout(100);
}
void loop() 
{
  

  digitalWrite(YLED,HIGH);
  digitalWrite(BLED,LOW);
  digitalWrite(RLED,LOW);
  lcd.setCursor(0,0);
  lcd.print("Residence");
  lcd.setCursor(0,1);
  lcd.print("Raspeberries");
  
  digitalWrite(YLED,HIGH);
  // Look for new cards
  if ( ! mfrc522.PICC_IsNewCardPresent()) 
  {
    return;
  }
  // Select one of the cards
  if ( ! mfrc522.PICC_ReadCardSerial()) 
  {
    return;
  }
  //Show UID on serial monitor
  //Serial.print("UID tag :");
  String content= "";
  byte letter;
  for (byte i = 0; i < mfrc522.uid.size; i++) 
  {
     //Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
     //Serial.print(mfrc522.uid.uidByte[i], HEX);
     content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
     content.concat(String(mfrc522.uid.uidByte[i], HEX));
  }
  //Serial.println();
  //Serial.print("Message : ");
  content.toUpperCase();
  if (content.substring(1) == "29 F3 BF 55")
  {
    lcd.clear();
    Serial.println("1");
    Serial.flush();
    lcd.setCursor(0,0);
    lcd.print("Key Accepted");
    //Serial.println();
    digitalWrite(BLED,HIGH);
       // while(Serial.available() != "Welcome Simo")//to-do, need to skip all other comms
    //{
    //}
    delay(10000);
    lcd.clear();
    lcd.setCursor(0,0);
    if(Serial.available() > 0 ) {
    switch(int(Serial.read()) - 48)
    {
    case 1: lcd.setCursor(0,0); lcd.print("Welcome Simo");delay(5000); break;
    case 0: lcd.setCursor(0,0); lcd.print("Chezni we bunak");delay(5000); break;  
    }
    }
    

    delay(3000);
    lcd.clear();
//

//    lcd.clear();

    //Rotate servo and move camera

    //Get the label/name of the person who is seen and say hi, welcome home
  }
 
  else   
  {
    lcd.clear();
    lcd.setCursor(0,0);
    lcd.print("Key Rejected");
    Serial.println("0");
    digitalWrite(2,HIGH);
    delay(3000);
    lcd.clear();

  }
}