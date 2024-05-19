import os
import tkinter as tk
from tkinter import filedialog
import pygame

def browse_music():
    file_paths = filedialog.askopenfilenames(filetypes=[("Audio files", "*.mp3")])
    playlist.extend(file_paths)
    for file_path in file_paths:
        filename = os.path.basename(file_path)
        listbox.insert(tk.END, filename)

def play_music():
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        selected_song = playlist[index]
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

root = tk.Tk()
root.title("Music Player")

playlist = []

frame1 = tk.Frame(root)
frame1.pack(padx=10, pady=10)

listbox = tk.Listbox(frame1, selectmode=tk.SINGLE, width=40, height=10)
listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame1, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

frame2 = tk.Frame(root)
frame2.pack(padx=10, pady=10)

browse_button = tk.Button(frame2, text="Add Music", command=browse_music)
play_button = tk.Button(frame2, text="Play", command=play_music)
stop_button = tk.Button(frame2, text="Stop", command=stop_music)

browse_button.grid(row=0, column=0)
play_button.grid(row=0, column=1)
stop_button.grid(row=0, column=2)

pygame.mixer.init()

root.mainloop()


