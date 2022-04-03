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
        url = 'https://docs.google.com/forms/d/e/1FAIpQLSe3h6V2dTgCezwEJAwMSsgQ2dJvZfXQrGVkM6p5sQzcE_sK7g/formResponse'
        
        # Replace the three entry IDs with the corresponding entry IDs for your form
        form_data = {'entry.363913385': temperature_f, 'entry.711039572': temperature_c, 'entry.462028969': humidity}
        
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