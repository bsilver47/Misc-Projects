from pytube import YouTube
from moviepy.editor import *

def main():
    link = input("What is the link to the video you want to download? ")
    video_name = input("What would you like the file to be named? ")
    vname = (f"{video_name}.mp4")
    aname = (f"{video_name}.mp3")
    youtube_video = video_download(link, vname)
    print(youtube_video)   
    audio_file = mp4_to_mp3(vname, aname)
    print(audio_file)

def video_download(link, vname):
    try:
        yt = YouTube(link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1]
        video.download(filename=vname)
        return "Video Download Complete"
    except:
        return "Failed Video"

def mp4_to_mp3(vname, aname):
    try:
        video = VideoFileClip(vname)
        audio = video.audio
        audio.write_audiofile(aname)
        return "Audio Download Complete"
    except:
        return "Failed Audio"

if __name__ == "__main__":
    main()
