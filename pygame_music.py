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
  musiconloop("popit.mp3","stop")

# Starting the mixer
#mixer.init()

# Loading the song
