# Lesson 1: Intro to mobile Automation
Examples of mobile aut tools are: Appium, Calabash, Robotium, UI Automator, Ranorex studio, TestComplete mobile, 

# Lesson 2: Appium 
Appium is an open source tool used for automating native, mobile web & hybrid apps on iOS mobile, Android mobile 
& Windows desktop platforms.
Native apps: Apps built using iOS and Android SDKs. They are 'Platform dependent' eg calculator, calendar, etc
Mobile web apps: Web apps that are accessible using mobile browser
Appium supports native iOS and android apps. 
It supports multiple programming languages and cross-platform scripting

# Lesson 3: Setup for android automation
Prerequisites: Java 8, Android SDK, Android Emulator
Android studio is the official IDE for Android OS. It is available for download on windows, mac and linux OS.
Setup for Java 8 installation:
1. visit https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html and follow the installation instructions
2. type 'java' in terminal to verify installation

Setup Android SDK:
1. visit https://developer.android.com/studio and follwoing the installation prompt
2. on Android studio UI, select More Actions
3. Open the Android SDK manager
4. Select the SDKs, accept license and continue download

Setup Emulator
1. In Android studio UI click the 'More Actions' dropdown
2. click virtual device manager 
3. choose your device definition
4. select a system image (download if applicable)
5. click next and verify device configuration
6. click finish to finalize emulator setup
7. start emulator


# Lesson 5: Setup for android tools from terminal
This is a better option of using android tools as it saves a lot of resources (eg RAM) beats against having multiple apps open i.e android studio & emulator
1. Open your environment variable (search with environment variables on window) ()
2. Verify ANDROID_HOME is added to system variable. If not, add it
3. Add the Android emulator to the system path
4. Add the android platform tool to the system path

To run the emulator from terminal:
1. use the command <emulator -list-avds> to get the list of AVDs you have created on android studio
2. Then use the command <emulator -avd name-of-the-AVD> eg emulator -avd Pixel_4_API_31

# Lesson 6: Setup Appium for Python
Use the command to install appium python client <pip install Appium-Python-Client>
Then we can import the following packages:

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC