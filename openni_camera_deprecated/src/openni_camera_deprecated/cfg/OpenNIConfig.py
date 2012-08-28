## *********************************************************
## 
## File autogenerated for the openni_camera_deprecated package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

##**********************************************************
## Software License Agreement (BSD License)
##
##  Copyright (c) 2008, Willow Garage, Inc.
##  All rights reserved.
##
##  Redistribution and use in source and binary forms, with or without
##  modification, are permitted provided that the following conditions
##  are met:
##
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above
##     copyright notice, this list of conditions and the following
##     disclaimer in the documentation and/or other materials provided
##     with the distribution.
##   * Neither the name of the Willow Garage nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
##  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
##  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
##  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
##  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
##  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
##  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
##  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
##  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
##  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
##  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
##  POSSIBILITY OF SUCH DAMAGE.
##**********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 259, 'description': 'Image output mode for the color/grayscale image', 'max': 9, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'image_mode', 'edit_method': "{'enum_description': 'output mode', 'enum': [{'srcline': 10, 'description': '1280x1024@15Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_15Hz'}, {'srcline': 11, 'description': '640x480@30Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'VGA_30Hz'}, {'srcline': 12, 'description': '640x480@25Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'VGA_25Hz'}, {'srcline': 13, 'description': '320x240@25Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_25Hz'}, {'srcline': 14, 'description': '320x240@30Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_30Hz'}, {'srcline': 15, 'description': '320x240@60Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 6, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_60Hz'}, {'srcline': 16, 'description': '160x120@25Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 7, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_25Hz'}, {'srcline': 17, 'description': '160x120@30Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_30Hz'}, {'srcline': 18, 'description': '160x120@60Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 9, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_60Hz'}]}", 'default': 2, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 259, 'description': 'Bayer to RGB algorithm', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'debayering', 'edit_method': "{'enum_description': 'Bayer to RGB algorithm selection', 'enum': [{'srcline': 21, 'description': 'Fast debayering algorithm using bilinear interpolation', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Bilinear'}, {'srcline': 22, 'description': 'debayering algorithm using an edge-aware algorithm', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'EdgeAware'}, {'srcline': 23, 'description': 'debayering algorithm using a weighted edge-aware algorithm', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'EdgeAwareWeighted'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'depth output mode', 'max': 9, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'depth_mode', 'edit_method': "{'enum_description': 'output mode', 'enum': [{'srcline': 10, 'description': '1280x1024@15Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': 'SXGA_15Hz'}, {'srcline': 11, 'description': '640x480@30Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': 'VGA_30Hz'}, {'srcline': 12, 'description': '640x480@25Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': 'VGA_25Hz'}, {'srcline': 13, 'description': '320x240@25Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_25Hz'}, {'srcline': 14, 'description': '320x240@30Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 5, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_30Hz'}, {'srcline': 15, 'description': '320x240@60Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 6, 'ctype': 'int', 'type': 'int', 'name': 'QVGA_60Hz'}, {'srcline': 16, 'description': '160x120@25Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 7, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_25Hz'}, {'srcline': 17, 'description': '160x120@30Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 8, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_30Hz'}, {'srcline': 18, 'description': '160x120@60Hz', 'srcfile': '../cfg/OpenNI.cfg', 'cconsttype': 'const int', 'value': 9, 'ctype': 'int', 'type': 'int', 'name': 'QQVGA_60Hz'}]}", 'default': 2, 'level': 0, 'min': 2, 'type': 'int'}, {'srcline': 259, 'description': 'Depth data registration', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'depth_registration', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'depth image time offset in seconds', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'depth_time_offset', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -1.0, 'type': 'double'}, {'srcline': 259, 'description': 'image time offset in seconds', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/fuerte/stacks/dynamic_reconfigure/src/dynamic_reconfigure/parameter_generator.py', 'name': 'image_time_offset', 'edit_method': '', 'default': 0.0, 'level': 0, 'min': -1.0, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

OpenNI_SXGA_15Hz = 1
OpenNI_VGA_30Hz = 2
OpenNI_VGA_25Hz = 3
OpenNI_QVGA_25Hz = 4
OpenNI_QVGA_30Hz = 5
OpenNI_QVGA_60Hz = 6
OpenNI_QQVGA_25Hz = 7
OpenNI_QQVGA_30Hz = 8
OpenNI_QQVGA_60Hz = 9
OpenNI_Bilinear = 0
OpenNI_EdgeAware = 1
OpenNI_EdgeAwareWeighted = 2
