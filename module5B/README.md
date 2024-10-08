# Lesson 1: Intro to mobile Automation
Examples of mobile aut tools are: Appium, Calabash, Robotium, UI Automator, Ranorex studio, TestComplete mobile, 

# Lesson 2: Appium 
Appium is an open source tool used for automating native, mobile web & hybrid apps on iOS mobile, Android mobile 
& Windows desktop platforms.
Native apps: Apps built using iOS and Android SDKs. They are 'Platform dependent' eg calculator, calendar, etc
Native apps are apps built with native platform technologies(Android - Kotlin/Java | IOS - Swift)
They are downloaded from the stores. eg KIppaPay

Mobile web apps: Web apps that are accessible using mobile browser.
Web Apps are apps that run on the web entirely. You can call them website but it doesn't describe their sophistication. 
Landing page can be called a website better. Eg. CS dashboard.

Hybrid Apps. -> Apps built with hybrid/cross-platform technologies. Apps built with non-native technologies -> they are write once run everywhere kind of tech. 
Initially was mainly web tech bundled in Native containers(IONIC, etc)
Flutter is also an example but flutter is more efficient and don't just do conversions  to native like reactNative.
Kippa is hybrid. Same code runs on android and IOS.
Kippa Unified is hybrid too -> android, IOS, web can even run on desktop(macOS, windows, linux)

Appium supports native iOS and android apps. 
It supports multiple programming languages and cross-platform scripting

# Lesson 3: Setup for android automation
Prerequisites: Java 8, Android SDK, Android Emulator
Android studio is the official IDE for Android OS. It is available for download on windows, mac and linux OS.
We are not using android studio for development, instead we will use it to manage our SDK and emulator
Setup for Java 8 installation:
1. visit https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html and follow the installation instructions
2. type 'java' in terminal to verify installation

Setup Android SDK:
1. visit https://developer.android.com/studio and following the installation prompt
2. on Android studio UI, select More Actions
3. Open the Android SDK manager
4. Select the SDKs, accept license and continue download

# Lesson 4: Setup Emulator
1. In Android studio UI click the 'More Actions' dropdown
2. click virtual device manager 
3. choose your device definition
4. select a system image (download if applicable)
5. click next and verify device configuration
6. click finish to finalize emulator setup
7. start emulator


# Lesson 5: Setup for android tools from terminal
This is a better option of using android tools as it saves a lot of resources (eg RAM) and 
beats against having multiple apps open i.e android studio & emulator
1. Open your environment variable (search with environment variables on window) ()
--------------------------------------------------------------------

For mac users following these steps to add to environment variables:
Sure, to add an environment variable in macOS, you can follow these steps:
1. **Open Terminal:** You can find Terminal in the "Applications" folder under "Utilities," or you can use Spotlight (Command + Space, then type "Terminal") to open it.

2. **Identify the Shell:** Determine which shell you're using. By default, macOS uses the Bash shell. To check, you can type `echo $SHELL` in the Terminal and press Enter.

3. **Choose a Shell Configuration File:** Depending on the shell, you'll need to edit the respective shell configuration file. Commonly used configuration files are `.bash_profile` for Bash or `.zshrc` for Zsh if you're using macOS Catalina or later, which uses the Zsh shell by default. If these files don't exist, you might need to create them.

4. **Open the Configuration File:** Use a text editor to open the configuration file. You can do this using the Terminal. For example, if you're using Bash, you can type `nano ~/.bash_profile` and press Enter. If you're using Zsh, it might be `nano ~/.zshrc`. If the file doesn’t exist, it will create a new one.

5. **Add the Environment Variable:** In the opened file, you can add your environment variable in the format `export VARIABLE_NAME="variable_value"`. For instance, if you want to add a variable named `MY_VARIABLE` with a value of `example`, you'd add `export MY_VARIABLE="example"`.

6. **Save and Close the File:** After adding the environment variable, save the changes in the file. In Nano, you can press `Ctrl + X` to exit, it will prompt you to save the changes, press `Y` for Yes, and then press Enter.

7. **Apply the Changes:** To make the changes effective without restarting your system, you can run the command `source ~/.bash_profile` or `source ~/.zshrc` based on the file you've edited.

8. **Verify:** To verify that the environment variable has been added successfully, you can use the `echo` command followed by the variable name. For instance, `echo $MY_VARIABLE`.

After following these steps, the environment variable should be set and accessible within your terminal session on your macOS.
------------------------------------------------------------------------------------
2. Verify ANDROID_HOME is added to system variable. If not, add it
3. Add the Android emulator to the system path
4. Add the android platform tool to the system path

