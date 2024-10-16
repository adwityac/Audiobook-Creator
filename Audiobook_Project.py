import tkinter as tk
from tkinter import *
import PyPDF2
import pyttsx3
from tkinter import filedialog, messagebox
import os

root = Tk()  # Creating GUI window
root.geometry('400x400')  # Geometry of window
root.title("Audiobook Creator")  # Title of window
root.config(bg='lightblue')

Label(root, text="Audiobook Creator", font="Arial 18", bg='lightblue').pack(pady=10)
m = tk.IntVar()
f = tk.IntVar()

pdfReader = None

def browse():
    global pdfReader
    file = filedialog.askopenfilename(title="Select a PDF", filetypes=(("PDF Files", "*.pdf"), ("All Files", "*.*")))
    if file:
        pdfReader = PyPDF2.PdfReader(open(file, 'rb'))
        pathlabel.config(text=os.path.basename(file))  # Show only the file name

def save():
    global speaker
    if not pdfReader:
        messagebox.showerror("Error", "Please select a PDF file first.")
        return

    speaker = pyttsx3.init()
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])

    if not output_file:
        return

    voices = speaker.getProperty('voices')
    if m.get() == 0:
        speaker.setProperty('voice', voices[0].id)
    elif f.get() == 1:
        speaker.setProperty('voice', voices[1].id)

    Label(root, text="Generating audio... Please wait.", bg='lightblue').pack(pady=10)

    try:
        for page in pdfReader.pages:
            text = page.extract_text() or ""  # Handle pages with no text
            speaker.save_to_file(text, output_file)
            speaker.runAndWait()

        Label(root, text="The Audio File is Saved!", bg='lightblue').pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

pathlabel = Label(root, text="No file selected", bg='lightblue')
pathlabel.pack(pady=10)

Button(root, text="Browse a File", command=browse).pack(pady=5)
Button(root, text="Create and Save the Audio File", command=save).pack(pady=5)

Checkbutton(root, text="Male Voice", onvalue=0, offvalue=10, variable=m, bg='lightblue').pack(pady=5)
Checkbutton(root, text="Female Voice", onvalue=1, offvalue=10, variable=f, bg='lightblue').pack(pady=5)

root.mainloop()
