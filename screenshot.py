from PIL import ImageGrab
import time

def screenshot(i):
      
      current_time = 0
      time_string = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
      ss_region = (200,0,2000,1080)
      ss_img = ImageGrab.grab(ss_region)
      ss_img.save(f"screen\\{i}, time is {time_string}.jpg")
#screenshot(1)