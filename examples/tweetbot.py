import json
import subprocess
from vidpy import Clip, Composition
from twython import Twython

with open('creds.json') as infile:
    creds = json.load(infile)

APP_KEY = creds['APP_KEY']
APP_SECRET = creds['APP_SECRET']
OAUTH_TOKEN = creds['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = creds['OAUTH_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

subprocess.call(['say', 'you are now being recorded'])
subprocess.call(['/usr/local/bin/ffmpeg', '-f', 'avfoundation', '-pixel_format', 'yuyv422', '-framerate', '30', '-video_size', '1280x720', '-i', '0:0', '-t', '00:00:10', '-y', 'webcamrecord.mp4'])

clips = []

for i in range(0, 10):
    clip = Clip('webcamrecord.mp4', start=i, end=i+2, offset=i*0.4)
    clip.opacity(0.3)
    clips.append(clip)

comp = Composition(clips, bgcolor='red')
comp.save('creeper.mp4')

videodata = open('creeper.mp4', 'rb')
response = twitter.upload_video(media=videodata, media_type='video/mp4')
media_id = response['media_id']
twitter.update_status(status='Automated web cam portrait', media_ids=[media_id])
