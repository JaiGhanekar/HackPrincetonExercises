from time import sleep
from myo import init, Hub, DeviceListener
import myo as libmyo




class Listener(DeviceListener): 




    def on_pair(self, myo, timestamp, firmware_version):
        print("Hello, Myo!")

    def on_unpair(self, myo, timestamp):
        print("Goodbye, Myo!")

    def on_orientation_data(self, myo, timestamp, quat):
        # print("Orientation:", quat.x, quat.y, quat.z, quat.w)
        

        if quat.w <=  -0.05:
            print("W-axis failure")
            myo.vibrate("short")
        elif quat.x >  0.6:
            print("X-axis failure")
            myo.vibrate("short")
        elif quat.y > 0.8:
            print("Y-axis failure")
            myo.vibrate("short")
        elif quat.z > 0.1:
            print("Z-axis failure")
            myo.vibrate("short")
        else:
            print("Good job!")

    def set(self, keyPress):
        print('set')
        if (keyPress == " "):
            print("hi")
            #originPoint = [quad.w, quad.x, quad.y, quad.z]


libmyo.init('~/Downloads/sdk/myo.framework')
#expects list
listener = Listener()
hub = Hub()
hub.run(1000, listener)

try:
    while True:
        sleep(0.5)
except KeyboardInterrupt:
    print('\nQuit')
finally:
    hub.shutdown()  # !! crucial