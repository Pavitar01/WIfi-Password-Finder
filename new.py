from tkinter import *
from PIL import ImageTk, Image
import subprocess
class Wifi:

    def __init__(self, root):
        self.root = root
        self.root.title("Wifi Pass Finder | BY Pavitar Negi")
        self.root.geometry("1000x550+200+50")  ### 200 and 50 are x and y axizs from windo
        self.root.resizable(False, False)  ###SIZE CANT BERESIZE first false is width and second is height
        self.root.config(bg="white")

        title = Label(self.root, text="                  Wifi Password Finder", font=("Goudy Old Style", 40, "bold"), anchor='w',width=100,
                      bg="darkblue",
                      fg="white").pack()

        Details = Frame(self.root, bd=3, bg='white', relief=RIDGE)
        Details.place(x=50, y=100, width=500, height=380)

        emp_Title = Label(Details, text="DETAILS", font=("Goudy Old Style", 20), bg="darkblue", fg="white").place(x=0, y=0,relwidth=1,height=50)


        self.frame = Frame(Details,bg='#A8B9BF').place(x=0,y=50,width=500,height=380)


        self.text_box = Text(Details,height=23,width=60,  bg="darkblue", fg="green")
        self.text_box.grid(row=7,column=1)

        self.text_box.config(bg='#D9D8D7')

        sb = Scrollbar(Details,orient=VERTICAL)

        sb.grid(row=5, column=6, sticky=NS)

        self.text_box.config(yscrollcommand=sb.set)
        sb.config(command=self.text_box.yview)



        Frame1 = Frame(self.root, bd=3, bg='white', relief=RIDGE)
        Frame1.place(x=600, y=100, width='280', height='380')

        self.image = Image.open("linux-toy-cmatrix-animated.gif")

        self.resize_image = self.image.resize((280, 380))

        self.img = ImageTk.PhotoImage(self.resize_image)
        self.label1 = Label(Frame1,image=self.img, bg='white')
        self.label1.image = self.img
        self.label1.place(x=0, y=0, relwidth=1,relheight=1)

        GEN_BUTTON = Button(self.root, text="GENERATE", command=self.click, font=("times of roman", 20, 'bold'),
                            bg="white", fg="darkblue").place(x=100, y=450, width=180, height=30)
        CLEAR_BUTTON = Button(self.root, text="CLEAR", command=self.clear, font=("times of roman", 20, 'bold'),
                              bg="white", fg="darkblue").place(x=280, y=450, width=180, height=30)

    def click(self):

        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        for i in profiles:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                hello="{:<30}|  {:<}\n".format(i, results[0])
                #print(hello+"\n")
                self.text_box.insert('end', hello)

            except IndexError:
                print("{:<30}|  {:<}\n".format(i, " "))


    def clear(self):

        self.text_box.delete(1.0,'end')





root = Tk()
obj = Wifi(root)
root.mainloop()
