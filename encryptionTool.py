from tkinter import *
from tkinter import ttk
import random
import string

#Characters that the text will be encrypted into saved as a key
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

#function to randomize key
def randomize_key():
    random.shuffle(key)

def save_key():
    file = open('savedKey.txt', 'w')
    str = ''.join(key)
    file.write(str)

def load_key():
    global key
    file = open('savedKey.txt', 'r')
    str = file.read()
    key = list(str)

#Randomize key so it isn't always the same on startup
randomize_key()

#instantiate instance of a window
window = Tk()

### Configure Window ###
window.title("SandCaByte's Simple Encryption")

#Setup notebook widget
notebook = ttk.Notebook(window) #Widget that manages a collection of displays

#Add the tabs to the notebook widget
encryptTab = Frame(notebook) # new frame for tab
decryptTab = Frame(notebook) # new frame for tab

notebook.add(encryptTab, text="Encryption")
notebook.add(decryptTab, text="Decryption")
notebook.pack(side=LEFT)

#Frames with same size for consistency
encryptFrame = Frame(encryptTab, width=256, height=256)
decryptFrame = Frame(decryptTab, width=256, height=256)
encryptFrame.pack()
decryptFrame.pack()

#Encryption functions
def encrypt_text():
    plain_text = eEntry.get()
    cipher_text = ""

    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]

    eResultEntry.delete(0, END)
    eResultEntry.insert(0, cipher_text)

## Encryption Frame Widgets ##
eRandKeyButton = Button(encryptFrame, text="Randomize Key", command=randomize_key)
eSaveKeyButton = Button(encryptFrame, text="Save Key", command=save_key)
eLoadKeyButton = Button(encryptFrame, text="Load Key", command=load_key)
eLabel = Label(encryptFrame, text="Text to encrypt:", pady=5)
eEntry = Entry(encryptFrame)
eButton = Button(encryptFrame, text="Encrypt", command=encrypt_text, pady=5)
eResultHeaderLabel = Label(encryptFrame, text="Result:", pady=5)
eResultEntry = Entry(encryptFrame)

eRandKeyButton.grid(row=0, column=0)
eSaveKeyButton.grid(row=0, column=1)
eLoadKeyButton.grid(row=0, column=2)
eLabel.grid(row=1, column=0)
eEntry.grid(row=1, column=1)
eButton.grid(row=1, column=2)
eResultHeaderLabel.grid(row=2, column=0)
eResultEntry.grid(row=2, column=1)

#Encryption functions
def decrypt_text():
    cipher_text = dEntry.get()
    plain_text = ""

    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]

    dResultEntry.delete(0, END)
    dResultEntry.insert(0, plain_text)

## Decryption Frame Widgets ##
dRandKeyButton = Button(decryptFrame, text="Randomize Key", command=randomize_key)
dSaveKeyButton = Button(decryptFrame, text="Save Key", command=save_key)
dLoadKeyButton = Button(decryptFrame, text="Load Key", command=load_key)
dLabel = Label(decryptFrame, text="Text to decrypt:", pady=5)
dEntry = Entry(decryptFrame)
dButton = Button(decryptFrame, text="decrypt", command=decrypt_text, pady=5)
dResultHeaderLabel = Label(decryptFrame, text="Result:", pady=5)
dResultEntry = Entry(decryptFrame)

dRandKeyButton.grid(row=0, column=0)
dSaveKeyButton.grid(row=0, column=1)
dLoadKeyButton.grid(row=0, column=2)
dLabel.grid(row=1, column=0)
dEntry.grid(row=1, column=1)
dButton.grid(row=1, column=2)
dResultHeaderLabel.grid(row=2, column=0)
dResultEntry.grid(row=2, column=1)

window.mainloop() #place window on computer screen, listen for events