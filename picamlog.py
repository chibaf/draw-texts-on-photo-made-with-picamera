from picamera2 import Picamera2, Preview
from libcamera import controls
import time
from datetime import date

pc2 = Picamera2()
pc2.start_preview( True )
while True:
  today = date.today()
  t=time.localtime()
  current_time=time.strftime("_H%H_M%M_S%S",t)
  fn="photo_"+str(today)+current_time+".jpg"
  pc2.start()
  pc2.set_controls( {"AfMode" : controls.AfModeEnum.Continuous} )
  time.sleep( 5 )
  pc2.capture_file(fn)
  time.sleep(295)
