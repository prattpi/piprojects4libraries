# Poem Printer with Raspberry Pi

This tutorial will teach you how to set up a poem printer using Raspberry Pi.

## Equipment:
- Raspberry Pi
- Raspberry Pi power supply
- Micro SD card
- Monitor
- Keyboard
- Mouse
- Ethernet cable
- HDMI cable
- Keyestudio Button Switch
- Adafruit Mini Thermal Receipt Printer
- 3x female-female jumper wires


## Reimage the Raspberry Pi

To start the printer project, the micro SD card for the Raspberry Pi must be reimaged to Buster. Open the [Raspberry Pi imager](https://www.raspberrypi.com/software/) and select “Choose OS” followed by “Raspberry Pi OS (other).”

Scroll down and select Raspberry Pi OS (Legacy), as seen in the screenshot below.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f43706a6d4737772f756e6e616d65642e706e67.png">

Install the Raspberry Pi OS (Legacy) onto your micro SD card.

If you would like to add wifi information, enable SSH, or customize the setup of the Pi within the Raspberry Pi Imager, press Ctrl+Shift+X to bring up a settings page. This video is also helpful should you wish to configure settings: https://www.youtube.com/watch?v=om8gGB3gyT0


## Connect the Printer and Plug in the Button

Connect the printer’s jumper wires to your Raspberry Pi as referenced in the chart below.

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f3659584d4b53332f7261737062657272792d70692d6770696f2d6469616772616d2e706e67.png">

On the bottom of the printer, you should see a sticker that lists wires named “GND,” “RX,” and “TX.” These wires need to be plugged into the three pins on the right column Raspberry Pi after the two 5V pins.

See image below.

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f4e4e74463637352f494d472d363834312e6a7067.jpeg" width="500"/>

Next, we will plug in the Keyestudio Button Switch. To start, plug in three jumper wires to the button.

Start plugging in the jumper wires connected to the button to the Raspberry Pi as indicated in the charts below.

| Button      | Raspberry Pi Pin |
| ----------- | ----------- |
| GND (-)      | Ground (Pin 25)       |
| V+ (power positive pin)   | 3.3v (Pin 17)        |
| S (signal pin)   | GPIO23 (Pin 16)        |

<img src="https://github.com/prattpi/piprojects4libraries/blob/8897ebdcd1ff981029cb09a2b27803c40605e747/python3poembot/images/68747470733a2f2f692e6962622e636f2f3659584d4b53332f7261737062657272792d70692d6770696f2d6469616772616d2e706e67.png"/>

The Raspberry Pi should look like this:

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f703338344453512f494d472d373132352e6a7067.jpeg" width="500"/>





## Test the Printer

Make sure that the printer’s power supply is unplugged.

Hold the print button as you plug in the printer’s power supply, and the printer should print out a test page as shown below.

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f58337a346b71312f494d472d363834322e6a7067.jpeg" width="500"/>



Now, boot up the Raspberry Pi by connecting it to its power supply, monitor via HDMI cable, keyboard, mouse, and ethernet cable.

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f726d4d6648747a2f494d472d363835322e6a7067.jpeg" width="700"/>

## Enable the Serial Interface

Open the Terminal and type `sudo raspi-config` and press enter.

You should see the Terminal window change to look something like this:

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f476e794b7479772f323032322d30322d32342d3135323734322d3139323078313038302d7363726f742e706e67.png" width="700"/>

Use the arrow keys to move down and select 3 Interface Options. Press enter.

Afterwards, move down and select P6 Serial Port. Refer to the image below.

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f4e4b71797768532f323032322d30322d32342d3135333034332d3139323078313038302d7363726f742e706e67.png" width="700"/>

When prompted for a login shell, select No. 

Afterwards, select Yes when prompted about enabling serial port hardware. Refer to the image below.

<img src="https://github.com/prattpi/piprojects4libraries/blob/6f3ada18c670631ee8294c51b201f979d2f8932d/python3poembot/images/68747470733a2f2f692e6962622e636f2f593042636e6e672f323032322d30322d32342d3135333234322d3139323078313038302d7363726f742e706e67.png" width="700"/>

The interface should now state that the serial login shell has been disabled, and the serial interface has been enabled.

Press enter to return to the Raspberry Pi Software Configuration Tool. Press the right arrow key twice to highlight Finish and press enter. 

Reboot when asked to do so.


## Test the Printer

Next, open a Terminal window and type `stty -F /dev/serial0 19200`. Replace 19200 if your printer has a different baud rate.

Next, type `echo -e “This is a test.\\n\\n\\n” > /dev/serial0`

After pressing enter, the printer should print “This is a test.” as shown below.

<img src="https://github.com/prattpi/piprojects4libraries/blob/461e13859d0e9eb5d26f658f164cf4093721e7bc/python3poembot/images/68747470733a2f2f692e6962622e636f2f313839597643592f494d472d363834352e6a7067.jpeg" width="500"/>


## Install Updates and Drivers

Return to the Terminal and type `sudo apt-get update`


Next, type the following on one line:

`sudo apt-get -y install git cups wiringpi build-essential libcups2-dev libcupsimage2-dev python3-serial python-pil python-unidecode`

Now we will install the printer driver by typing the following, line by line, hitting enter after each line:

`cd ~`

`git clone https://github.com/adafruit/zj-58`

`cd zj-58`

`make`

`sudo ./install`

Next, we will be making the printer the default printer. To do so, start by typing the following on one line (replace the baud rate of 19200 with your baud rate if applicable):

`sudo lpadmin -p ZJ-58 -E -v serial:/dev/serial0?baud=19200 -m zjiang/ZJ-58.ppd`

Next, type `sudo lpoptions -d ZJ-58`

The printer will now be the default printer.




## Clone the python3poembot Repository and Run It

Open a Terminal window and type the following on one line: 

`git clone https://github.com/prattpi/piprojects4libraries`

Next, type `cd piprojects4libraries/python3poembot`

Type `python3 poemsMain.py` to run the program.

It should print out the following message:

`Hello! Ready to print Golden Treasury poems.`

Press the button, and the printer will print out a poem, as seen in the image below.

<img src="https://github.com/prattpi/piprojects4libraries/blob/461e13859d0e9eb5d26f658f164cf4093721e7bc/python3poembot/images/68747470733a2f2f692e6962622e636f2f5778775a436b6d2f494d472d363838302e6a7067.jpeg" width="500"/>

The contents of the CSV file (accessible by going to the folder icon in the top bar, navigating to piprojects4libraries and into the python3poembot folder) can be changed to fit your interests or the code can point to a different CSV file you may already have.

For more ideas for what to do with the Adafruit thermal receipt printer, feel free to look here: https://learn.adafruit.com/mini-thermal-receipt-printer
