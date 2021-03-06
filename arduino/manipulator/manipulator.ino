
// Arduino IDE v 1.8.7

#include "AX12A.h"

#define DirectionPin  (10)
#define BaudRate      (117600)
//#define Broadcast     (254u)
#define Basic_speed (30)

AX12A ax12a2;

bool f = 1;

void setup() {
    Serial.begin(9600);
    Serial3.begin(117600);
    ax12a.begin(BaudRate, DirectionPin, &Serial3);
}
void poweron(){
  
    for (int i = 1;i <= 4; i++) {
      ax12a.moveSpeed(i, 2048, Basic_speed);
       delay(50);
       
  }
}

void loop() {

  for (int i = 0; i <= 3; i++){
    Serial.println(ax12a.readPosition(i));
    delay(50);
  }
Serial.println("------------");


}

  
 
  
