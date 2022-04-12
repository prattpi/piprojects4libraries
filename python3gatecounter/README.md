# Gate Counting with Raspberry Pi


## Equipment
* Raspberry Pi
* Raspberry Pi power supply
* Micro SD card
* PIR sensor
* 3x female-female jumper wires
* Monitor
* Keyboard
* Mouse
* Ethernet cable
* HDMI cable



## Connect Raspberry Pi to PIR Sensor
The PIR Sensor has three pins, and these three pins will be connected to the Raspberry Pi using the 3 female-female jumper wires.

First, plug three ends of the jumper wires onto the PIR sensor.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/bbc321ad7de563d6d923dd45d94603d13a1d0a4a/python3gatecounter/images/Picture1.png" width = 600>



Next, take a look at the Raspberry Pi and make sure the side with all the pins is facing up. Using the chart below, locate Pin 01 (the only pin with a square base) as a frame of reference.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/d3892c0b9d0e9e2e8c7c26b4a9de9d587d106462/python3gatecounter/images/raspberrypi_pins.png" width = 600>

https://pinout.xyz is also a good resource for locating where each pin is.

Start plugging in the jumper wires connected to the PIR sensor to the Raspberry Pi as indicated in the chart below:

| PIR Sensor  | Raspberry Pi |
| ------------- | ------------- |
| GND  | Ground (Pin 06)  |
| V+ (power positive pin)  | 3.3v (Pin 01)  |
| S (signal pin)  | GPIO07 (Pin 26)  |


The Raspberry Pi should look like this:

<img src="https://github.com/prattpi/piprojects4libraries/blob/540c8d9182b4baca08a675582f91e664bf1711da/python3gatecounter/images/pi_hooked_up_to_sensor.jpg" width=600>

Once everything has been connected, plug your monitor, keyboard, mouse, ethernet cable, HDMI cable, and the Raspberry Pi power supply into the Raspberry Pi to start it up.

<img src="https://github.com/prattpi/piprojects4libraries/blob/540c8d9182b4baca08a675582f91e664bf1711da/python3gatecounter/images/pi_hooked_up_to_sensor2.jpg" width=600>

## Create a Google Form to Collect Data
Navigate to Google Drive, and create a new form.

In this form, create the following “question”: COUNT

The input section for each question can simply be the short answer text option. See the screenshot below for reference.

<img src ="https://github.com/prattpi/piprojects4libraries/blob/540c8d9182b4baca08a675582f91e664bf1711da/python3gatecounter/images/google_form.png" width=600>

Afterwards, click on the Responses tab and the Google Sheets icon to create a spreadsheet of responses.
<img src = "https://github.com/prattpi/piprojects4libraries/blob/540c8d9182b4baca08a675582f91e664bf1711da/python3gatecounter/images/google_form2.png" width=600>

# Cloning the Python File
Go to the Raspberry Pi icon in the top left corner, and open an IDE in the Programming dropdown, such as Thonny Python IDE or Geany. Type the following: 

`git clone https://github.com/prattpi/piprojects4libraries`

Next, type `cd piprojects4libraries/python3gatecounter`

Then type `python3 gatecounter.py` to run the program.

## Editing the Python File

Return to the Google Form, click the eye icon in the top right corner to open up a preview of the form. 

Inspect the form by right-clicking and selecting “Inspect.”

<img src = "https://github.com/prattpi/piprojects4libraries/blob/161d5cd6941f8822711288dad495ab68ff6e88c9/python3gatecounter/images/google_form_inspect.png" width=100%>

In the element inspection window, press Control+F to open the find window. In the find window, search for “entry.” You should find one value that begins with “entry.” followed by a string of numbers, as seen below.


<img src ="https://github.com/prattpi/piprojects4libraries/blob/bec72368353b096aa41c27f038ba6760d6a4bd1a/python3gatecounter/images/google_form_inspect2.png" width=100%>

Switch back to your Python IDE, and on line 32, replace the URL value with your Google Form URL. Make sure that the URL ends in `formResponse` insead of `viewform`. 

On line 35, replace the entry ID variable (entry.XXXXXXXXXX) with the entry ID found by inspecting the webpage.

Refer to the screenshot below for an example.

<img src ="https://github.com/prattpi/piprojects4libraries/blob/abaaa00fd8dbf4169f77e16bb0c75ccbf7aa4951/python3gatecounter/images/screenshot_python.png" width = 100%>

Once changed, press save.

## Install Python Schedule
Navigate to the terminal on your Raspberry Pi, and type the following:

