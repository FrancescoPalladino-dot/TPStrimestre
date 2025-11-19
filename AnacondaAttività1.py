#Anaconda: definire funzione Chiedi che chieda all'utente dei numeri 
#e controlla che inserisca dei numeri e li aggiunge ad una lista
listanumeri = []
def CHIEDI():
    i=0
    print ("inserisci dei numeri")
    risposta = input("vuoi inserire dei numeri? (si o no)")
    while risposta.lower() != "no":
        n=input("Inserisci il numero")
        if n.isnumeric():
            listanumeri.append(n)
        else:
            print("non hai inserito un numero")
        risposta = input("vuoi inserire un altro numero? (si o no)")
    print(f"la lista dei numeri è {listanumeri}")
#riceve come parametro una lista contenente numeri e restituisce una copia
#della lista dove sono eliminati i numeri uguali
listanumeri1=[1,1,1,1,1,2,3,2,32,231,312,321,]
risposta1 = 1
def PULISCI(lista = []):
    lista1 = []
    for i in lista:
        if(i not in lista1):
            lista1.append(i)
    return lista1
print("prova def CHIEDI")
CHIEDI()
print()
print("prova def PULISCI")
print("si parte da una lista con elementi uguali:")
print(listanumeri1)
print("effettuiamo il def: ")
print(PULISCI(listanumeri1))