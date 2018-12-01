# GEORGIA TECH ECHO DOT INTEGRATION PROJECT FOR HVAC AND LIGHTING
## Overview
This project is designed to provide HVAC and lighting control to Georgia Tech's Towers residence hall through Amazon's AI assistant, Alexa. Upgrading the building controls mitigates injuries from treading up and down the high-lofted beds and provides the ability to control the thermostat and lights through voice commands. The system architecture scheme is meant to push a user's commands to the Echo Dot, then to our web server, and finally to Metasys--Johnson Controls Inc.'s software for controlling the HVAC and lighting. The command response is meant to flow in the opposite direction to inform the user of the success of the command.

The Echo Dot is responsible for voice recognition and mapping the recognized speech to the sample utterances we listed. The utterances are then mapped to the intents by the Alexa skill--"Housing Jacket". The intent is then packaged together with other information--including the UID--and and sent to the endpoint specified by the skill. Serveo, a SSH server for remote port forwarding, to act as a secure tunnel between local servers and the Internet. It's needed for communication between Flask-Ask--a web server package for Python that maps received intents to Python functions--and the Echo Dot because it can't access local servers.

Flask-Ask will allow for the extraction of other data that is sent to the web server, such as variables and the UID. The UID is unique for each Echo Dot for a given skill and thus can be used to find the corresponding number of that Echo Dot. This is accomplished by having a map on the web server that takes the UID as its input and outputs the room number. 

We created a GUI-Bot to manually change the fan and light states in the Metasys server. The acquisition of the Metasys Secure System Access disk allows for a user to create an authentication token to access Metasys. Metasys will send the intent from the web server to the GUI-Bot which will then modify the light and fan values in the launcher.    

The Metasys server will send a response to the web server which can be used to determine the success or failure of a command. The web server will then send a text message response detailing the result of the actions taken previously. This may entail the changed state of a room or failure of a command to go through. The Echo Dot will process the text response and synthesize speech, thus allowing the user to hear the the result of their command.    

## Release Notes
- [x] Coded the back-end for the Alexa Skill.
- [x] Intent schema with utterances (utterance list can be expanded later).
- [x] Set up web server to communicate between AWS and Metasys.
- [x] Received authentication for a private testing server.
- [x] Created GUI-Bot to manually change state of the lights and fan in the Metasys server.
- [x] Accessed the Metasys Secure System Access disk and installed.
- [ ] With the Metasys Secure System Access disk, allow for the creation of an authentication token for Metasys access. 
- [ ] Expand utterance list.

### Inspection Log For Code
Issues that are/or may cause [bugs](https://drive.google.com/drive/u/1/folders/1jhQzavJDpOM2O_NDJYMQMQMg24d2AFL-). 

## Install Guide
### Prerequisites
#### Installing the Alexa Skill
1. Set Up Echo Dot
* In the Alexa app, sign in with your Amazon account. Press the collapsed menu button in the upper left hand corner and select "Settings". From there, select "Device Settings" and then the '+' icon in the upper right. Select "Add Device" and follow the steps
2. Enabling the Skill
* In the Alexa app, press the collapsed menu button in the upper left hand corner and select "Skills & Games". Search for "Housing Jacket". Select "Enable". (At the current time, this skill hasn't been certified so it will not show up in the search. Upon certification, follow Step 2.)
#### Troubleshooting
If you come across any problems, visit the [Amazon Help Desk](https://www.amazon.com/gp/help/customer/display.html) for troubleshooting tips.
#### Installing Python
Download and install Python (if you don't already have it):
* https://www.python.org/downloads/
* IMPORTANT NOTE: You may have to downgrade the cryptography depending on the system. 

### Dependencies
Download and install the following dependencies:
* https://pypi.org/project/Flask-Ask/
* https://ngrok.com/download
* Serveo (will provide because it requires a lot of setup).

### Download
Click on link to download the code:
* https://github.com/melaniehall12/JIC_8124_GT_Echo_Dot_Project.git

### Running the Application
In the terminal, move to the path of the downloaded project file and type
```commandline
python Housing_app.py
```
Run Serveo/ngrok
```commandline
ngrok http 5000
```
Change the endpoint to the web address that is given once Serveo/ngrok is running.

## Using "Housing Jacket" Skill
To access the "Housing Jacket" skill, say "Alexa, Housing Jacket". Alexa will then welcome the user. Below is a list of utterances that can be used with this skill. This is not an exhaustive list.
Note: Alexa will stay in the skill until you say, "Alexa, stop." 
* Changing the Lights:
  * "Turn on lights."
  * "Switch off the lights."
  * "Close the lights."
* Adjusting the Temperature
  * "Turn heat up by {number} degrees."
  * "Turn heat down by {number}."
* Adjusting the Fan
  * "Fan on."
  * "Turn down fan."
  * "Turn up the fan."
* Setting Temperature Change 
This allows a user to set an arbitrary number for Alexa to either decrease or increase the temperature by without having to specify each time. You can say, "Heat up" and Alexa will increase the temperature by your set number.
  * "Set temperature change to {number} degrees."
* Undo Commands
  * "Undo."
  * "Undo command."
  * "Undo previous."
  
## Authors
* Melanie Hall
* Daniel Mullen
* Simola Nayak
* Steve Nkuranga
* Sonia Thakur

## Client
* Senior Sustainability Project Manager: Malte Weiland
* Email: malte.weiland@aux.gatech.edu

