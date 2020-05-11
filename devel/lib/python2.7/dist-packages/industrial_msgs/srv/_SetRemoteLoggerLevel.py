# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from industrial_msgs/SetRemoteLoggerLevelRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import industrial_msgs.msg

class SetRemoteLoggerLevelRequest(genpy.Message):
  _md5sum = "3a0089a136293a269fa1a44788ce9777"
  _type = "industrial_msgs/SetRemoteLoggerLevelRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """




industrial_msgs/DebugLevel level

================================================================================
MSG: industrial_msgs/DebugLevel
# Debug level message enumeration.  This may replicate some functionality that
# alreay exists in the ROS logger.
# TODO: Get more information on the ROS Logger.
uint8 val

uint8 DEBUG = 5
uint8 INFO = 4
uint8 WARN = 3
uint8 ERROR = 2
uint8 FATAL = 1
uint8 NONE = 0 
"""
  __slots__ = ['level']
  _slot_types = ['industrial_msgs/DebugLevel']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       level

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetRemoteLoggerLevelRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.level is None:
        self.level = industrial_msgs.msg.DebugLevel()
    else:
      self.level = industrial_msgs.msg.DebugLevel()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.level.val))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.level is None:
        self.level = industrial_msgs.msg.DebugLevel()
      end = 0
      start = end
      end += 1
      (self.level.val,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.level.val))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.level is None:
        self.level = industrial_msgs.msg.DebugLevel()
      end = 0
      start = end
      end += 1
      (self.level.val,) = _get_struct_B().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from industrial_msgs/SetRemoteLoggerLevelResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import industrial_msgs.msg

class SetRemoteLoggerLevelResponse(genpy.Message):
  _md5sum = "50b1f38f75f5677e5692f3b3e7e1ea48"
  _type = "industrial_msgs/SetRemoteLoggerLevelResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """industrial_msgs/ServiceReturnCode code


================================================================================
MSG: industrial_msgs/ServiceReturnCode
# Service return codes for simple requests.  All ROS-Industrial service
# replies are required to have a return code indicating success or failure
# Specific return codes for different failure should be negative.
int8 val

int8 SUCCESS = 1
int8 FAILURE = -1

"""
  __slots__ = ['code']
  _slot_types = ['industrial_msgs/ServiceReturnCode']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       code

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetRemoteLoggerLevelResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.code is None:
        self.code = industrial_msgs.msg.ServiceReturnCode()
    else:
      self.code = industrial_msgs.msg.ServiceReturnCode()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_b().pack(self.code.val))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.code is None:
        self.code = industrial_msgs.msg.ServiceReturnCode()
      end = 0
      start = end
      end += 1
      (self.code.val,) = _get_struct_b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_b().pack(self.code.val))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.code is None:
        self.code = industrial_msgs.msg.ServiceReturnCode()
      end = 0
      start = end
      end += 1
      (self.code.val,) = _get_struct_b().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
class SetRemoteLoggerLevel(object):
  _type          = 'industrial_msgs/SetRemoteLoggerLevel'
  _md5sum = '4ae8385cb830c0d46129570c3394af54'
  _request_class  = SetRemoteLoggerLevelRequest
  _response_class = SetRemoteLoggerLevelResponse