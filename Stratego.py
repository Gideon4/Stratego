from tkinter import *
import time

root=Tk()

board=[[["   ",0,0] for i in range(10)] for j in range(10)]
choosebtngrid=[[0 for i in range(10)] for j in range(10)]
btngrid=[[0 for i in range(10)] for j in range(10)]

colors=["Red","Blue"]
selcolor="#0090ff"

pieces=[["1",1],["2",8],["3",5],["4",4],["5",4],["6",4],["7",3],["8",2],["9",1],["10",1],["B",6],["F",1]]

lbl=Label(root,font="Arial 30",text=str(colors[0])+", set up your team")
lbl.grid(row=0,column=0)

choosebtnframe=Frame(root)
choosebtnframe.grid(row=1,column=0)

pickpieceframe=Frame(root)    
pickpieceframe.grid(row=2,column=0)

btnframe=Frame(root)
captframe=Frame(root)

listo=[]
listi=[]

r=6
c=0
turn=0
playing=True

def cheaty():
    global board
    board=[[['1', 1, 0], ['2', 1, 0], ['2', 1, 0], ['2', 1, 0], ['2', 1, 0], ['2', 1, 0], ['2', 1, 0], ['2', 1, 0], ['2', 1, 0], ['3', 1, 0]], [['3', 1, 0], ['3', 1, 0], ['3', 1, 0], ['3', 1, 0], ['4', 1, 0], ['4', 1, 0], ['4', 1, 0], ['4', 1, 0], ['5', 1, 0], ['5', 1, 0]], [['5', 1, 0], ['5', 1, 0], ['6', 1, 0], ['6', 1, 0], ['6', 1, 0], ['6', 1, 0], ['7', 1, 0], ['7', 1, 0], ['7', 1, 0], ['8', 1, 0]], [['8', 1, 0], ['9', 1, 0], ['10', 1, 0], ['B', 1, 0], ['B', 1, 0], ['B', 1, 0], ['B', 1, 0], ['B', 1, 0], ['B', 1, 0], ['F', 1, 0]], [['   ', 0, 0], ['   ', 0, 0], ['L', 3, 1], ['L', 3, 1], ['   ', 0, 0], ['   ', 0, 0], ['L', 3, 1], ['L', 3, 1], ['   ', 0, 0], ['   ', 0, 0]], [['   ', 0, 0], ['   ', 0, 0], ['L', 3, 1], ['L', 3, 1], ['   ', 0, 0], ['   ', 0, 0], ['L', 3, 1], ['L', 3, 1], ['   ', 0, 0], ['   ', 0, 0]], [['1', 2, 0], ['2', 2, 0], ['2', 2, 0], ['2', 2, 0], ['2', 2, 0], ['2', 2, 0], ['2', 2, 0], ['2', 2, 0], ['2', 2, 0], ['3', 2, 0]], [['3', 2, 0], ['3', 2, 0], ['3', 2, 0], ['3', 2, 0], ['4', 2, 0], ['4', 2, 0], ['4', 2, 0], ['4', 2, 0], ['5', 2, 0], ['5', 2, 0]], [['5', 2, 0], ['5', 2, 0], ['6', 2, 0], ['6', 2, 0], ['6', 2, 0], ['6', 2, 0], ['7', 2, 0], ['7', 2, 0], ['7', 2, 0], ['8', 2, 0]], [['8', 2, 0], ['9', 2, 0], ['10', 2, 0], ['B', 2, 0], ['B', 2, 0], ['B', 2, 0], ['B', 2, 0], ['B', 2, 0], ['B', 2, 0], ['F', 2, 0]]]
    buttn.grid(row=3,column=0)

