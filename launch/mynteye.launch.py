#!/usr/bin/env python3
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    ld = LaunchDescription()
    config_path = os.path.join(get_package_share_directory('mynteye_ros2_wrapper'), 'config', 'params.yaml')  
    base_node = Node(package = 'mynteye_ros2_wrapper',
                     executable = 'mynteye_raw_data',
                     output = 'screen',
                     emulate_tty=True,
                     parameters = [config_path])
    rect_node = Node(package = 'mynteye_ros2_wrapper',
                     executable = 'mynteye_rectification.py',
                     output = 'screen',
                     emulate_tty=True,
                     parameters = [config_path])
    disp_node = Node(package = 'stereo_image_proc',
                     executable = 'disparity_node',
                     output = 'screen',
                     emulate_tty=True,
                     parameters = [config_path])
    view_node = Node(package = 'image_view',
                     executable = 'disparity_view',
                     output = 'screen',
                     emulate_tty=True,
                     remappings=[('/image', '/disparity')])
    ld.add_action(base_node)
    ld.add_action(rect_node)
    ld.add_action(disp_node)
    ld.add_action(view_node)
    return ld
