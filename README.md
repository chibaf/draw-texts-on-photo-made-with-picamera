# draw-texts-on-photo-made-with-picamera
draw texts on photo made with picamera

## code:  picamlogt.py

<pre>
font = PIL.ImageFont.truetype("/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",48)
pc2 = Picamera2()
pc2.preview_configuration.size = (2560,1920)
pc2.start(show_preview=True)
while True:
  try:
	  today = date.today()
	  t=time.localtime()
	  current_time1=time.strftime(":%H:%M:%S",t)
	  current_time=time.strftime("_H%H_M%M_S%S",t)
	  fn="./"+sys.argv[1]+"/photo_"+str(today)+current_time+".jpg"
	  pc2.start()
	  pc2.set_controls( {"AfMode" : controls.AfModeEnum.Continuous} )
	  time.sleep(5)
	  pc2.capture_file("./"+sys.argv[1]+"/temp_.jpg")
	  img=Image.open("./"+sys.argv[1]+"/temp_.jpg")
	  draw=ImageDraw.Draw(img)
	  draw.text((20, 880), str(today)+current_time1, 'yellow', font=font)
	  img.save(fn)
	  time.sleep(295)
  except KeyboardInterrupt:
    os.remove("./"+sys.argv[1]+"/temp_.jpg")
</pre>

## usage:
<pre>
  python3 picamlog2.py sub_directory
</pre>

## references

Python, Pillowで文字（テキスト）を描画、フォント設定 | note.nkmk.me

https://note.nkmk.me/python-pillow-imagedraw-text-imagefont/

Fonts and PIL ImageFont ignorance - Raspberry Pi Forums

https://forums.raspberrypi.com/viewtopic.php?t=342857
