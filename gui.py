import tkinter as tk
from tkinter.ttk import Frame, Button, Label, Style
from tkinter import BOTH, W, N, E, S
import constants
from return_definition import parseAndReturn

class dictWindow(Frame):
    def __init__(self):
        super(dictWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()

        self.lbl_enter = tk.Label(self, text="Enter a word to look up")
        self.lbl_enter.grid(row=0, column = 0)

        self.entry_field = tk.Entry(self)
        self.entry_field.grid(row=1, column=0)

        button_lookup = Button(self, text="Look up word", command = self.lookup)
        button_lookup.grid(row=1, column = 1)

        button_clip = Button(self, text="Copy to clipboard", command = self.copyToClip)
        button_clip.grid(row=1, column = 2)

        button_quickCopy = Button(self, text="Lookup and Copy", command = self.lookAndCopy)
        button_quickCopy.grid(row = 2, column = 1)

        
        self.area = tk.Text(self)
        self.area.grid(row=8, column=0, columnspan=2, rowspan=4)#, sticky=E+W+S+N)
     #   self.area["state"] = 'disabled'


    def lookup(self):
        word = self.entry_field.get()
        if not word == "":
            try:
                defDict = parseAndReturn(word)
                stringToCopy = word + "\n" + self.processDict(defDict)
                self.area.delete('1.0', 'end')
                self.area.insert('1.0', stringToCopy)
            except AttributeError as err:
                print(err)

    def copyToClip(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.area.get('1.0', 'end'))
        self.master.update()

    def lookAndCopy(self):
        self.lookup()
        self.copyToClip()

    def centerWindow(self):
        width = constants.WIDTH
        height = constants.HEIGHT

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = (sw - width)/2
        y = (sh - height)/2
        self.master.geometry('%dx%d+%d+%d' % (width, height, x, y))

    def processDict(self, dictionary):
        outString = ""
        for definition in range(len(dictionary)):
            for subdef in range(len(dictionary[definition])):
                if subdef == 0:
                    outString += "(" + dictionary[definition][subdef] + "):\n"
                else:
                    outString += "- " + dictionary[definition][subdef] + "\n"

        return outString 

def main():
    window = tk.Tk("QuickDict V0.0")
    window.title("QuickDict V0.0")
    dictLooker = dictWindow()
    window.mainloop()

if __name__ == "__main__":
    main()

print("DONE")

