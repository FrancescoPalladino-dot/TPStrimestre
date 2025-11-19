import Calcolatrice
#from Calcolatrice import *

if __name__=="__main__":
    operazione = input("Scegli che operazione fare (+,-,x,:): ")
    primoNum = int(input("Inserisci primo numero"))
    secondoNum = int(input("Inserisci secondo numero"))
    m1 = int(primoNum)
    n1 = int(secondoNum)
    if operazione == "+":
        risultato = Calcolatrice.add(primoNum, secondoNum)
    elif operazione == "-":
            risultato = Calcolatrice.sub(primoNum, secondoNum)
    elif operazione == ":":
            risultato = Calcolatrice.div(primoNum, secondoNum)
    elif operazione == "x":
            risultato = Calcolatrice.mol(primoNum, secondoNum)
    else:
        risultato = "Operazione non valida!"

print("Il risultato è:", risultato)
#quando faccio python calc.py
#a calc.py viene assegnato il nome main  __name__ --> __main__ programma viene lanciato solo se è il programma main

#quando faccio import calc.py
#__name__ -->

