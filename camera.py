import datetime  
import picamera  
import RPi.GPIO as GPIO  
  
GPIO.setmode(GPIO.BCM)  
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)  
  
while True:  
GPIO.wait_for_edge(24, GPIO.FALLING)  
        dvrname = datetime.datetime.now().strftime("%y%m%d_%H%M%S")  
        with picamera.PiCamera() as camera:  
camera.resolution = (1920, 1080)  
camera.start_preview()  
camera.start_recording('/home/pi/' + dvrname + '.h264')  
GPIO.wait_for_edge(24, GPIO.RISING)  
camera.stop_recording()  
  
GPIO.cleanup()  