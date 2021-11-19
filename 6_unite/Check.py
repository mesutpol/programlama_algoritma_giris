from tkinter import *
window = Tk()
window.title("Test")
window.geometry("431x252")
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(window, text = "Spor yapmayı severim", variable = CheckVar1, \
onvalue = 1, offvalue = 0, height=5, \
width = 20)
C2 = Checkbutton(window, text = "Müzik dinlemeyi severim", variable = CheckVar2, \
onvalue = 1, offvalue = 0, height=5, \
width = 20)
C3 = Checkbutton(window, text = "Çok konuşurum", variable = CheckVar3, \
onvalue = 1, offvalue = 0, height=5, \
width = 20)
C1.pack()
C2.pack()
C3.pack()
window.mainloop()
