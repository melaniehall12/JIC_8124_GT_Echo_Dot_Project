# Georgia Tech Echo Dot Integration Project for HVAC and Lighting
Junior Design project for CS 3312/LMC 3431 for the client, Malte Weiland. This project focuses on the integration of Amazon's Echo Dot into Georgia Tech dorm rooms.

Team: Melanie Hall, Daniel Mullen, Simola Nayak, Steve Nkuranga, and Sonia Thakur.

### Release Notes

NEW FEATURES

None.

BUG FIXES

None. 

KNOWN BUGS

Doesn't work.

### Install Guide

PRE-REQUISITES

Need an Echo Dot/Echo Dot sim. You must have the Metasys Launcher program installed. See https://www.johnsoncontrols.com/buildings/specialty-pages/metasys-launcher. A authorized username and password is also required to open the launcher. You must also have Python downloaded (may have to downgrade cryptography depending on the system).  

DEPENDENCIES

Download and install Flask-Ask (https://pypi.org/project/Flask-Ask/).

Download and install ngrok (https://ngrok.com/download).

Download and install Serveo (will provide because it requires a lot of setup).

DOWNLOAD

https://github.com/melaniehall12/JIC_8124_GT_Echo_Dot_Project.git

BUILD

No build is necessary.

INSTALLATION

Create an Amazon Web Developer account. Link Echo Dot(s) to account and upload the 'Housing_app' skill. Change endpoint to the web address that is given when Serveo/ngrok is run with argument http 5000.

RUNNING APPLICATION

Run Housing_app.py through command line. Run Serveo/ngrok with argument http 5000.

