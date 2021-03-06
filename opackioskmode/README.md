# OPAC Kiosk with Raspberry Pi
This tutorial will teach you how to set your library catalog website as the homepage of your browser on Raspberry Pi, as well as set up a kiosk browser.

## Equipment
* Raspberry Pi
* Raspberry Pi power supply
* Micro SD card
* Monitor
* Keyboard
* Mouse
* Ethernet cable
* HDMI cable


## Start up the Pi
Connect the Raspberry Pi power supply, HDMI cable, Ethernet cable, keyboard, and mouse.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/3142d05c5be1dae820009f9de47c56c26c14c6ac/opackioskmode/images/Picture1.png" width = 600>


## Open the Web Browser
Click the second icon on the top bar to open the web browser.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/8e71e3e2654c6f4884814f1f71bf8b95884c239f/opackioskmode/images/web_browser_chromium.png" width = 600>


Once Chromium is open, click the three dots on the right of the browser and click “Settings.”

<img src = "https://github.com/prattpi/piprojects4libraries/blob/e30ff2a161c58832691ac42211f9026af88f2f0b/opackioskmode/images/chromium_setting.png" width = 600>

Click on “Appearance” in the left sidebar and toggle “Show home button.” Afterwards, add your URL of choice in the space provided.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/5bd9ab3eef9d5f7099e3b21e6dc42f0895985a98/opackioskmode/images/appearance.png" width = 800>

Next, click on “On Startup” on the left sidebar and click “Open a specific page or set of pages,” and choose “Add a new page,” and add your URL.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/ab5c294ddf2218ea84f41d38ae4403a77d4c95d0/opackioskmode/images/appearance2.png" width = 800>

Now, your URL of choice will be displayed when the browser is first opened, and can also be accessed easily by clicking the Home icon next to the Refresh icon.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/ab5c294ddf2218ea84f41d38ae4403a77d4c95d0/opackioskmode/images/2022-02-06-114501_1920x1080_scrot.png" width = 800>

## Setting up Kiosk Mode
Kiosk mode refers to having your website locked onto the screen, in that the user will not be able to access anything but your website of choice.

First, install updates using the following command:

`sudo apt-get update && sudo apt-get upgrade -y`

Next, we will make sure that the Chromium browser is the latest version. Type the following command, and enter yes when prompted:

`sudo apt-get install chromium x11-xserver-utils`

Next, edit the lightdm.conf file by typing the following command:

`sudo nano /etc/lightdm/lightdm.conf`

In the lightdm.conf file, use the arrow keys to go to `[Seat:*]`. You should find #xserver-command=X six lines below it. Change this line to:

`xserver-command=X -s 0 -dpms`

Refer to the image below.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/8193d372facfc23353ea037a2be4155b49d78af8/opackioskmode/images/screenshot_terminal.png" width = 800>

Press Ctrl+X, press y, and press enter to save the file.

Next, type the following command:

`sudo apt-get install unclutter`

After, type the following command:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

Add the following lines to the file:

    @xset s off 
    @xset -dpms 
    @xset s noblank 
    @chromium-browser --kiosk --incognito -disable-translate --app=YOUR URL HERE
    @unclutter -idle 0

Refer to the image below.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/0cf942e1b5a56412d306427c5323415a0248f255/opackioskmode/images/screenshot_terminal2.png" width = 800>

Press Ctrl+X, press y, and press enter to save the file.

Type `sudo reboot` to restart your Pi. After a few moments, the monitor should display the URL you inputted.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/0cf942e1b5a56412d306427c5323415a0248f255/opackioskmode/images/IMG_6569.JPG" width = 800>

## Returning to the Raspberry Pi Interface
Follow the steps below to access the Raspberry Pi interface by exiting kiosk mode.

Press Ctrl+Alt+F1 to access the Terminal. From there, type the following command:

`sudo killall /usr/lib/chromium-browser/chromium-browser-v7`

Afterwards, press Ctrl+Alt+F7 to access the Raspberry Pi interface.




## Stopping Kiosk Mode on Boot

If you would like to stop booting up in kiosk mode, access the Terminal and type the following:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

This will take you back to the autostart file. 

From there, comment out the five lines that were added by adding a pound sign (#) in front of each line. 

Refer to the image below.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/e891054d4c85ad2a75d82534549f6ffd25f1519c/opackioskmode/images/screenshot_terminal3.png" width = 800>

Press Ctrl+X, press y, and press enter to save the file.

Afterwards, type `sudo reboot` to reboot the Pi. The regular Raspberry Pi interface should now appear after the Pi has booted up.

