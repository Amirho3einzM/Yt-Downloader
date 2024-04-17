from pytube import YouTube
import tkinter as tk
from tkinter import filedialog



def downloader(url,save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("downlaod successfully")
    
    except Exception as e:
        print(e)
        
    
def select_loc():
    folder=filedialog.askdirectory()
    if folder:
        print(f"selected folder: {folder}")
        
    return folder

if __name__=="__main__":
    root=tk.Tk()
    root.withdraw()
    
    video_url = input("Please enter your youtube url: ")
    save_dir= select_loc()
    if save_dir:
        print("start download...")
        downloader(video_url,save_dir)
    else:
        print("invalid save location")
