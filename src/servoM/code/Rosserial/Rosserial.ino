/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */
#include "AX12A.h"
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <std_msgs/String.h>
#include <sensor_msgs/JointState.h>
#include <ros/time.h>
#include <tf/transform_broadcaster.h>
#include <tf/tf.h>


#define DirectionPin  (10)
#define BaudRate      (117600)
#define Basic_speed   (30)


ros::NodeHandle nh; //node 

AX12A ax12a2;

float test = 0;
float pos = 2048;
char result[50];
double theta = 0;



void JointsCallback(const sensor_msgs::JointState& cmd_msg){
  ax12a.moveSpeed(0, pos, Basic_speed); //go to zero
    pos = ceil(radToDyn(cmd_msg.position[0]));    
}


//ros::Subscriber<sensor_msgs::JointState> jointsCallback("joint_states", &JointsCallback );//subscribe

sensor_msgs::JointState msg;

ros::Publisher pub("joint_states", &msg);

char *name[] = {"Rotate", "Rotation2"};
float pos1[] = {1.57, 1.57};

void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  //nh.subscribe(jointsCallback);
      nh.advertise(pub);




  Serial3.begin(117600);
  ax12a.begin(BaudRate, DirectionPin, &Serial3);
}

void loop()
{

      //dtostrf(pos,6, 2, result); 
      //nh.loginfo(result); //echo to uart
    



    msg.header.stamp = nh.now();
    msg.name = name;
    pos1[0] = dynToRad(ax12a.readPosition(0));
    msg.position = pos1;
    
    msg.name_length = 1;
    msg.position_length = 1;
    pub.publish(&msg);
    nh.spinOnce();
    delay(100);
  
}

inline float radToDyn(float position_radians) //convert radians to degree
{
  return 4095 * ((180 + position_radians * 57.2958) / 360);
}

inline float dynToRad(float position_dynamixel) //convert radians to degree
{
  return ((((360 * position_dynamixel) / 4095) - 180) * 3.14 / 180);
}
