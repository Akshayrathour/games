from tkinter import *

def checkwin():
    global decide
    if decide:
        if(blocks[0]!=0 and blocks[0]==blocks[1] and blocks[0]==blocks[2]):
            bton0.configure(bg="red")
            bton1.configure(bg="red")
            bton2.configure(bg="red")
            # root.configure(bg="green")
            decide=0
        elif(blocks[0]!=0 and blocks[0]==blocks[2] and blocks[0]==blocks[6]):
            bton0.configure(bg="red")
            bton2.configure(bg="red")
            bton6.configure(bg="red")
            # root.configure(bg="green")
            decide=0
        elif(blocks[0]!=0 and blocks[0]==blocks[4] and blocks[0]==blocks[8]):
            bton0.configure(bg="red")
            bton4.configure(bg="red")
            bton8.configure(bg="red")
            # root.configure(bg="green")
            decide=0
        elif(blocks[1]!=0 and blocks[1]==blocks[4] and blocks[1]==blocks[7]):
            bton1.configure(bg="red")
            bton4.configure(bg="red")
            bton7.configure(bg="red")
            # root.configure(bg="green")
            decide=0
        elif(blocks[2]!=0 and blocks[2]==blocks[5] and blocks[2]==blocks[8]):
            bton2.configure(bg="red")
            bton5.configure(bg="red")
            bton8.configure(bg="red")
            # root.configure(bg="green")
            decide=0
        elif(blocks[2]!=0 and blocks[2]==blocks[4] and blocks[2]==blocks[6]):
            bton2.configure(bg="red")
            bton4.configure(bg="red")
            bton6.configure(bg="red")
            # root.configure(bg="green")
            decide=0
        elif(blocks[3]!=0 and blocks[3]==blocks[4] and blocks[3]==blocks[5]):
            bton3.configure(bg="red")
            bton4.configure(bg="red")
            bton5.configure(bg="red")
            # root.configure(bg="green")
            decide=0
        elif(blocks[6]!=0 and blocks[6]==blocks[7] and blocks[6]==blocks[8]):
            bton6.configure(bg="red")
            bton7.configure(bg="red")
            bton8.configure(bg="red")
            # root.configure(bg="green")
            decide=0
    else:
        pass

def click(j,bt):
    global counter
    if blocks[j]!=0:
        pass
    else:
        if(counter%2==0):
            blocks[j]='X'
            bt.configure(text="X")
            counter+=1
        else:
            blocks[j]='O'
            bt.configure(text="O")
            counter+=1
    checkwin()

def Reset():
    global blocks,decide
    decide=1
    blocks=[0,0,0,0,0,0,0,0,0]
    bton0.configure(text="",bg="#f0f0f0")
    bton1.configure(text="",bg="#f0f0f0")
    bton2.configure(text="",bg="#f0f0f0")
    bton3.configure(text="",bg="#f0f0f0")
    bton4.configure(text="",bg="#f0f0f0")
    bton5.configure(text="",bg="#f0f0f0")
    bton6.configure(text="",bg="#f0f0f0")
    bton7.configure(text="",bg="#f0f0f0")
    bton8.configure(text="",bg="#f0f0f0")

decide=1
blocks=[0,0,0,0,0,0,0,0,0]
counter=1
root=Tk()
root.geometry("325x380")
root.title("Tic-Tac-Toe")
root.configure(bg="black")
root.minsize("325","356")
root.maxsize("325","380")
bton0=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(0,bton0))
bton0.place(x=0,y=0)
bton1=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(1,bton1))
bton1.place(x=110,y=0)
bton2=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(2,bton2))
bton2.place(x=220,y=0)
bton3=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(3,bton3))
bton3.place(x=0,y=120)
bton4=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(4,bton4))
bton4.place(x=110,y=120)
bton5=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(5,bton5))
bton5.place(x=220,y=120)
bton6=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(6,bton6))
bton6.place(x=0,y=240)
bton7=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(7,bton7))
bton7.place(x=110,y=240)
bton8=Button(root,text="",font="Georgia 20",height=3,width=6,command= lambda:click(8,bton8))
bton8.place(x=220,y=240)
rebton=Button(root,text="Restart",font="georgia 10",command=Reset)
rebton.place(x=140,y=356)
root.mainloop()