To run the emulator from terminal (computer terminal or other IDE terminals eg VS code, pycharm etc):
1. use the command <emulator -list-avds> to get the list of AVDs you have created on android studio
2. Then use the command <emulator -avd name-of-the-AVD> eg emulator -avd Pixel_4_API_31

# Lesson 6: Setup Appium for Python
1. Create a folder and give it a name that is not the keyword 'appium'. i called my appium_mobile
2. Open a terminal and type the below command to install appium-python client
Use the command to install appium python client <pip install Appium-Python-Client>
3. You can go ahead to confirm its installation by clicking on the 'Python Packages' at the bottom left
of this pycharm IDE (next to git) and search for appium-python-client 
4. Create a python file (eg hello.py)
Then we can import the following packages by writing them in the hello.py file:

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

5. Write a simple test eg print("Hello World")
6. Next ensure you configure Java home if its not already set as an environment variable


# Lesson 7: Run your first mobile automation using an existing app
Desire capabilities are key-value pairs encoded in json object that is sent by appium client to the server during a new automation session

{
    "platformName": "App"
    "platformVersion": "12"
    "deviceName": "Android Emulator"
    "appPackage": "com.package.app"
    "app": "/path/to/my.app"
}
    

Step 1: Start your emulator which can be done from terminal using the command 
<emulator -avd name-of-the-AVD> eg emulator -avd Pixel_4_API_31
Ensure you have saved the paths to emulator, build tools, platform tools, tools in your system environment as we did for java home
My environment looks like this https://monosnap.com/file/JsDnkOgHrYYaoHfd2crcWWXBejcG06
Step 2: create a your python file for the automation e.g googlesearch_automation.py
Step 3: Add the libraries to be imported to the python file i.e 
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Step 4: start writing your code either directly into the py file or within a function
Step 5: declare the desired capabilities in the main function
To get the device name, on your emulator go to Settings > Search for 'About Emulated device' > you will see device name https://prnt.sc/_Cm3EwShCf3I
Step 6: Start your appium server (appium GUI) and ensure its the port on the appium server that is set as 
command executor path

Note: desired capabilities for running an app for the first time on an emulator is slightly different from that
that of running an app already installed on the emulator.
* For New app, eg installing YTmusic for the first time. The DC is:

import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    desired_caps = {
        "deviceName": "Android Emulator",
        "platformName": "Android",
        "platformVersion": "12",
        "app": "<path of the downloaded app>",
        "appPackage": "<can be gotten from apkpure site where app was downloaded from>",
        "noSign": True
    }
    driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_caps)
    time.sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()

* For Existing app, the 'app' parameter is absent and App activity is present
Step 7: Run the python file. The appium server is installed on the emulator and then the app runs
* https://monosnap.com/file/VEyTwlkBY9QvIe6FgqbT7ONubJvAjh

# Lesson 8: Running your first application on System or Server
The above steps show how to run apps from the system. To run from server the following changes is done:
1. Download the calculator app from https://apkpure.com/calculator/com.google.android.calculator/downloading
2. A server is created at the folder location where the downloaded app is by opening a 
terminal in that folder location and using the command <python -m http.server <port of choice>>
eg python -m http.server 9009 https://monosnap.com/file/OU8G2xZzhaRxJ9PrmjkO4CpNvrLoUt
Note: You can confirm the server has started by typing http://127.0.0.1:9009/ in a browser and this will display the contents of the directory. Look for the calculator in the directory and copy the path which you should paste as the app value https://prnt.sc/GjoiSy5eAXBf
N.B: 127.0.0.1 is the same as local host
3. Ensure appium server is runner
4. Uninstall the app if its installed so as to allow you reinstall it using the server option.
5. You can confirm the server is correct by typing it directly in a browser https://monosnap.com/file/bC42YNTJcmWZUhlbZAuf6V0XkeKhad

# Lesson 9: Getting android app variables
ADB = Android debug bridge is a programming tool used to debug android-based devices. 
It allows for communication with the android device over TCP or USB connection
ADB shell = virtual CLI present on the android device through ADB connection
Note: To use ADB, you must be connected to an android device

To get the list of installed apps and their package name on the android device; 
enter the shell and execute the commands: 
<adb shell>
<pm list packages -f>
Alternatively run <adb shell pm list packages -f>

To get the list of android app activities; enter the shell and run command
<adb shell>
<dumpsys package | grep -i"<package name>" | grep Activity
Alternatively run <adb shell dumpsys package | grep -i"<package name>" | grep Activity>

Android LOGCAT is a utility that dumbs up the android device logs so that errors and other messages can be seen  
Use the command <adb logcat> to view system logs

To get the list of app activities use the command <dumpsys package | grep -i 'com.android.calendar' | grep 'Activity'>