/*
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */
#include "AX12A.h"
#include <ros.h>
#include <std_msgs/UInt16.h>
#include <sensor_msgs/JointState.h>
#include <ros/time.h>
#include <tf/transform_broadcaster.h>
#include <tf/tf.h>


#define DirectionPin  (10)
#define BaudRate      (117600)
#define Basic_speed   (30)

ros::NodeHandle nh; //node to listen
ros::NodeHandle nh02; //node to write


geometry_msgs::TransformStamped t;
tf::TransformBroadcaster broadcaster;

char base_link[] = "Servo";
char child_link[] = "Horn";


AX12A ax12a2;

float test = 0;
float pos = 2048;
char result[50];
double theta = 0;



void JointsCallback(const sensor_msgs::JointState& cmd_msg){
  ax12a.moveSpeed(0, pos, Basic_speed); //go to zero
 pos = ceil(radToDyn(cmd_msg.position[0]));
     
}


ros::Subscriber<sensor_msgs::JointState> jointsCallback("joint_states", &JointsCallback );//subscribe



void setup()
{
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(jointsCallback);
  nh02.initNode();  //init write 
  broadcaster.init(nh02);


  Serial3.begin(117600);
  ax12a.begin(BaudRate, DirectionPin, &Serial3);
}

void loop()
{

    //dtostrf(pos,6, 2, result); 
    //nh02.loginfo(result); //echo to uart
    nh.spinOnce();
    delay(100);


    //t.transform.translation.z = dynToRad(ax12a.readPosition(0));
   /* t.transform.translation.z = 0.049;
    t.transform.rotation = tf::createQuaternionFromYaw(dynToRad(ax12a.readPosition(0)));
    t.header.frame_id = base_link;
    t.child_frame_id = child_link;
    t.header.stamp = nh02.now();
    broadcaster.sendTransform(t);*/
    //nh02.spinOnce();
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
