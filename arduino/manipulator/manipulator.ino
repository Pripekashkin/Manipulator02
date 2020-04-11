
// Arduino IDE v 1.8.7

#include "AX12A.h"

#define DirectionPin  (10)
#define BaudRate      (57600)
//#define Broadcast     (254u)
#define Basic_speed (30)

AX12A ax12a2;

bool f = 1;

void setup() {
    Serial.begin(9600);
    Serial3.begin(57600);
    ax12a.begin(BaudRate, DirectionPin, &Serial3);
    ax12a.setEndless(0, OFF);
    ax12a.setEndless(1, OFF);
    ax12a.setEndless(2, OFF);
    ax12a.setEndless(3, OFF);
    ax12a.setEndless(4, OFF);
    ax12a.setEndless(5, OFF);

}
void poweron(){
  
    for (int i = 1;i <= 4; i++) {
      ax12a.moveSpeed(i, 2048, Basic_speed);
       delay(50);
       
  }
}

void loop() {
  
ax12a.moveSpeed(4, 2048, Basic_speed);


}

  
 
  
