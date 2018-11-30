# GEORGIA TECH ECHO DOT INTEGRATION PROJECT FOR HVAC AND LIGHTING
## Overview
This project is designed to provide HVAC and lighting control to Georgia Tech's Towers residence hall through Amazon's AI assistant, Alexa. Upgrading the building controls mitigates injuries from treading up and down the high-lofted beds and provides the ability to control the thermostat and lights through voice commands. The system architecture scheme is meant to push a user's commands to the Echo Dot, then to our web server, and finally to Metasys--Johnson Controls Inc.'s software for controlling the HVAC and lighting. The command response is meant to flow in the opposite direction to inform the user of the success of the command.

The Echo Dot is responsible for voice recognition and mapping the recognized speech to the sample utterances we listed. The utterances are then mapped to the intents by the Alexa skill--"Housing Jacket". The intent is then packaged together with other information--including the UID--and and sent to the endpoint specified by the skill. Serveo, a SSH server for remote port forwarding, to act as a secure tunnel between local servers and the Internet. It's needed for communication between Flask-Ask--a web server package for Python that maps received intents to Python functions--and the Echo Dot because it can't access local servers.

Flask-Ask will allow for the extraction of other data that is sent to the web server, such as variables and the UID. The UID is unique for each Echo Dot for a given skill and thus can be used to find the corresponding number of that Echo Dot. This is accomplished by having a map on the web server that takes the UID as its input and outputs the room number. Once the room number and intents are known, the output command for the SOAP client----can be created. This output command is equivalent to a getter/setter for an object in the Metasys database. The SOAP client then does an authentication handshake with Metasys using the Metasys Secure System Access DLL--a dynamically linked list for secure connection with the Metasys server--and sends over the output command.   

The Metays server will send a response to the web server which can be used to determine the success or failure of a command. The web server will then send a text message response detailing the result of the actions taken previously. This may entail the changed state of a room or failure of a command to go through. The Echo Dot will process the text response and sythesize speech, thus allowing the user to hear the the result of their command.    

## Release Notes

### New Features

### Known Bugs

## Install Guide
### Prerequisites
#### Installing the Alexa Skill
1. Set Up Echo Dot
* In the Alexa app, press the collapsed menu button in the upper left hand corner and select "Settings". From there, select "Device Settings" and then the '+' icon in the upper right. Select "Add Device" and follow the steps.  
2. Enabling the Skill
* In the Alexa app, press the collapsed menu button in the upper left hand corner and select "Skills & Games". Search for . Select "Enable".
3. Link GT Account
* 
#### Creating an Amazon Web Developer (AWS) Account
*
#### Installing the Metasys Launcher
Download and install the Launcher:
* https://www.johnsoncontrols.com/buildings/specialty-pages/metasys-launcher
*


See  A authorized username and password is also required to open the launcher. You must also have Python downloaded (may have to downgrade cryptography depending on the system).  

### Dependencies
Download and install the following dependencies:
* https://pypi.org/project/Flask-Ask/
* https://ngrok.com/download
* Serveo (will provide because it requires a lot of setup).

### Download
Click on link to download the code:
* https://github.com/melaniehall12/JIC_8124_GT_Echo_Dot_Project.git

### Installation
Link Echo Dot(s) to account and upload the 'Housing_app' skill. Change endpoint to the web address that is given when Serveo/ngrok is run with argument http 5000.

### Running the Application
Run Housing_app.py through the command line. Then, run Serveo/ngrok with the argument "http 5000".

## Authors
* Melanie Hall
* Daniel Mullen
* Simola Nayak
* Steve Nkuranga
* Sonia Thakur

## Client
* Senior Sustainability Project Manager: Malte Weiland

