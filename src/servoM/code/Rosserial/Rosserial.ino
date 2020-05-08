/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */
#include "AX12A.h"
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <sensor_msgs/JointState.h>

#define DirectionPin  (10)
#define BaudRate      (117600)
#define Basic_speed   (30)

ros::NodeHandle nh;
AX12A ax12a2;

float test = 0;
float pos = 2048;
char result[50];




void JointsCallback(const sensor_msgs::JointState& cmd_msg){
  ax12a.moveSpeed(0, pos, Basic_speed); //go to zero
  pos =+ ceil(RadiansToDegrees(cmd_msg.position[0]));

  
  
}

ros::Subscriber<sensor_msgs::JointState> jointsCallback("joint_states", &JointsCallback );


void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(jointsCallback);
  Serial3.begin(117600);
  ax12a.begin(BaudRate, DirectionPin, &Serial3);
}

void loop()
{

  dtostrf(pos,6, 2, result);
  //sprintf(log_msg,"= "result);
  nh.loginfo(result);
  nh.spinOnce();
  delay(1);



}

inline float RadiansToDegrees(float position_radians)
{
  return position_radians / 0.001533;
}
