# OPAC Kiosk with Raspberry Pi
This tutorial will teach you how to set your library catalog website as the homepage of your browser on Raspberry Pi, as well as set up a kiosk browser.

## Equipment
* Raspberry Pi
* Raspberry Pi Power Supply
* Raspberry Pi Imager
* Secondary Computer
* SD Card
* SD Card Reader
* HDMI Cable
* Ethernet Cable
* Monitor
* Mouse
* Keyboard

<img src = "https://github.com/prattpi/piprojects4libraries/blob/50418bf8bfc01dc47a2808be14ea578a017f65c3/opackioskmode/images/raspberry%20pi%20equipment%20with%20labels.jpg" width = 800>

## Imaging the Pi
Insert your SD card into the SD Card reader. Plug the SD Card reader into your secondary computer. Using your secondary computer open <a href="https://www.raspberrypi.com/software/">the Raspberry Pi Imager</a> and install the ‘recommended version’. In this case, we are using the <b>Raspberry Pi OS 64-bit version.</b>  

Choose the storage, in this case, it should be the SD card you use. Click on ‘Write’ and wait for your SD card to be reimaged with Raspberry Pi OS.

<b>Note:</b> For this project, it is recommended to work with Firefox Browser, although Chromium is preinstalled, it is rather slow when run in Kiosk mode. 

<img src = "https://github.com/prattpi/piprojects4libraries/blob/2503b04189228741ab78f64ccffd31588f23f129/opackioskmode/images/Pi%20Imager1.jpg" width = 400> <img src = "https://github.com/prattpi/piprojects4libraries/blob/2503b04189228741ab78f64ccffd31588f23f129/opackioskmode/images/Pi%20Imager%202.jpg" width = 400>

## Setting up your Raspberry Pi
Once you are done imaging your SD card with the Raspberry Pi OS, it is time to start up the Pi. Connect the Raspberry Pi Power Supply to the Pi, and insert the SD card into it. Connect the Pi with the Monitor using the HDMI cable. Connect the mouse and keyboard to the Pi. Plug in the Ethernet cable to a working port and connect it to the Pi to access the internet.

Check for a blinking red light on your Pi to ensure it is being supplied with power. To check for a working internet connection, look for a yellow blinking light inside the port for the ethernet cable.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/835685013bb162709ab867d1b34fb55faaea0c22/opackioskmode/images/Raspberry%20Pi%20ON.jpg" width = 300> <img src = "https://github.com/prattpi/piprojects4libraries/blob/835685013bb162709ab867d1b34fb55faaea0c22/opackioskmode/images/SD%20card%20in%20Pi.jpg" width = 300>

<img src = "https://github.com/prattpi/piprojects4libraries/blob/835685013bb162709ab867d1b34fb55faaea0c22/opackioskmode/images/Yellow%20Light%20for%20internet.jpg" width = 600>

## Starting up the browser

Once you have successfully booted your Raspberry Pi, you will be given the option to choose your browser of choice. Raspberry Pi comes with two in-built options - Chromium and Firefox. <b>Choose Firefox as your choice of the default browser.</b>  

Go to the Settings menu in Firefox as displayed here.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/a30cb746f76ae0c766136cf7612751b5e1be0de2/opackioskmode/images/customurlset1.png" width = 600>

Click on 'Manage more settings'.

Navigate to the ‘Home’ option

<img src = "https://github.com/prattpi/piprojects4libraries/blob/5e5aa9c6d2f10e40d9bc7ee754d593935d269217/opackioskmode/images/customurlset2.png" width = 600>

Choose ‘Custom URL’ here and add the address of your desired webpage.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/5e5aa9c6d2f10e40d9bc7ee754d593935d269217/opackioskmode/images/customurlset3.png" width = 600>

## Set up Kiosk Mode in Firefox

Kiosk mode refers to having your website locked onto the screen, in that the user will not be able to access anything but your website of choice.

For the following steps, you will be using the Terminal to type in (or copy in) text commands.
Press Ctrl+Alt+F1 to access the Terminal or the Terminal icon on the navigation bar at the top. From there, type the following command to install updates:

`sudo apt-get update && sudo apt-get upgrade -y`

## Using Firefox ESR - When to install Firefox ESR?

Firefox ESR is available for lower versions of Raspberry Pi OS. These versions are not compatible with the Firefox browser that comes with the newer 64-bit version. If you are using the Legacy version of Raspberry Pi, it is recommended to install Firefox ESR. 

Simply input this command into the terminal:

`sudo apt-get install firefox-esr`

Next, edit the lightdm.conf file by typing the following command:

`sudo nano /etc/lightdm/lightdm.conf`

In the lightdm.conf file, use the arrow keys to go to [Seat:*]. You should find #xserver-command=X six lines below it. Change this line to:

`xserver-command=X -s 0 -dpms`

Refer to the image below.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/8193d372facfc23353ea037a2be4155b49d78af8/opackioskmode/images/screenshot_terminal.png" width = 800>

Press Ctrl+X, press y, and press enter to save the file.

Next, type the following command:

<b>Please note</b> that the following command is used to hide the mouse pointer on the screen. In case, you do not want your mouse pointer to blink upon movement, feel free to skip this command. 

`sudo apt-get install unclutter`

After, type the following command:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

Add the following lines to the file:

    @xset s off 
    @xset -dpms 
    @xset s noblank 
    @firefox-browser --kiosk --incognito -disable-translate --app=YOUR URL HERE
    @unclutter -idle 0

<b> For Firefox ESR users, copy and paste this code instead: </b>

    @xset s off 
    @xset -dpms 
    @xset s noblank 
    @firefox-esr --kiosk --incognito -disable-translate --app=YOUR URL HERE
    @unclutter -idle 0

<b> Again, note that the last line `@unclutter -idle 0` is optional and upto you</b>

Press Ctrl+X, press y, and press enter to save the file.

Type `sudo reboot` to restart your Pi. After a few moments, the monitor should display the URL you inputted.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/a1799bd12b80ec146764168a3b831837611b0cd6/opackioskmode/images/Firefox%20Pratt%20Library%20Setup.jpg" width = 800>

## Returning to the Raspberry Pi Interface
Follow the steps below to access the Raspberry Pi interface by exiting kiosk mode.

Press Ctrl+Alt+F1 to access the Terminal. From there, type the following command:

`sudo killall /usr/lib/firefox-browser-v7`

Afterwards, press Ctrl+Alt+F7 to access the Raspberry Pi interface.




## Stopping Kiosk Mode on Boot

If you would like to stop booting up in kiosk mode, access the Terminal and type the following:

`sudo nano /etc/xdg/lxsession/LXDE-pi/autostart`

This will take you back to the autostart file. 

From there, comment out the five lines that were added by adding a pound sign (#) in front of each line that you added. 

    #@xset s off 
    #@xset -dpms 
    #@xset s noblank 
    #@firefox-browser --kiosk --incognito -disable-translate --app=YOUR URL HERE
    #@unclutter -idle 0

<b> For Firefox ESR users, this is how it should look: </b>

    #@xset s off 
    #@xset -dpms 
    #@xset s noblank 
    #@firefox-esr --kiosk --incognito -disable-translate --app=YOUR URL HERE
    #@unclutter -idle 0

Press Ctrl+X, press y, and press enter to save the file.

Afterwards, type `sudo reboot` to reboot the Pi. The regular Raspberry Pi interface should now appear after the Pi has booted up.

