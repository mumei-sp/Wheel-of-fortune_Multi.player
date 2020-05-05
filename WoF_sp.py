def clicked(alphabet):
    global amount
    amount = amounts[randint(0,(len(amounts) - 1))]
    txt="Spinning";
    label1.configure(text=txt)
    global p
    answer=s
    global n
    chance=amounts.index(amount)
    image_paths=['BankRupt.jpg','350.jpg','400.jpg','450.jpg','500.jpg','550.jpg','700.jpg','800.jpg','900.jpg','5000.jpg',"loose turn.jpg","free play.jpg"]
    img = Image.open(image_paths[chance])
    img = img.resize((300, 300), Image.ANTIALIAS)
    img= ImageTk.PhotoImage(img)
    panel = Label(window, image = img)
    panel.grid(column=35, row=20)
    if alphabet in el:
        image = Image.open("ini.jpg")
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        txt="Alphabet ["+alphabet+"] already entered";
        label1.configure(text=txt)
        p+=1
    elif amount=="BankRupt":
        image = Image.open("BankRupt.jpg")
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        globals()["p%s"%p]=0
        txt="BankRypt!!  u r UnFortunate";
        label1.configure(text=txt)
        xt="Player"+str(p)+"= $"+str(globals()["p%s"%p]);
        globals()["pp%s"%p].configure(text=xt,fg="white",bg="Black",font = "Helvetica 16 bold italic")
        p+=1
    elif amount=="loose turn":
        image = Image.open("loose turn.jpg")
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        p+=1
        txt="U lost ur Turn!!";
        label1.configure(text=txt)
    elif amount=="free play":
        image = Image.open("free play.jpg")
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        txt="Free play";
        label1.configure(text=txt)
        if alphabet in s:
            l=list(s)
            z=[x for x,y in enumerate(l) if y==alphabet]
            for i in z:
                globals()["b0%s" %i]["text"]=alphabet
        else:
            txt="Try again!!";
            label1.configure(text=txt)
            messagebox.showinfo("Not in Word!!!","Try again")
    elif alphabet in vowels:
        image = Image.open(image_paths[chance])
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        if globals()["p%s"%p] >= 250:
            globals()["p%s"%p]-=250
            g=s.count(alphabet)
            if g>1:
                l=list(s)
                z=[x for x,y in enumerate(l) if y==alphabet]
                for i in z:
                    globals()["b0%s" %i]["text"]=alphabet
                
            for i in range(len(answer)):
                if alphabet ==s[i]:
                    globals()["b0%s" %i]["text"]=alphabet
                    globals()["p%s"%p]+=amount*g
                    txt="u gOT  $"+str(amount*g);
                    label1.configure(text=txt,bg="white")
                    xt="Player"+str(p)+"= $"+str(globals()["p%s"%p]);
                    globals()["pp%s"%p].configure(text=xt,fg="white",bg="Black",font = "Helvetica 16 bold italic")
                    el.append(alphabet)
                    break
            else:
                p+=1
                txt="u lost chance of winning!!: $"+str(amount);
                label1.configure(text=txt)
                messagebox.showinfo("Not in Word!!!","Try again")
        else:
            p+=1
            txt='Not enough money';
            label1.configure(text=txt)
    else:
        g=s.count(alphabet)
        image = Image.open(image_paths[chance])
        image = image.resize((300, 300), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        if g>1:
                l=list(s)
                z=[x for x,y in enumerate(l) if y==alphabet]
                for i in z:
                    globals()["b0%s" %i]["text"]=alphabet
                
        for i in range(len(answer)):
            if alphabet ==s[i]:
                globals()["b0%s" %i]["text"]=alphabet
                globals()["p%s"%p]+=amount*g
                txt="u gOT  $"+str(amount*g);
                label1.configure(text=txt,bg="white")
                xt="Player"+str(p)+"= $"+str(globals()["p%s"%p]);
                globals()["pp%s"%p].configure(text=xt,fg="white",bg="Black",font = "Helvetica 16 bold italic")
                el.append(alphabet)
                break
        else:
            p+=1
            txt="u lost chance of winning!! : $"+str(amount);
            label1.configure(text=txt)
            messagebox.showinfo("Not in Word!!!","Try again!!")
    if p==(n+1):
        p=p-(n)
    if (all([globals()["b0%s" %j]["text"]==s[j] for j in range(len(s))])):
        messagebox.showinfo("congratulations player "+str(p), "U R Fortunate!!!!\n You have: $" + str(globals()["p%s"%p]))
        window.destroy()

def gg():
    x1 = entry1.get()
    if x1 ==s.lower():
        g1.configure(text="Congratulations  !! U Won The game",bg="black")
        messagebox.showinfo("congratulations Player "+str(p), "U R Fortunate!!!!\n You have: $" + str(globals()["p%s"%p]))
        window.destroy()
    else:
        g1.configure(text="Wrong...  keep Guessing!!",bg="black")
        messagebox.showinfo("Try Again!!!","Keep Guessing!!")

def getWord():
    with open("words.json", 'r') as f:
        word = json.loads(f.read())
        category = random.choice(list(word.keys()))
        word   = random.choice(word[category])
        return (category, word.upper())


print('Guess one letter at a time. If you want to buy a vowel, you must have at least $250, otherwise, you cannot buy a vowel.\nIf spin stops at "Bankrupt",the player losses all the money ')
print('If u kunow the word/phrase u can guess by typing in entry & pressing Guess')
print("Solve the puzzle!!\nHave Fun")
print("#Note : Spaces are replaced by '_'" )
import time
import string
import random
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import json
amounts = ["BankRupt",350,400,450,500,550,700,800,900,5000,"loose turn","free play",350,400,450,500,550,700]
category, s = getWord()
xx="Category: "+category
s=s.replace(" ","_")
vowels = ['A', 'E', 'I', 'O', 'U']
window = Tk()
window.title("WHEEL OF FORTUNE  #WOF...")
window.geometry("1960x720")
answer_arr=[]
for b in range(len(s)):
    globals()["b0%s" %b]=Button(window, text=" ",bg="white", fg="Black",width=2,height=1,font=('Helvetica','20'))
    globals()["b0%s" %b].grid(column=b+4, row=0)
l=list(s)
pun=string.punctuation
z=[x for x,y in enumerate(l) if y in pun]
for i in z:
    globals()["b0%s" %i]["text"]=l[i]
label3=Label(window,text=xx,font = "Helvetica 18 bold italic")
label3.grid(row=25,column=0)
img = Image.open('ini.jpg')
img = img.resize((300, 300), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(column=35, row=20)
el=[]
n=int(input("Enter the no of players: "))
p=1
for i in range(1,n+1):
    globals()["pp%s"%i]=Label(window,text="player"+str(i)+"= 0",fg = "red",font = "Times 16 italic")
    globals()["pp%s"%i].grid(row=0+i,column=0)
for j in range(1,n+1):
    globals()["p%s"%j]=0
entry1 = Entry (window)
entry1.grid(column=25, row=15)       
button=Button(text='Guess',bg="yellow", fg="Black",width=2,height=1,font=('Helvetica','12'), command=gg)
button.grid(row=13,column=25)
g1 = Label(window, text= "...",fg="white",font = "Helvetica 15 bold italic")
g1.grid(row=14,column=25)
#Buttons (Alphabets)    
a1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
a1.grid(column=4, row=1)
a2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
a2.grid(column=5, row=1)
a3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
a3.grid(column=6, row=1)
a4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
a4.grid(column=7, row=1)
a5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
a5.grid(column=8, row=1)
a6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
a6.grid(column=9, row=1)
a7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
a7.grid(column=10, row=1)
a8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
a8.grid(column=11, row=1)
a9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
a9.grid(column=12, row=1)
a10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
a10.grid(column=6, row=2)
a11= Button(window, text="K",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
a11.grid(column=7, row=2)
a12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
a12.grid(column=8, row=2)
a13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
a13.grid(column=9, row=2)
a14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
a14.grid(column=10, row=2)
a15= Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
a15.grid(column=4, row=3)
a16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
a16.grid(column=5, row=3)
a17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
a17.grid(column=6, row=3)
a18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
a18.grid(column=7, row=3)
a19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
a19.grid(column=8, row=3)
a20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
a20.grid(column=9, row=3)
a21= Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
a21.grid(column=10, row=3)
a22 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("V"))
a22.grid(column=11, row=3)
a23 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
a23.grid(column=12, row=3)
a24 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
a24.grid(column=7, row=5)
a25 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
a25.grid(column=8, row=5)
a26= Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
a26.grid(column=9, row=5)
label1=Label(window,text="Spinning...",fg = "red",font = "Times 16 italic")
label1.grid(row=20,column=0)
window.mainloop()

        
        
        