from pytube import YouTube, streams

url = input(str('DIGITE A URL DO VÍDEO: '))
video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path='XXX')

print('DOWNLOAD CONCLUIDO!')
