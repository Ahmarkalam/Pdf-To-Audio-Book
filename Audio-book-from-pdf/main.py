import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

book = askopenfilename()
reader = PdfReader(book)
pages = len(reader.pages)

for num in range(0, pages):
    page = reader.pages[num]
    text = page.extract_text()
    player = pyttsx3.init()
    player.say(text)

    player.runAndWait()
    


