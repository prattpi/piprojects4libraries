# Digital Signage with Raspberry Pi

Screenly Open Source Edition (OSE) is a free digital signage software that runs on the Raspberry Pi.

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

<img src = "https://github.com/prattpi/piprojects4libraries/blob/10d28c9674ab88246338f766453e8216e2864d46/screenlydigitalsignage/images/raspberry%20pi%20equipment%20with%20labels.jpg" width = 800>

## Setting Up Screenly OSE
Download the Screenly OSE zip file (the disk image) of the latest sprint from [Screenly’s Github releases page](https://github.com/Screenly/screenly-ose/releases).

<img src = "https://github.com/prattpi/piprojects4libraries/blob/ad1386d708b0d8cf06632be47fc251b4ee5102d3/screenlydigitalsignage/images/Screen%20Shot%202021-11-17%20at%201.12.08%20PM.png" width = 800>

Download Etcher from [balena’s website](https://www.balena.io/etcher/).

Insert the micro SD card into a card reader, and connect to a computer.

Using balena Etcher, flash the disk image onto the micro SD card.

<img src ="https://github.com/prattpi/piprojects4libraries/blob/ad1386d708b0d8cf06632be47fc251b4ee5102d3/screenlydigitalsignage/images/Capture.PNG" width = 800>

## Setting up your Raspberry Pi
Once you are done imaging your SD card with the Raspberry Pi OS, it is time to start up the Pi. Connect the Raspberry Pi Power Supply to the Pi, and insert the SD card into it. Connect the Pi with the Monitor using the HDMI cable. Connect the mouse and keyboard to the Pi. Plug in the Ethernet cable to a working port and connect it to the Pi to access the internet.

Check for a blinking red light on your Pi to ensure it is being supplied with power. To check for a working internet connection, look for a yellow blinking light inside the port for the ethernet cable.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/10d28c9674ab88246338f766453e8216e2864d46/screenlydigitalsignage/images/Raspberry%20Pi%20ON.jpg" width = 300> <img src = "https://github.com/prattpi/piprojects4libraries/blob/10d28c9674ab88246338f766453e8216e2864d46/screenlydigitalsignage/images/SD%20card%20in%20Pi.jpg" width = 300>

<img src = "https://github.com/prattpi/piprojects4libraries/blob/10d28c9674ab88246338f766453e8216e2864d46/screenlydigitalsignage/images/Yellow%20Light%20for%20internet.jpg" width = 600>

## Using Screenly OSE

On your secondary laptop, computer, or phone, navigate to the IP address displayed on the screen when Screenly boots up.

<img src ="https://github.com/prattpi/piprojects4libraries/blob/ad1386d708b0d8cf06632be47fc251b4ee5102d3/screenlydigitalsignage/images/IMG_5708.png" width = 800>

Click “Add Asset” on the Screenly asset management page to add an asset.

<img src ="https://github.com/prattpi/piprojects4libraries/blob/ad1386d708b0d8cf06632be47fc251b4ee5102d3/screenlydigitalsignage/images/Screen%20Shot%202021-11-11%20at%202.13.45%20PM.png" width = 800>

Add an asset by pasting the URL or uploading a file.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/ad1386d708b0d8cf06632be47fc251b4ee5102d3/screenlydigitalsignage/images/Screen%20Shot%202021-11-11%20at%202.14.17%20PM.png" width = 800>

After toggling the “Activity” slider, the uploaded image should now appear on your Screenly monitor.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/ad1386d708b0d8cf06632be47fc251b4ee5102d3/screenlydigitalsignage/images/Screen%20Shot%202021-11-11%20at%202.15.11%20PM.png" width = 800>

<img src = "https://github.com/prattpi/piprojects4libraries/blob/ad1386d708b0d8cf06632be47fc251b4ee5102d3/screenlydigitalsignage/images/IMG_5715.png" width = 800>

This is what a usual set-up of Screenly with Raspberry Pi looks like.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/10d28c9674ab88246338f766453e8216e2864d46/screenlydigitalsignage/images/20230528_110006.jpg" width = 800>

