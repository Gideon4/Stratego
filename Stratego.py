import time

board = []
bboard = []
rboard = []
zeroro1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
zeroro2 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
middle1 = [[0,0,0,0],[0,0,0,0],["Lake",0,3,0],["Lake",0,3,0],[0,0,0,0],[0,0,0,0],["Lake",0,3,0],["Lake",0,3,0],[0,0,0,0],[0,0,0,0]]
middle2 = [[0,0,0,0],[0,0,0,0],["Lake",0,3,0],["Lake",0,3,0],[0,0,0,0],[0,0,0,0],["Lake",0,3,0],["Lake",0,3,0],[0,0,0,0],[0,0,0,0]]
winner = 0
askvar = ""

def ask(text,input1,input2):
    global askvar
    askvar = input(text)
    if askvar != input1 and askvar != input2:
        print("You can't do that silly!")
        ask(text,input1,input2)

def goaway(team):
    print(team+", go away!")
    time.sleep(5)
    for i in range(108):
        print(" ")

def setteams(num):
    global board,rownum

    yourteam = []
    if rownum == "3":
        pieces = [[1,1],[2,5],[3,4],[4,2],[5,2],[6,3],[7,3],[8,2],[9,1],[10,1],["Flag",1],["Bomb",5]]
    else:
        pieces = [[1,1],[2,8],[3,5],[4,4],[5,4],[6,4],[7,3],[8,2],[9,1],[10,1],["Flag",1],["Bomb",6]]

    if num == 1:
        print("Red, pick your team.")
    else:
        print("Blue, pick you team.")
    for k in range(int(rownum)):
        trow = []
        clmn = 1
        while(len(trow) != 10):
            print("What would you like to be in row #"+str(k + 1)+" column #"+str(clmn)+"?")
            words = ""
            for l in range(12):
                if pieces[l][1] != 0:
                    words = words+", "+str(pieces[l][0])+"s: "+str(pieces[l][1])
            print("Pieces left"+words)
            curaddpie = input()
            whiind = 0
            found = False
            while (found == False) and (whiind < 12):
                if curaddpie ==  str(pieces[whiind][0]) and pieces[whiind][1] > 0:
                    trow.append([pieces[whiind][0],num,num,num])
                    clmn += 1
                    pieces[whiind][1] -= 1
                    found = True
                whiind += 1
            if found == False:
                print("You can't do you that, silly!")
        board.append(trow)
        yourteam.append(trow)
    for m in range(4):
        tsyt = ""
        for n in range(10):
            if yourteam[m][n][0] == "Bomb" or yourteam[m][n][0] == "Flag":
                tsyt = tsyt+yourteam[m][n][0]+" "
            elif yourteam[m][n][0] == 10:
                tsyt = tsyt+"  10 "
            else:
                tsyt = tsyt+"  "+str(yourteam[m][n][0])+"  "
        print(tsyt)
    if input("Do you approve of you team?") == "no":
        setteams()

def setboard(excludednum,excludedcolor,yourcolor):
    global board
    
    for i in range(10):
        text = ""
        ycolor = ""
        for j in range(10):
            if board[i][j][1] == excludednum:
                ycolor = excludedcolor
            else:
                ycolor = yourcolor
            if board[i][j][1] == excludednum and board[i][j][3] != 0:
                text = text+"  "+excludedcolor+"?  "
            elif board[i][j][0] == "Bomb" or board[i][j][0] == "Flag":
                text = text+ycolor+board[i][j][0]+" "
            elif  board[i][j][0] == "Lake":
                text = text+" Lake "
            elif board[i][j][0] == 0:
                text = text+"      "
            elif board[i][j][0] == 10:
                text = text+"  "+ycolor+"10 "
            else:
                text = text+"  "+ycolor+str(board[i][j][0])+"  "
        print(text)

def move(teamnum):
    global board
    
    cft = 0
    cft2 = 0
    cft3 = 0
    cft4 = 0
    
    tloc = input("Pick a piece.")
    if tloc[len(tloc)-1] == "0":
        cft = 9
    else:
        cft = int(tloc[len(tloc)-1])-1
    if tloc[0] == "1" and tloc[1] == "0":
        cft2 = 9
    else:
        cft2 = int(tloc[0])-1
    if board[cft][cft2][1] == teamnum and board[cft][cft2][0] != "Bomb" and board[cft][cft2][0] != "Flag":
        tmloc = input("Where would you like to move it?")
        if tmloc[len(tmloc)-1] == "0":
            cft3 = 9
        else:
            cft3 = int(tmloc[len(tloc)-1])-1
        if tloc[0] == "1" and tloc[1] == "0":
            cft4 = 9
        else:
            cft4 = int(tmloc[0])-1
        if board[cft3][cft4][2] != teamnum and board[cft3][cft4][2] != 3:
            if ((abs(cft-cft3) == 1) ^ (abs(cft2-cft4) == 1)) or twomove(cft,cft2,cft3,cft4):
                if board[cft3][cft4][2] == 0:
                    board[cft3][cft4] = board[cft][cft2]
                else:
                    board[cft3][cft4] = attack(board[cft][cft2][0],board[cft3][cft4][0],teamnum)
                board[cft][cft2] = [0,0,0,0]
            else:
                print("You can't do that silly!")
                move(teamnum)
        else:
            print("You can't do that silly!")
            move(teamnum)
    else:
        print("You can't do that silly!")
        move(teamnum)

def attack(attacker,attackee,attackerteam):
    global bombxplo
    if attackerteam == 1:
        otherteam = 2
    else:
        otherteam = 1
    if attackee == "Flag":
        win(attackerteam)
    elif (attacker == 1) and (attackee == 10):
        num = 1
        team = attackerteam
    elif (attacker == 3) and (attackee == "Bomb"):
        num = 3
        team = attackerteam
    elif (attackee == "Bomb") or (attacker == attackee):
        if bombxplo == "y":
            num = 0
            team = 0
        else:
            num = "Bomb"
            team = otherteam
    elif attacker > attackee:
        num = attacker
        team = attackerteam
    else:
        num = attackee
        team = otherteam
    return[num,team,team,0]

def win(winteam):
    global winner
    winner = winteam
    if winteam == 1:
        print("Red Wins!")
    else:
        print("Blue Wins!")

def twomove(y1,x1,y2,x2):
    global board
    if board[y1][x1][0] == 2 and (y1 == y2 or x1 == x2):
        tttruth = True
        if y1 == y2:
            if x1 > x2:
                for i in range(y1 - y2 - 1):
                    if board[y2 + i + 1][x1][2] != 0:
                        tttruth = False
            else:
                for i in range(y2 - y1 - 1):
                    if board[y1 + i + 1][x1][2] != 0:
                        tttruth = False
        else:
            if y1 > y2:
                for i in range(x1 - x2 - 1):
                    if board[y1][x2 + i + 1][2] != 0:
                        tttruth = False
            else:
                for i in range(x2 - x1 - 1):
                    if board[y1][x1 + i + 1][2] != 0:
                        tttruth = False
        return(tttruth)
    
ask("How many rows? 3 or 4","3","4")
rownum = askvar
ask("Do you want bombs to explode? y or n","y","n")
bombxplo = askvar
goaway("Blue")
setteams(1)
if rownum == "3":
    board.append(zeroro1)
    board.append(middle1)
    board.append(middle2)
    board.append(zeroro2)
else:
    board.append(middle1)
    board.append(middle2)
goaway("Red")
setteams(2)
while winner == 0:
    goaway("Blue")
    setboard(2,"B","R")
    move(1)
    if winner == 0:
        goaway("Red")
        setboard(1,"R","B")
        move(2)
