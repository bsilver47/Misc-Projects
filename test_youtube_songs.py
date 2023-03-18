from Youtube_Songs import video_download, mp4_to_mp3
import pytest
from pytube import YouTube
from moviepy.editor import *

def test_video_download(link="link", vname="name"):
    vid_download = video_download(link, vname)
    return vid_download

def test_mp4_to_mp3(vname="vname", aname="aname"):
    aud_download = mp4_to_mp3(vname, aname)
    return aud_download

videos_dict = {
    "All Creatures Of Our God And King": ["https://www.youtube.com/watch?v=3wrUd1CrVm0"],
    "More Than A Feeling / Long Time": ["https://www.youtube.com/watch?v=IjW6SbLT5NE"],
    "In Christ Alone": ["https://www.youtube.com/watch?v=WQCpxt0XRoc"],
    "Nocturne": ["https://www.youtube.com/watch?v=s1XJGS4QFTs"],
    "Where Can I Turn for Peace (I Believe in Christ)": ["https://www.youtube.com/watch?v=buPE9Et8Zlw"],
    "This Is The Christ": ["https://www.youtube.com/watch?v=ae0HhqVCtRM"],
    "The Spirit of God": ["https://www.youtube.com/watch?v=QWoeNWqU_48"]
}

video_fails_dict = {
    "The First Fail": ["NotALink"],
    "The Second Fail": ["https://mail.google.com/"],
    "The Third Fail": ["https://fb.watch/hjPINTNRQW/"]
}

def main():
    for name in videos_dict:
        link = (videos_dict[name])[0]
        vname = f"{name}.mp4"
        aname = f"{name}.mp3"
        vid_test = test_video_download(link, vname)
        print(vid_test)
        aud_test = test_mp4_to_mp3(vname, aname)
        print(aud_test)
        assert vid_test.find("Video Download Complete") != -1
        assert aud_test.find("Audio Download Complete") != -1

    for name in video_fails_dict:
        link = (video_fails_dict[name])[0]
        vname = f"{name}.mp4"
        aname = f"{name}.mp3"
        vid_test = test_video_download(link, vname)
        aud_test = test_mp4_to_mp3(vname, aname)
        assert vid_test.find("Video Download Complete") == -1
        assert aud_test.find("Audio Download Complete") == -1

pytest.main(["-v", "--tb=line", "-rN", __file__])
