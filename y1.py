from pytube import YouTube


def youtubedownloader(url):
 yt = YouTube(url)

 try: 
  tt = yt.streams.filter(mime_type="video/mp4" , progressive =True , res = '1080p').first()

  return tt.download(filename = 'youtube.mp4' , output_path = '.')
 except:
  try:
     tt = yt.streams.filter(mime_type="video/mp4" , progressive =True , res = '720p').first()
     return tt.download(filename = 'youtube.mp4' ,output_path = '.')
  except:
     tt = yt.streams.filter(mime_type="video/mp4" , progressive =True).first()
     return tt.download(filename = 'youtube.mp4' , output_path = '.')



