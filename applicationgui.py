from tkinter import *
from tkinter import filedialog
from os import system

class PythonApplication:
    def selectFile(self, event):
        fp1 = filedialog.askopenfilename(initialdir = '/home',
                                              title = 'Select file', 
                                          filetypes = (("java files" ,"*.java"),("all files", "*.*")))

        self.fileLocationLabel['text'] = str(fp1)

    def compileFile(self, event):
        temp = self.fileLocationLabel['text']        
        #system("find ." + )

    def executeFile(self, event):
        pass

    def __init__(self, master):
        frame = Frame(master)
        frame.place(x = 5,
                    y = 5)

        self.selectFileButton = Button(frame,
                         text = 'Select File',
                         fg = 'black')
        self.compileButton = Button(frame,
                      text = 'Compile',
                        fg = 'black')


        self.executeButton = Button(frame,
                      text = 'Execute',
                        fg = 'black')

        self.fileLocationLabel = Label(frame, 
                                       text = ' ', 
                                       borderwidth = .5, 
                                       relief = "sunken", 
                                       bg="white", 
                                       width = 30)

        #Binding
        self.compileButton.bind("<Button-1>", self.compileFile)
        self.executeButton.bind("<Button-1>", self.executeFile)
        self.selectFileButton.bind("<Button-1>", self.selectFile)

        #Packing
        self.fileLocationLabel.pack(side = TOP, anchor = W, fill = X, expand = YES)
        self.selectFileButton.pack(side = LEFT)
        self.compileButton.pack(side = LEFT)
        self.executeButton.pack(side = LEFT)

root = Tk()
root.geometry('250x60')
root.resizable(0,0)
root.title("Java Compiler and Executer")
classInstance = PythonApplication(root)
root.mainloop()
