
"use strict";

let StartMotion = require('./StartMotion.js')
let SetDrivePower = require('./SetDrivePower.js')
let GetRobotInfo = require('./GetRobotInfo.js')
let CmdJointTrajectory = require('./CmdJointTrajectory.js')
let StopMotion = require('./StopMotion.js')
let SetRemoteLoggerLevel = require('./SetRemoteLoggerLevel.js')

module.exports = {
  StartMotion: StartMotion,
  SetDrivePower: SetDrivePower,
  GetRobotInfo: GetRobotInfo,
  CmdJointTrajectory: CmdJointTrajectory,
  StopMotion: StopMotion,
  SetRemoteLoggerLevel: SetRemoteLoggerLevel,
};
