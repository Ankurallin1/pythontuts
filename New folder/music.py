# import time
# import vlc
# player = vlc.MediaPlayer("john.mp3.mp3")
# #start the music
# player.play()
# #listen music for 10 seconds
# time.sleep(3)
# #stop the music
# player.stop()
# from playsound import playsound
# playsound('john.mp3.mp3')
# import playsound
# playsound.playsound("john.mp3.mp3")
from pygame import mixer

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a== stopper:
            mixer.music.stop()
            break
if __name__ == '__main__':
  print("playing sound")
  musiconloop("john.mp3.mp3","stop")
