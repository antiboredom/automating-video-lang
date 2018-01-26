import glob
import random
from vidpy import Clip, Composition, config
config.MELT_BINARY = '/Applications/Shotcut.app/Contents/MacOS/qmelt'


def make_hands():
    clips = []

    backgrounds = glob.glob('images/*.jpg')
    background_clip = Clip(random.choice(backgrounds))

    clips.append(background_clip)

    hands = glob.glob('hands/*.mp4')
    hand = random.choice(hands)

    x = random.randint(-400, -200)
    distance = 100

    duration = 0

    for i in range(0, 6):
        clip = Clip(hand)
        clip.chroma()
        clip.fadein(0.1)
        clip.fadeout(0.1)
        clip.set_offset(i * 0.5)
        clip.position(x=x)
        clips.append(clip)

        x += distance
        duration = clip.duration + i * 0.5


    composition = Composition(clips, width=1280, height=720, duration=duration)
    composition.preview()


make_hands()

