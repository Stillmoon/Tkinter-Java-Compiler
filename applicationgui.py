from tkinter import *
from tkinter import filedialog
from os import system

class PythonApplication:


    def selectFile(self, event):
        fp1 = filedialog.askopenfilename(initialdir = './',
                                              title = 'Select file', 
                                          filetypes = (("java files" ,"*.java"),("all files", "*.*")))
        
        self.fileLocationLabel['text'] = str(fp1)

    def compileFile(self, event):

        i = 0
        directoryList = []
        directoryList.append(None)

        for ch in self.fileLocationLabel['text']:
            if (directoryList[0] == None or
                directoryList[0] == ' ' or 
                directoryList[i] == None):
            
                directoryList[i] = ch
            else:
                if(ch == '/'):
                    directoryList.append(None)
                    i += 1
                else:
                    directoryList[i] = str(directoryList[i]) + str(ch)
     


        directoryList[0] = directoryList[0][1:]
        dire = ""
        file1 = ""
        for folder in directoryList:
            if ('.java' in folder):
                file1 = folder                
                break
            dire = dire + '/' + folder
        print(dire)   
        try:
            system("cd " + dire + "&& javac " + file1)
        except:
            print("t")

    def executeFile(self, event):
        
        i = 0
        directoryList = []
        directoryList.append(None)

        for ch in self.fileLocationLabel['text']:
            if (directoryList[0] == None or
                directoryList[0] == ' ' or 
                directoryList[i] == None):
            
                directoryList[i] = ch
            else:
                if(ch == '/'):
                    directoryList.append(None)
                    i += 1
                else:
                    directoryList[i] = str(directoryList[i]) + str(ch)
     


        directoryList[0] = directoryList[0][1:]
        filelist = []
        filelist.append(None)
        dire = ""
        file1 = ""
        for folder in directoryList:
            if ('.java' in folder):
                file1 = folder
                x = file1.split('.')
                print(x[0])
                file1 = x[0]
                break
            dire = dire + '/' + folder
        print(dire)   
        try:
            system("cd " + dire + "&& java " + file1)
        except:
            print("t")

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
