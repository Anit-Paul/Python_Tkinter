import tkinter as tk

root = tk.Tk()
root.title('first programme')
root.minsize(width=500,height=30)

my_label=tk.Label(text="i am a label")
my_label.pack()  #for any component added to the window we need to use it
#my_label.pack(side='left')
root.mainloop()