def pick(event):
    global choosebtngrid,r,c,board,pieces


    #cheaty()

    
    if (turn==0 and event.widget.row>5) or (turn==1 and event.widget.row<4):
        if choosebtngrid[r][c]==choosebtngrid[event.widget.row][event.widget.col] and choosebtngrid[r][c]["text"]!=" ? ":
            pie=0
            for i in range(len(pieces)):
                if pieces[i][0]==choosebtngrid[r][c]["text"]:
                    pie=i
            pieces[pie][1]+=1
            choosebtngrid[r][c].config(text=" ? ")
            refresh()
        else:
            choosebtngrid[r][c].config(fg=colors[turn%2])
            r=event.widget.row
            c=event.widget.col
            choosebtngrid[r][c].config(fg=selcolor)
    
def chosepiece(event):
    global board,choosebtngrid,pieces,listo
    if choosebtngrid[r][c]["text"]!=" ? ":
        if choosebtngrid[r][c]["text"]=="F":
            pieces[9][1]+=1
        elif choosebtngrid[r][c]["text"]=="B":
            pieces[8][1]+=1
        else:
            pieces[int(choosebtngrid[r][c]["text"])-1][1]+=1
    choosebtngrid[r][c].config(text=pieces[event.widget.num][0])
    pieces[event.widget.num][1]-=1
    board[r][c][0]=pieces[event.widget.num][0]
    refresh()

def refresh():
    global listo    
    for item in listo:
        item.destroy()
    listo=[]            
    for i in range(len(pieces)):
        if pieces[i][1]>0:
            listo.append(Button(pickpieceframe,text=str(pieces[i][0])))
            listo[len(listo)-1].bind("<Button-1>",chosepiece)
            listo[len(listo)-1].grid(row=0,column=i)
            listo[len(listo)-1].num=i
            listo.append(Label(pickpieceframe,text=str(pieces[i][1])+" left"))
            listo[len(listo)-1].grid(row=1,column=i)
    buttn.grid_forget()
    if listo==[]:
        buttn.grid(row=3,column=0)

def donechoose():
    global choosebtngrid,turn,r,c,pieces
    buttn.grid_forget()
    if turn==0:
        for i in range(6,10):
            for j in range(10):
                choosebtngrid[i][j].config(text=" ? ",fg=colors[0])
        r=0
        c=0
        lbl.config(text=colors[1]+", pick your team")
        pieces=[["1",1],["2",8],["3",5],["4",4],["5",4],["6",4],["7",3],["8",2],["9",1],["10",1],["B",6],["F",1]]
        turn=1
        refresh()
    else:
        choosebtnframe.grid_forget()
        pickpieceframe.grid_forget()
        for i in range(10):
            for j in range(10):                
                btngrid[i][j]=Button(btnframe)
                btngrid[i][j].bind("<Button-1>",select)
                btngrid[i][j].grid(row=i,column=j)
                btngrid[i][j].row=i
                btngrid[i][j].col=j
        if i<4:
            choosebtngrid[i][j].config(fg=colors[1])
        if i>5:
            choosebtngrid[i][j].config(fg=colors[0])
        btnframe.grid(row=1,column=0)
        captframe.grid(row=2,column=0)
        eachturn()

def select(event):
    global r,c,btngrid
    if btngrid[event.widget.row][event.widget.col]["fg"]==selcolor:
        btngrid[event.widget.row][event.widget.col].config(fg=colors[turn%2])
    elif (board[event.widget.row][event.widget.col][1]==2-turn%2) and not(board[event.widget.row][event.widget.col][0]=="B" or board[event.widget.row][event.widget.col][0]=="F"):
        btngrid[r][c].config(fg=colors[board[r][c][1]%2])
        r=event.widget.row
        c=event.widget.col
        btngrid[r][c].config(fg=selcolor)
    elif btngrid[r][c]["fg"]==selcolor:
        move(r,c,event.widget.row,event.widget.col)

