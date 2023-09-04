# to run --> python <name of the file>
#pip install pytube
#----------------------------------------------------------
from pytube import YouTube
from tkinter import filedialog
url = input("Enter the URL: ")

allStreams = YouTube(url).streams.all() #all the qualities (streams)

#printing the different qualities
i = 0
for stream in allStreams:
    print(str(i+1) + " : " + str(stream))
    i+=1

streamChoiceIndex = int(input("Choose the stream quality index you want:  "))
print("please choose the directory to download in! ")

path = filedialog.askdirectory()
allStreams[streamChoiceIndex-1].download(path)

print("The Video has been downloaded, Yaaaay!")