`sudo python3 -m pip install schedule`

This will install a Python scheduler that will make it possible to send data to the Google Form after a specific time interval.

## Run the Program
Go back to the Terminal, and type `cd piprojects4libraries/python3gatecounter` to navigate to the project in your directories. Afterwards, type the following and press enter:

`python3 gatecounter.py`

As the PIR sensor picks up data, it will be displayed in the Terminal and the count will increase with each new motion. Each new motion only registers if there is a distinct period of no movement after the motion; if too many motions happen within the same time period, it will be registered as one motion.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/89e2d1bdf3fa143fff840304eb0b898374797b6f/python3gatecounter/images/screenshot_terminal.png" width = 800>

The data will be sent in 1-minute intervals to the Google Form, and can be viewed in the Responses sheet as seen in the screenshot below. If you want to confirm that the motion sensor counts are correctly being recorded in your Google Form, wait 1 minute until you see ‘Data sent to Google Form’ before stopping the program. 

Press Ctrl+C in the terminal to stop the program.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/540c8d9182b4baca08a675582f91e664bf1711da/python3gatecounter/images/google_sheet.png" width = 600> 


## Changing How Often the Data is Sent

Currently, the data will be aggregated and sent to the Google Form every minute. To change this, go to line 46.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/a10243c725a972c1950d91af961b57e58484900d/python3gatecounter/images/screenshot_python2.png" width = 100%>

The `minutes` can be changed to `seconds` or `hour` depending on your preference, and the variable inside the parentheses (which is 1 in this case) can also be changed.

For instance, if you would like the data to be aggregated and sent to the Google Form every ten minutes, change line 46 to the following:

`schedule.every(10).minutes.do(send)`

Or, if you would prefer to send data every hour, change line 46 to:

`schedule.every().hour.do(send)`

https://pypi.org/project/schedule/ is also a great resource for further customizing how often the data will be sent to the Google Form.

## Automating Gate Counting with Crontab
It is also possible to have the program run as soon as the system has been booted up, which means that you will not have to go into the Terminal and start up the program every time.

To accomplish this, we will be adding a new job for Crontab, a job scheduler, to run upon reboot.

To begin, open the `gatecounter.py` file and add `time.sleep(15)` under `import requests` found on line 5 like so:

<img src = "https://github.com/prattpi/piprojects4libraries/blob/2c4f152a020c4b55a1e1431c956e75cb30c87485/python3gatecounter/images/screenshot_python3.png" width = 100%>

This will ensure that all the frameworks will have time to boot up before the program is run automatically (15 seconds after booting up).

Press save.

Open a Terminal window and type `crontab -e` and when prompted, type `1` to select the nano editor.

Your Terminal window should now look something like this:

<img src = "https://github.com/prattpi/piprojects4libraries/blob/859e9b958408e4ac905e4dd2dd0e6aff53cf9ef9/python3gatecounter/images/screenshot_terminal2.png" width = 800>

Scroll down to the very bottom of the file (use your keyboard arrow buttons to scroll in the terminal), and type the following line:

`@reboot /usr/bin/python3 /home/pi/piprojects4libraries/python3gatecounter/gatecounter.py`

Refer to the screenshot below (*please note that the filepath included in the screenshot below is different than the filepath you will enter here).

<img src = "https://github.com/prattpi/piprojects4libraries/blob/6a8b9fce75ab4518d36b1c1301da085b89de1b90/python3gatecounter/images/screenshot_terminal3.png" width=800>

Press Ctrl+X to Exit, press Y to save, and press the Enter key to return to the Terminal. You should see the following text: `crontab: installing new crontab.`

To view what you have written, type `crontab -l`, and to edit what you wrote, type `crontab -e`.

To test your scheduled job, type `sudo reboot` to reboot the system. About 15 seconds after the Pi has rebooted, the Pi will start recording gate counting data and send that data to the Google Form.

If you would like to stop the automated gate counting, return to the editor via `crontab -e` and add a `#` in front of `@reboot /usr/bin/python3 /home/pi/piprojects4libraries/python3gatecounter/gatecounter.py`. Refer to the screenshot below.

<img src = "https://github.com/prattpi/piprojects4libraries/blob/ff4f68bfd9f945a74dbd6f00b43c2fd5ce739f56/python3gatecounter/images/screenshot_terminal4.png" width = 800>

Doing so comments out the line and once you reboot the system, the gate counting will no longer be automated. If you would like to re-enable the automated temperature readings, remove the #.
