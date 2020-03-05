import time,math
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(12, GPIO.OUT)

TimeDelayIncrease = 999 #Increase to slower the delay
TimeDelayDecrease = 999 #Increase to slower the delay
TimeRiding = 5;
outputPWM = 0;
incrementation=1;

def ForSin(start,end,pin):
  if start>end:
    incrementation = -1;
  else:
    incrementation = 1;
  for x in range(start,end,incrementation):
    outputPWM=math.sin(math.radians(x))
    outputPWM=round(outputPWM,3)
    #p = GPIO.PWM(pin, outputPWM)
    print(outputPWM)
    if start<end:
      time.sleep( 1 / TimeDelayIncrease)
    if start>end:
      time.sleep( 1 / TimeDelayDecrease)

#p.start()


for x in range(0,1000):
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

#GPIO.cleanup()

