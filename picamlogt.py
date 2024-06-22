from picamera2 import Picamera2, Preview
from libcamera import controls
import PIL
from PIL import Image, ImageDraw, ImageFont
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
  time.sleep(5)
  pc2.capture_file("tempp.jpg")
  img=Image.open("tempp.jpg")
  draw=ImageDraw.Draw(img)
  draw.text((75, 50), current_time, 'red')
  img.save(fn)
  time.sleep(5)
