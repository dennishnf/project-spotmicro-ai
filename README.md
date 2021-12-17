[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/dennishnf/project-microspot-ai/issues)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Download%20and%20use%20the%20Project%20XR%20Glasses&url=https://github.com/dennishnf/project-microspot-ai&hashtags=robotics,spotmicroai,spotmicro,raspberry)     

# Project-SpotMicro-AI

Controlling the MicriSpotAI robot from scratch


## Colaborators

- Alexander    
- Dennis 


## Components from MicroSpot

The MicriSpotAI has the following components:

<p align="center">
<img src="_images/components-microspot-ai.png" alt="Flowchart" width="450"/>
</p>


## Conection to Raspbperry Pi

To connect to the MicroSpot robot you must use their own hotspot network, but this type of configuration produces that the Raspberry Pi and the laptop does not have internet connection, which is a problem. For this reason we looked for another type of access from a laptop to the Raspberry Pi. So, there are several configurations for the SSH connection, it can be through a LAN cable, or through the local internet network.

Between these two types of SSH connections, the connection via the local WiFi network was chosen because it would be easier to manipulate the robot wireless and remotely.

<p align="center">
<img src="_images/ssh-conexion-rpi.png" alt="Flowchart" width="450"/>
</p>



## Calibration of Servo Motors

### Calibration of 1 servomotor via GPIO ports


### Calibration of 1 servomotor via PCA9885 module


### Calibration of 4 servomotor via PCA9885 module



## Resources and references

- https://github.com/mike4192/spotMicro

- https://gitlab.com/public-open-source/spotmicroai/electronics

- http://www.python-exemplary.com/drucken.php?inhalt_mitte=raspi/en/servomotors.inc.php

- https://github.com/FlorianWilk/SpotMicroAI

- https://www.instructables.com/Nova-Spot-Micro-a-Spot-Mini-Clone/

- https://www.hackster.io/news/the-spot-micro-is-a-much-smaller-cheaper-and-diy-version-of-its-namesake-d93c1d36fe91

- http://wiki.ros.org/kinetic

- [ROS Website](https://www.ros.org/)




<!---

git pull
git add -A
git commit -m "v0"
git push -u origin main

--->

