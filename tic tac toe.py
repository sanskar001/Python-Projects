import random
print("                            TIC TAC TOE")
print("                           *************")
block={"tl":"","tm":"","tr":"","ml":"","mm":"","mr":"","dl":"","dm":"","dr":""}  # dictionary for tic tac toe board
print("                        "+ "[tl]"+" " + "|"+" " + "[tm]"+" "+"|"+" "+"[tr]"+" ")
print("                       "+ "      " + "|" + "      " + "|" + "      ")
print("                        "+"__________________")
print("                        "+ "[ml]"+" " + "|"+" " + "[mm]"+" "+"|"+" "+"[mr]"+" ")
print("                       "+ "      " + "|" + "      " + "|" + "      ")
print("                        "+"__________________")
print("                        "+ "[dl]"+" " + "|"+" " + "[dm]"+" "+"|"+" "+"[dr]"+" ")
print("                       " + "      " + "|" + "      " + "|" + "      ")
ply1_name=input("Enter the name of player 1:")         # taking name of players
ply2_name=input("Enter the name of player 2:")

print("                       LETS DO TOSS FOR MATCH")
print("# SELECT THE NUMBER TYPE FOR TOSS(ODD/EVEN)")   # toss for match
ply1_toss=""
ply2_toss=""      
toss=random.randint(0,2)
if toss==0:
    ply1_toss=input("Enter your choice:")        # random player choice for toss
    if ply1_toss=="even":
        ply2_toss="odd"
    else :
        ply2_toss="even"
else:
    ply2_toss=input("Enter your choice:")
    if ply2_toss=="even":
        ply1_toss="odd"
    else :
        ply1_toss="even"
toss_winner=""                         # toss_winner
toss_no=random.randint(1,11)
if toss_no%2==0:
    if ply1_toss=="even":
        print("* player 1 win the toss")
        toss_winner="player1"
    else:
        print("* player 2 win the toss")
        toss_winner="player2"
else:
    if ply1_toss=="odd":
        print("* player 1 win the toss")
        toss_winner="player1"
    else:
        print("* player 2 win the toss")
        toss_winner="player2"

ply1_symbol=input("Player_1 select the symbol O/X:")    # ply1_symbol(O/X)
ply2_symbol=input("PLayer_2 select the symbol O/X:")    # ply2_symbol(O/X)
symbol=""
turn=""

