# draw-texts-on-photo-made-with-picamera
draw texts on photo made with picamera

## code

<pre>
font = PIL.ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",48)
pc2 = Picamera2()
pc2.start_preview( True )
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
  draw=ImageDraw.Draw(img)
  draw.text((20, 440), str(today)+current_time1, 'yellow', font=font)
  img.save(fn)
  time.sleep(295)
</pre>

## references

Python, Pillowで文字（テキスト）を描画、フォント設定 | note.nkmk.me

https://note.nkmk.me/python-pillow-imagedraw-text-imagefont/

Fonts and PIL ImageFont ignorance - Raspberry Pi Forums

https://forums.raspberrypi.com/viewtopic.php?t=342857
