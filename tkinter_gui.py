import tkinter as tk
from _tkinter import *

root = tk.Tk() 

root.title('Counting Seconds') 

#backround red:-
tk.Canvas(root,bg="green",width=500,height=500).pack() 
tk.Label(root,text="hellow rio si r",font=("times",55)).pack()

#message:=
tk.Message( root, text="Hey!? How are you doing?" ).pack()

#button :=
tk.Button(root, text ="Hello thsi is button ", bg="yellow").pack()

#label and entry box :=
tk.Label(root,text="enter usernsme ").pack(side="left")
tk.Entry(root,).pack(side="left")


# cheakbox :=
tk.Checkbutton(root, text = "Music",   height=5, width = 20).pack()
tk.Checkbutton(root, text = "Video",   height=5, width = 20).pack()


#readio button :=
tk.Radiobutton(root, text="Option 1",value=1,).pack()
tk.Radiobutton(root, text="Option 1",value=2,).pack()
tk.Radiobutton(root, text="Option 1",value=3,).pack()
tk.Radiobutton(root, text="Option 1",value=4,).pack()


# scale := 
tk.Scale( root, ).pack(anchor="center")

root.mainloop()



