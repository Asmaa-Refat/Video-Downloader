# to run --> python <name of the file>
#pip install pytube
#----------------------------------------------------------
from pytube import YouTube
from tkinter import filedialog
url = input("Enter the URL: ")

allStreams = YouTube(url).streams.all()

i = 0
for stream in allStreams:
    print(str(i+1) + " : " + str(stream))
    i+=1


streamChoiceIndex = int(input("Choose the stream quality index you want:  "))
print("please choose the direcroty to download in! ")
folderName = filedialog.askdirectory()

allStreams[streamChoiceIndex-1].download(folderName)

print("Video has been downloaded, YaaaaY!!!!!")