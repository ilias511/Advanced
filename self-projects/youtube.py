import pytube


link = input('Enter a youtube link:')
video = pytube.YouTube(link)


print(video.title)
print(video.views)
print(video.channel_url)

download = video.streams.get_audio_only()

print('Downloading...')

download.download()