def eachturn():
    global btngrid,turn,r,c,listi
    r=(1-turn%2)*9
    c=0
    turn+=1
    lbl.config(text=colors[turn%2]+", make your move")
    for i in range(10):
        for j in range(10):
            btngrid[i][j].config(text=board[i][j][0])
            if (board[i][j][1]==1+turn%2) and board[i][j][2]==0:
                btngrid[i][j].config(text="?")
            if board[i][j][1]==1:
                btngrid[i][j].config(fg=colors[1])
            if board[i][j][1]==2:
                btngrid[i][j].config(fg=colors[0])
    for i in range(len(pieces)-1):
        count=0
        for row in board:
            for item in row:
                if item[0]==pieces[i][0] and item[1]==1+turn%2:
                    count+=1
        listi[i].config(text="There are "+str(count)+" "+pieces[i][0]+"s left")

def move(r1,c1,r2,c2):
    global board,btngrid
    if board[r2][c2][1]==0 or board[r2][c2][1]==1+turn%2:
        bool=True
        if (r1-r2)==0^(c1-c2)==0 and board[r1][c1][0]=="2":
            if r1==r2:
                for i in range(min([c1,c2])+1,max([c1,c2])):
                    if board[r1][i][0]!="   ":
                        bool=False
            else:
                for i in range(min([r1,r2])+1,max([r1,r2])):
                    if board[i][c1][0]!="   ":
                        bool=False
        elif not ((abs(r1-r2)>0)^(abs(c1-c2)>0)) and abs(r1-r2)<2 and abs(c1-c2)<2:
          bool=False
        if bool:
            if board[r2][c2][1]==1+turn%2:
                board[r2][c2]=attack(r1,c1,r2,c2)
                board[r2][c2][2]=1
            else:
                board[r2][c2]=board[r1][c1].copy()
            board[r1][c1]=["   ",0,0]
            btngrid[r1][c1].config(fg="#000000")
            if playing:
                eachturn()

def attack(r1,c1,r2,c2):
    p1=board[r1][c1][0]
    p2=board[r2][c2][0]
    if p1=="1" and p2=="10":
        return board[r1][c1]
    elif p1=="3" and p2=="B":
        return board[r1][c1]
    elif p2=="F":
        win()
        return board[r2][c2]
    elif p2=="B":
        return board[r2][c2]
    elif p1==p2:
        return ["   ",0,0]
    elif int(p1)>int(p2):
        return board[r1][c1]
    else:
        return board[r2][c2]

def win():
    global board,btngrid,playing
    for i in range(10):
        for j in range(10):
            btngrid[i][j].config(text=board[i][j][0])
            if board[i][j][1]==1:
                btngrid[i][j].config(fg=colors[1])
            if board[i][j][1]==2:
                btngrid[i][j].config(fg=colors[0])
    lbl.config(text=colors[turn%2]+" wins")
    captframe.destroy()
    playing=False
                
for i in range(10):
    for j in range(10):
        choosebtngrid[i][j]=Button(choosebtnframe,text=" ? ")
        choosebtngrid[i][j].bind("<Button-1>",pick)
        choosebtngrid[i][j].grid(row=i,column=j)
        choosebtngrid[i][j].row=i
        choosebtngrid[i][j].col=j
        if i<4:
            choosebtngrid[i][j].config(fg=colors[1])
            board[i][j][1]=1
        elif i>5:
            choosebtngrid[i][j].config(fg=colors[0])
            board[i][j][1]=2
        elif (j>1 and j<4) or (j>5 and j<8):
            choosebtngrid[i][j].config(text=" L ")
            board[i][j]=["L",3,1]
        else:
            choosebtngrid[i][j].config(text="   ")

for i in range(len(pieces)):
    if i!=len(pieces)-1:
        listi.append(Label(captframe))
        listi[i].grid(row=int(i/3),column=i%3)
    if pieces[i][1]>0:
        listo.append(Button(pickpieceframe,text=str(pieces[i][0])))
        listo[len(listo)-1].bind("<Button-1>",chosepiece)
        listo[len(listo)-1].grid(row=0,column=i)
        listo[len(listo)-1].num=i
        listo.append(Label(pickpieceframe,text=str(pieces[i][1])+" left"))
        listo[len(listo)-1].grid(row=1,column=i)

buttn=Button(root,text="Done",font="Arial 30",command=donechoose)

root.mainloop()
