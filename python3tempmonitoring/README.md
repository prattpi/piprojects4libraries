# Temperature Monitoring with Raspberry Pi


## Equipment
* Raspberry Pi
* Raspberry Pi power supply
* Micro SD card
* DHT11 temperature sensor
* 3x female-female jumper wires
* Monitor
* Keyboard
* Mouse
* Ethernet cable
* HDMI cable


## Connect Raspberry Pi to DHT11 Temperature Sensor
The DHT11 temperature sensor has three pins, and these three pins will be connected to the Raspberry Pi using the 3 female-female jumper wires.

First, plug three ends of the jumper wires onto the DHT11 temperature sensor.

Next, take a look at the Raspberry Pi and make sure the side with all the pins is facing up. Using the chart below, locate Pin 01 (the only pin with a square base) as a frame of reference.



Start plugging in the jumper wires connected to the PIR sensor to the Raspberry Pi as indicated in the chart below, as well as the graphic above:

| PIR Sensor  | Raspberry Pi |
| ------------- | ------------- |
| S  | GPIO04 (Pin 07)  |
| + | 5v (Pin 02)  |
| - | Ground (Pin 06)  |

The Raspberry Pi should look like this:


Once everything has been connected, plug your monitor, keyboard, mouse, ethernet cable, HDMI cable, and the Raspberry Pi power supply into the Raspberry Pi to start it up.

## Create a Google Form to Collect Data

Navigate to Google Drive, and [create a new form](https://support.google.com/a/users/answer/9302965).

In this form, create the following “questions”:
* Fahrenheit
* Celsius
* Humidity

The input section for each question can simply be the short answer text option. See the screenshot below for reference.



Afterwards, click on the Responses tab and the Google Sheets icon to create a spreadsheet of responses.




## Installing CircuitPython Libraries on Raspberry Pi
Open the Terminal. Input the following, and press enter after each line:

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3-pip
    sudo pip3 install --upgrade setuptools

Then type the following commands, and press enter after each line.

    cd ~
    sudo pip3 install --upgrade adafruit-python-shell

Type the following and press enter.

    wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py

Afterwards, type the following commands and press enter to install the CircuitPython-DHT library.

    sudo python3 raspi-blinka.py
    pip3 install adafruit-circuitpython-dht  
    sudo apt-get install libgpiod2



## Creating the Python File

Go to the Raspberry Pi icon in the top left corner, and open an IDE in the Programming dropdown, such as Thonny Python IDE or Geany. 

Copy and paste the following code into a new file:

    # SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
    # SPDX-License-Identifier: MIT

    import time
    import board
    import adafruit_dht
    import requests

    # Initial the dht device, with data pin connected to:
    dhtDevice = adafruit_dht.DHT11(board.D4)

    # you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
    # This may be necessary on a Linux single board computer like the Raspberry Pi,
    # but it will not work in CircuitPython.
    # dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

    while True:
      try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity

        # Replace the URL below with your Google Forms URL, and make sure that it ends with formResponse
        url = 'https://docs.google.com/forms/d/e/FORMID/formResponse'
        
        # Replace the three entry IDs with the corresponding entry IDs for your form
        form_data = {'entry.#########': temperature_f, 'entry.#########': temperature_c, 'entry.#########': humidity}
        
        # This sends the data to the Google Form
        x = requests.post(url, data = form_data)

        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    # The 2.0 refers to  time (seconds) that elapses between each reading. Currently, this is set to 2 seconds, but feel free to change this value as you see fit
    time.sleep(2.0)

Save the file as `temp.py` on your Desktop.

## Edit the Python File

Return to the Google Form, click the eye icon in the top right corner to open up a preview of the form. 

Inspect the form by right-clicking and selecting “Inspect.”



In the element inspection window, press Control+F to open the find window. In the find window, search for “entry.” You should find three values that begin with “entry.” followed by a string of numbers, as seen below.



Switch back to your Python IDE, and on line 24, replace the URL value with your Google Form URL. Make sure that the URL ends in `formResponse` insead of `viewform`. Refer to the screenshot below for an example.



On line 27, replace the three entry IDs (entry.#########) with the three entry IDs found by inspecting the webpage.

Afterwards, save the file.



## Run the Program

Go back to the Terminal, and type `cd Desktop` to navigate to directories in your desktop. Afterwards, type the following and press enter:

`python3 temp.py`

You should see temperature readings (in Fahrenheit and Celsius, along with the humidity) in the Terminal.



You should also see temperature readings sent to your Google Form (and Sheet) as seen below:


Press `Ctrl+C` in the Terminal to stop the program.

If you would like to set the number of seconds that elapses between each reading, return to the Python file and change the value in the parentheses on line 48. 

For instance, if you would like the time between each reading to be 10 minutes, replace `2.0` with `600`.


## Automating Temperature Readings with Crontab
It is also possible to have the program run as soon as the system has been booted up, which means that you will not have to go into the Terminal and start up the program every time.

To accomplish this, we will be adding a new job for Crontab, a job scheduler, to run upon reboot.

To begin, open the `temp.py` file from your Desktop and add `time.sleep(15)` under import requests found on line 7 like so:



This will ensure that all the frameworks will have time to boot up before the program is run automatically (15 seconds after booting up).

Press save.

Open a Terminal window and type `crontab -e` and when prompted, type `1` to select the nano editor.

Your Terminal window should now look something like this:



Scroll down to the very bottom of the file (use your keyboard arrow buttons to scroll in the terminal), and type the following line:

`@reboot /usr/bin/python3 /home/pi/Desktop/temp.py`

Refer to the screenshot below.


Press Ctrl+X to Exit, press Y to save, and press the Enter key to return to the Terminal. You should see the following text: `crontab: installing new crontab`.

To view what you have written, type `crontab -l`, and to edit what you wrote, type `crontab -e`.

To test your scheduled job, type sudo reboot to reboot the system. About 15 seconds after the Pi has rebooted, you should be able to see more data sent to your Google Form and Google Sheets documents.

If you would like to stop the automated temperature readings, return to the editor via `crontab -e` and add a `#` in front of `@reboot /usr/bin/python3 /home/pi/Desktop/temp.py`. Refer to the screenshot below.



Doing so comments out the line, and once you reboot the system, the temperature readings will no longer be automated. If you would like to re-enable the automated temperature readings, remove the `#`.

