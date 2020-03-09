import time,math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinList, GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
PolarityPins = [29,31]
TimeDelayIncrease = 999 #Increase to slower the delay
TimeDelayDecrease = 999 #Increase to slower the delay
TimeRiding = 5;
outputPWM = 0;
incrementation=1;

def ForSin(start,end,pin):
  p = GPIO.PWM(32, 1000)
  p.stop()
  if start>end:
    incrementation = -1;
    GPIO.output(PolarityPins, (GPIO.HIGH, GPIO.LOW))
  else:
    incrementation = 1;
    GPIO.output(PolarityPins, (GPIO.LOW, GPIO.HIGH))
  for x in range(start,end,incrementation):
    outputPWM=math.sin(math.radians(x))
    outputPWM=round(outputPWM,3)
    p.start(outputPWM)
    print(outputPWM)
    if start<end:
      time.sleep( 1 / TimeDelayIncrease)
    if start>end:
      time.sleep( 1 / TimeDelayDecrease)



for x in range(0,1000):
  GPIO.output(pinList, GPIO.LOW)
  GPIO.output(PWMPin, GPIO.LOW)
  TimeDelayIncrease=int(input("Time delay increase: "))
  TimeDelayDecrease=int(input("Time delay decrease: "))
  TimeRiding=int(input("Time Riding: "))
  ForSin(0,91,12)
  time.sleep(TimeRiding)
  ForSin(90,-1,12)
  #p.stop()
  print("Increase Time Delay is",TimeDelayIncrease)
  print("Decrease Time Delay is",TimeDelayDecrease)
  print("Time Riding is",TimeRiding)
  input("Press enter to continue")
  GPIO.cleanup()

#GPIO.cleanup()
