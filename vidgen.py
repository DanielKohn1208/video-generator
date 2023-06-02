import requests
from moviepy.editor import *


def vidgen():
    print("Fetching quote ...")
    # getting quote
    response = requests.get('https://zenquotes.io/api/random/')

    json = response.json()
    author = json[0]['a']
    quote = json[0]['q']

    print('author: ' + author)
    print('quote: ' + quote)

    print("Generating video ...")

    img = ImageClip('resources/sunset.png', ismask=False).set_duration(10)
    music = AudioFileClip('resources/music.mp3').subclip(60, 70)

    text = TextClip(quote + " -" + author,
                    font="FreeSans-Bold",
                    fontsize=60,
                    color="black",
                    size=img.size,
                    method='caption',
                    stroke_color="white",
                    stroke_width=2,
                    )
    text = text.set_position('center').set_duration(10)
    color = ColorClip(color=[77, 166, 255], size=img.size).set_duration(10)
    video = CompositeVideoClip([color, img, text])
    videoWithAudio = video.set_audio(music)
    videoWithAudio.write_videofile('out.mp4', fps=15)


if __name__ == "__main__":
    vidgen()
