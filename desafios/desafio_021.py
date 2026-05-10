import vlc
import time

player = vlc.MediaPlayer("../src/audio.mp3")
player.play()
time.sleep(1)
while player.is_playing():
    time.sleep(0.5)
    