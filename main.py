import os
import PyPDF2 #A Pure-Python library built as a PDF toolkit
from gtts import gTTS #Google Text to speech
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filelocation = askopenfilename()
with open(filelocation,"rb") as f:
    pdf = PyPDF2.PdfFileReader(f)
    mytext = ""
    for pageNum in range(pdf.numPages):
        pageObj = pdf.getPage(pageNum)
        mytext += pageObj.extractText()
print(mytext)

final_output = gTTS(text=mytext, lang="en")
print("Generating Speech.........")
final_output.save("Generated_speech.mp3")
os.system("Start Generated_speech.mp3")
print("Successfully Generated")