x=0
for x in range(9):
    if toss_winner=="player1":
        if x%2==0:
            symbol=ply1_symbol
            turn=input("Enter the turn:")
            block[turn]=symbol
            print("                        "+ "  " + block["tl"]+"  " + "|"+"  " + block["tm"]+"   "+"|"+"  "+block["tr"]+"  ")
            print("                        " + "     " + "|" + "     " + "|" + "     ")
            print("                        "+"_________________")
            print("                        "+"  "+ block["ml"]+"   " + "|"+"  " + block["mm"]+"    "+"|"+"  "+block["mr"]+"  ")
            print("                        " + "     " + "|" + "     " + "|" + "     ")
            print("                        "+"_________________")
            print("                        "+"  "+ block["dl"]+"   " + "|"+"  " + block["dm"]+"    "+"|"+"  "+block["dr"]+"  ")
            print("                        " + "     " + "|" + "     " + "|" + "     ")
            if block["tl"]==symbol and block["tm"]==symbol and block["tr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            elif block["ml"]==symbol and block["mm"]==symbol and block["mr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            elif block["dl"]==symbol and block["dm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            elif block["tl"]==symbol and block["ml"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            elif block["tm"]==symbol and block["mm"]==symbol and block["dm"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            elif block["tr"]==symbol and block["mr"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            elif block["tl"]==symbol and block["mm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            elif block["tr"]==symbol and block["mm"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
            
                  
        else:
           symbol=ply2_symbol
           turn=input("Enter the turn:")
           block[turn]=symbol
           print("                        "+ "  " + block["tl"]+"  " + "|"+"  " + block["tm"]+"   "+"|"+"  "+block["tr"]+"  ")
           print("                        " + "     " + "|" + "     " + "|" + "     ")
           print("                        "+"_________________")
           print("                        "+"  "+ block["ml"]+"   " + "|"+"  " + block["mm"]+"    "+"|"+"  "+block["mr"]+"  ")
           print("                        " + "     " + "|" + "     " + "|" + "     ")
           print("                        "+"_________________")
           print("                        "+"  "+ block["dl"]+"   " + "|"+"  " + block["dm"]+"    "+"|"+"  "+block["dr"]+"  ")
           print("                        " + "     " + "|" + "     " + "|" + "     ")
           if block["tl"]==symbol and block["tm"]==symbol and block["tr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
           elif block["ml"]==symbol and block["mm"]==symbol and block["mr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
           elif block["dl"]==symbol and block["dm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
           elif block["tl"]==symbol and block["ml"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 2 IS WINNER *") 
                  break
           elif block["tm"]==symbol and block["mm"]==symbol and block["dm"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
           elif block["tr"]==symbol and block["mr"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
           elif block["tl"]==symbol and block["mm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
           elif block["tr"]==symbol and block["mm"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")  
                  break
    else:
        if x%2==0:
            symbol=ply2_symbol
            turn=input("Enter the turn:")
            block[turn]=symbol
            print("                        "+ "  " + block["tl"]+"  " + "|"+"  " + block["tm"]+"   "+"|"+"  "+block["tr"]+"  ")
            print("                        " + "     " + "|" + "     " + "|" + "     ")
            print("                        "+"_________________")
            print("                        "+"  "+ block["ml"]+"   " + "|"+"  " + block["mm"]+"    "+"|"+"  "+block["mr"]+"  ")
            print("                        " + "     " + "|" + "     " + "|" + "     ")
            print("                        "+"_________________")
            print("                        "+"  "+ block["dl"]+"   " + "|"+"  " + block["dm"]+"    "+"|"+"  "+block["dr"]+"  ")
            print("                        " + "     " + "|" + "     " + "|" + "     ")
            if block["tl"]==symbol and block["tm"]==symbol and block["tr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
            elif block["ml"]==symbol and block["mm"]==symbol and block["mr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
            elif block["dl"]==symbol and block["dm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
            elif block["tl"]==symbol and block["ml"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")   
                  break
            elif block["tm"]==symbol and block["mm"]==symbol and block["dm"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
            elif block["tr"]==symbol and block["mr"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *")
                  break
            elif block["tl"]==symbol and block["mm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 2 IS WINNER *") 
                  break
            elif block["tr"]==symbol and block["mm"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 2 IS WINNER *") 
                  break
        else:
             symbol=ply1_symbol
             turn=input("Enter the turn:")
             block[turn]=symbol
             print("                        "+ "  " + block["tl"]+"  " + "|"+"  " + block["tm"]+"   "+"|"+"  "+block["tr"]+"  ")
             print("                        " + "     " + "|" + "     " + "|" + "     ")
             print("                        "+"_________________")
             print("                        "+"  "+ block["ml"]+"   " + "|"+"  " + block["mm"]+"    "+"|"+"  "+block["mr"]+"  ")
             print("                        " + "     " + "|" + "     " + "|" + "     ")
             print("                        "+"_________________")
             print("                        "+"  "+ block["dl"]+"   " + "|"+"  " + block["dm"]+"    "+"|"+"  "+block["dr"]+"  ")
             print("                        " + "     " + "|" + "     " + "|" + "     ")
             if block["tl"]==symbol and block["tm"]==symbol and block["tr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
             elif block["ml"]==symbol and block["mm"]==symbol and block["mr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
             elif block["dl"]==symbol and block["dm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
             elif block["tl"]==symbol and block["ml"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 1 IS WINNER *") 
                  break
             elif block["tm"]==symbol and block["mm"]==symbol and block["dm"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
             elif block["tr"]==symbol and block["mr"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break
             elif block["tl"]==symbol and block["mm"]==symbol and block["dr"]==symbol:
                  print("                * PLAYER 1 IS WINNER *") 
                  break
             elif block["tr"]==symbol and block["mm"]==symbol and block["dl"]==symbol:
                  print("                * PLAYER 1 IS WINNER *")
                  break

print("                        THANKYOU")        
       
