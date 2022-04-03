import schedule
import RPi.GPIO as GPIO
import time
from datetime import datetime
import requests

# sensor pin in bcm mode 
sensor = 7
count = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Callback for rising or falling pin state
def motion_callback(pin):
  global count

  # Get current state, 1 is motion, 0 is no motion
  current_state = GPIO.input(pin)
  
  if current_state == 1:
      count += 1
      print ("Motion detected at " + datetime.now().strftime("%H:%M:%S") + ". The count is " + str(count))

# Set up interrupts
GPIO.add_event_detect(sensor, GPIO.BOTH, callback=motion_callback) 

def send():
    global count
    
    # Add your Google Forms URL, and make sure that it ends with formResponse
    url = 'https://docs.google.com/forms/d/e/1FAIpQLScTGalasn1QsviEU7tinTbpN-ZXaFncP9O2mWwP-f9SOfZpaw/formResponse'
        
    # Add the corresponding entry ID for your form
    form_data = {'entry.2119768208': count}
        
    # This sends the data to the Google Form
    x = requests.post(url, data = form_data)
    
    print ("Data sent to Google Form.")
    
    count = 0
    
# [minutes] can be replaced with [seconds] or [hour]
# go to pypi.org/project/schedule/ to learn more about customizing how often data is sent
schedule.every(1).minutes.do(send)

while True:
    schedule.run_pending()
    time.sleep(1)

# Start looping forever waiting for sensor interrupt
try:  
  while True : pass  
except:
  print ('Exception, quitting...')
  GPIO.remove_event_detect(sensor)
  GPIO.cleanup() 