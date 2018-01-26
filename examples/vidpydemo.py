import glob
from vidpy import Clip, Composition, Text

clips = []

face_files = glob.glob("face*.mp4")


start = 0
for f in face_files:
    clip = Clip(f)
    clip.set_offset(start)
    clip.repeat(20)
    clip.opacity(.5)
    clips.append(clip)
    start += .5

textclip = Text("Your faces look cool!", font="Comic Sans MS", color="#ff0000")
clips.append(textclip)
comp = Composition(clips)
comp.preview()


# clip1 = Clip("face-5.mp4")
# clip1.repeat(50)
# clip1.fx('frei0r.cartoon', {'0': .999})
#
# comp = Composition([clip1])
# comp.preview()


# clip2 = Clip("face-3.mp4")

# clip1.repeat(100)
# clip1.chroma()
# clip2.spin(-2)
#
#
# clip2.repeat(100)
# clip2.chroma(color="#000000")
# clip2.spin(20)
#
# # clip2.zoompan(['-100%', 0, '0%', '0%'], [0, 0, '100%', '100%'], start=0, end=200)
#
# # clip2.repeat(3)
# # clip2.fadein(1)
# #
# # clip1.set_offset(2).fadein(2)
# # clip2.spin(3)
# # clip2.position(x=100, y=100, w="20%", h="20%")
#
# # comp = Composition([clip1, clip2], singletrack=True)
# comp = Composition([clip1, clip2], bgcolor="#ff0000", duration=3)
#
# comp.save('whatever.mp4')
