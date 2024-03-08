from pytube import YouTube

try:
    #Ask user to input URL
    url = input("Enter Youtube URL: ")

    yt = YouTube(url)

    print("Title: ", yt.title)

    #Get Highest Resolution
    yd = yt.streams.get_highest_resolution()

    yd.download('./YtDownloads')

    print("Download Complete.")
except Exception as e:
    print("Error", str(e))