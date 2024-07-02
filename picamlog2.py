from picamera2 import Picamera2, Preview
from libcamera import controls
import PIL
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import date

font = PIL.ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",48)
pc2 = Picamera2()
pc2.preview_configuration.size = (2560,1920)
pc2.start(show_preview=True)
while True:
  today = date.today()
  t=time.localtime()
  current_time1=time.strftime(":%H:%M:%S",t)
  current_time=time.strftime("_H%H_M%M_S%S",t)
  fn="photo_"+str(today)+current_time+".jpg"
  pc2.start()
  pc2.set_controls( {"AfMode" : controls.AfModeEnum.Continuous} )
  time.sleep(5)
  pc2.capture_file("temp_.jpg")
  img=Image.open("temp_.jpg")
  draw=ImageDraw.Draw(img)
  draw.text((20, 880), str(today)+current_time1, 'yellow', font=font)
  img.save(fn)
  time.sleep(295)
