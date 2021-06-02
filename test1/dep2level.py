#!/usr/bin/python3
from PIL import Image, ImageSequence
import matplotlib.pyplot as plt
import numpy as np
import warnings
from bluetooth import *

############ For bluetooth! #####################3
# target_name = "ArduinoNanoBLE"
# target_address = None

# nearby_devices = bluetooth.discover_devices()

# for bdaddr in nearby_devices:
#     if target_name == bluetooth.lookup_name( bdaddr ):
#         target_address = bdaddr
#         break

# if target_address is not None:
#     print "found target bluetooth device with address ", target_address
# else:
#     print "could not find target bluetooth device nearby"


# port = 3
# s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# s.connect((serverMACAddress, port))

#######################################################3
im = Image.open("teaser.gif")
area = (0, 150, 480, 290)
#im = im.crop(area)
# resizeImg = imresize(depthImg,[300 410]); % 320 x 240 pixels
index = 1

#########width###########
#
#
# height
#
#
label = np.zeros((480, 140))        
level = np.zeros((10,10))
fig = plt.figure(1)
for frame in ImageSequence.Iterator(im):
    frame = frame.crop(area)
    # frame.save("frame%d.png" % index)
    width, height = frame.size # 480, 140
    channels = 1
    pixel_values = list(frame.getdata())
    pixel_values = np.array(pixel_values).reshape((width, height, channels))

    for posx in range(width-1): # 0~479
        for posy in range(height-1): # 0~139
            if pixel_values[posx][posy] > 230 :
                label[posx,posy] = 8
            elif pixel_values[posx][posy] <= 230 & pixel_values[posx][posy] > 200 :
                label[posx,posy] = 7
            elif pixel_values[posx][posy] <= 200 & pixel_values[posx][posy] > 170 :
                label[posx,posy] = 6
            elif pixel_values[posx][posy] <=170 & pixel_values[posx][posy] > 140 :
                label[posx,posy] = 5
            elif pixel_values[posx][posy] <=140 & pixel_values[posx][posy] > 110 :
                label[posx,posy] = 4
            elif pixel_values[posx][posy] <=110 & pixel_values[posx][posy] > 80 :
                label[posx,posy] = 3
            elif pixel_values[posx][posy] <=80 & pixel_values[posx][posy] > 50 :
                label[posx,posy] = 2
            else :
                label[posx,posy] = 1
    print(label.shape)
   #  for posx in range(0, height, 33) :
   #      for posy in range(0, width, 39) :
   #          level[posx//33,posy//39] = np.around(np.mean(label[posx:posx+33,posy:posy+39]))
			# # s.send(level) ############# for bluetooth!

    for posx in range(0, width, 48) :
        for posy in range(0, height, 14) :
            level[posx//48,posy//14] = np.around(np.mean(label[posx:posx+48,posy:posy+14]))
    index += 1
    print(level)
    np.savetxt("level.csv", level, delimiter=",")

    plt.imshow(frame)
    plt.pause(0.00000001)
