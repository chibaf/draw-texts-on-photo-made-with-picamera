from picamera2 import Picamera2, Preview
from libcamera import controls
import PIL
from PIL import Image, ImageDraw, ImageFont
import time
from datetime import date

font = PIL.ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",48)
pc2 = Picamera2()
config = pc2.create_still_configuration(lores={"size": (1280,960)}, display="lores")
pc2.configure(config)
pc2.start_preview(True)
pc2.resolution = (1280,960)
pc2.framerate = 15
while True:
  today = date.today()
  t=time.localtime()
  current_time1=time.strftime(":%H:%M:%S",t)
  current_time=time.strftime("_H%H_M%M_S%S",t)
  fn="photo_"+str(today)+current_time+".jpg"
  pc2.start()
  pc2.set_controls( {"AfMode" : controls.AfModeEnum.Continuous} )
  time.sleep(5)
  pc2.capture_file("tempp.jpg")
  img=Image.open("tempp.jpg")
#  img_resize = img.resize((1280,960))
  draw=ImageDraw.Draw(img) #_resize)
  draw.text((20, 880), str(today)+current_time1, 'yellow', font=font)
#  img_resize.save(fn)
  img.save(fn)
#  pc2.stop_preview( True )
  time.sleep(5)
