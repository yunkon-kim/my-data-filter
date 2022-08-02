import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pandas as pd  


def main():    
    # create the root window
    root = tk.Tk()
    root.title('Tkinter Open File Dialog')
    root.resizable(False, False)
    root.geometry('300x150')
    root.withdraw() # Hides small tkinter window.

    # open button
    # open_button = ttk.Button(
    #     root,
    #     text='Open a File',
    #     command=select_file
    # )

    # open_button.pack(expand=True)

    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

    filetypes = (
        ("xlxs files", ".*xlsx"),
        ('text files', '*.txt'),
        ('All files', '*.*')
    )


    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='./',
        filetypes=filetypes)

    print("Selected filename:", filename)

    # Read the file  
    df = pd.read_excel(filename, index_col=None, header=1) 

    print(df) 
    
    # Output the number of rows  
    print("Total rows: {0}".format(len(df)))  
    
    # See which headers are available  
    headers = list(df)
    print(headers)  
    
    # Drop uniques
    df = df[df.duplicated(subset=[headers[0]], keep=False)]
    print(df)

    # Drop duplicated
    df = df.drop_duplicates(subset=[headers[1]], keep=False)
    print(df)

    # run the application
    # root.mainloop()


if __name__ == "__main__":
	main()
