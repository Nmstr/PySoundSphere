# uncomment if you have copied the git repo instead of installing the package and copying the file
#import sys; import os; sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import PySoundSphere
import time

player = PySoundSphere.AudioPlayer("sounddevice")
player.load("path/to/your/audio_file")
player.volume = 0.025
player.play()

time.sleep(10)
