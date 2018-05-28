import random as r
import math as m
def nouveauTas():
    return [r.randrange(5,24) for i in range(r.randrange(3,8))]
def calculScore(tour):
    tot=0
    for i in range(m.ceil(tour/2)): 
        tot+=i*(10**i)
    return tot
    
def printTop10():
    print("Top 10:")
    scoreList=[]
    index=0
    listrange=0
  
    with open("save.txt",'r') as save:
        for best in save:
            scoreList.append([best.strip('\n').split(':')[0],best.strip('\n').split(':')[2]])
    if len(scoreList) <10:
        listrange=len(scoreList)
    else:
        listrange=10
    for l in range(listrange):
        index=0
        maximum=int(scoreList[0][1])
        for i in range(len(scoreList)):
            if int(scoreList[i][1])>maximum:
                maximum=int(scoreList[i][1])
                index=i 
        print(l+1,".",scoreList[index][0],":",maximum)
        scoreList.remove(scoreList[index])
             
            
    
def setup():
    global nomJoueur1
    global nomJoueur2
    global ancienScore1
    global ancienScore2
    global bestScore1
    global bestScore2
    
    
    nomJoueur1,nomJoueur2=("A déterminer","A déterminer")
    ancienScore1,bestScore1,ancienScore2,bestScore2=0,0,0,0
    joueur1=input("Entrez le nom du joueur 1 : ")
    joueur2=input("Entrez le nom du joueur 2 : ")
    with open("save.txt",'r') as save:
        for ligne in save:
            if ligne.split(':')[0]==joueur1:
                nomJoueur1,ancienScore1,bestScore1=ligne.strip('\n').split(':')
                
            if ligne.split(':')[0]==joueur2:
                nomJoueur2,ancienScore2,bestScore2=ligne.strip('\n').split(':')
                
    if nomJoueur1=="A déterminer":
        nomJoueur1=joueur1
    if nomJoueur2=="A déterminer":
        nomJoueur2=joueur2
    
def printGame(tas):
    string=""
    for i in range(len(tas)):
        string+=str(i+1)+"|"
        for piece in range(tas[i]):
            string+="*"
        for espace in range(23-tas[i]):
            string+=" "
        print(string,"| ",tas[i])
        string=""
def nbrPieceTotal(tas):
    total=0
    for i in tas:
        total+=i
    return total
def jouer():
    tas=nouveauTas()
    setup()
    print("Pour Joueur1:",nomJoueur1,"| Score antérieur:",ancienScore1,"| Meilleur Score:",bestScore1)
    print("Pour Joueur2:",nomJoueur2,"| Score antérieur:",ancienScore2,"| Meilleur Score:",bestScore2)
    tour=1
    while True:
        if tour%2==0:
            print("C'est au tour de ",nomJoueur2," de jouer")
        else:
            print("C'est au tour de ",nomJoueur1," de jouer")
        
        printGame(tas)
        print("Veuillez choisir un tas ")
        numTas=int(input())
        print("Veuillez choisir le nombre de pièce dans le tas: ")
        nbrPiece=int(input())
        try:
            if tas[numTas-1] or tas[numTas-1]<=0:
                if nbrPiece<=23 and nbrPiece>0:
                    if nbrPieceTotal(tas)-nbrPiece <1:
                        score=calculScore(tour)
                        f = open("save.txt","r")
                        lignes = f.readlines()
                        f.close()
                        if tour%2==0:
                            print("Bravo.",nomJoueur1," Vous avez gagné la partie ! SCORE:",score)
                            
                            with open("save.txt",'w') as save:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJoueur1:
                                            pass
                                        else:
                                            save.write(ligne)
                            with open("save.txt",'a') as save:
                                
                                if score>int(bestScore1):
                                    save.write("{}:{}:{}\n".format(nomJoueur1,score,score))
                                else:
                                    save.write("{}:{}:{}\n".format(nomJoueur1,score,bestScore1))

                        else:
                            print("Bravo.",nomJoueur2," Vous avez gagné la partie ! SCORE:",score)
                            with open("save.txt",'w') as save:
                                    for ligne in lignes:
                                        if ligne.split(':')[0]==nomJoueur2:
                                            pass
                                        else:
                                            save.write(ligne)
                            with open("save.txt",'a') as save:
                                if score>int(bestScore1):
                                    save.write("{}:{}:{}\n".format(nomJoueur2,score,score))
                                else:
                                    save.write("{}:{}:{}\n".format(nomJoueur2,score,bestScore2))
                        print("Partie terminée!")
                        printTop10()
                        break  
                
                    if tas[numTas-1]-nbrPiece >=0:
                        tas[numTas-1]-=nbrPiece
                        tour+=1
                else:
                    print("ERREUR! Veuillez choisir un nombre de pièce valide !")
            else:
                print("Vous avez choisi le mauvais tas")
        except:
            print("Il y a eu une erreur veuillez réessayer!")
    nouvPartie=input("Voulez-vous vous engagez dans une nouvelle partie (oui/non)  ")
    if nouvPartie=="oui":
        jouer()
    else:
        print("Dommage! Une prochaine fois peut être!")
        
jouer()	
