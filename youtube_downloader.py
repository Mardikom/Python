#not work
from pytube import YouTube

video_url = input("Enter the video url: ")
download_folder = input("Enter the download folder: ")
video_obj = YouTube(video_url)
stream = video_obj.streams.get_highest_resolution()
stream.download(download_folder)

#https://www.youtube.com/watch?v=xWDf0WSWKXw