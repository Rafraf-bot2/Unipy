import re,sys,locale

locale.setlocale(locale.LC_ALL, 'fr_FR')

#CREATION DE SUBST_ENRI##########################################

f = open(sys.argv[1],"r",encoding="utf-8")
t = f.read()
f.close()
f=open("subst_enri.dic","w+",encoding='utf_16')
a = re.findall("([A-Z]+)(\s|:|[A-Z])*[0-9]+(,[0-9]+)?\s?(mg|mol|mmol|ml|µ|.*matin|.*midi|.*soir|/j)",t)

k=1
for i in a:
    if(len(i[0]) > 3):
        print(i[0], k)
        k += 1
        f.write(i[0].lower()+",.N+subst\n")
f.close()

#################################################################

#AJOUT DANS SUBST.DIC############################################

f = open("subst.dic", "r+", encoding='utf_16')
t = f.readlines()
m1 = ord((t[0])[0])
m2 = ord((t[len(t)-1])[0])

f2 = open("subst_enri.dic", "r", encoding='utf_16')
t = f2.readlines()
for i in t:
    if m1 <= ord(i[0].lower()) <= m2:
        #f.write(i.lower()+",.N+subst\n")
         f.write(i)
f.close()
f2.close()

###################################################################

#CREATION DE INFO2#################################################

f = open("subst_enri.dic","r",encoding='utf_16')
f2 = open("info2.txt","w+",encoding='utf_16')
liste = f.readlines()
liste.sort()
x = (liste[0])[0]
k=0
for i in liste:
    if((i[0] == x[0]) and (i!=liste[len(liste)-1])) or ((x[0]=="é" and i[0]=="e") or (x[0]=="e" and i[0]=="é")): k+=1
    else :
        if(i == liste[len(liste)-1]) : k+=1
        if(x[0]=="é"):x="e"
        f2.write("le nombre de substances pour la lettre "+x[0].lower()+": "+str(k)+"\n")
        x = i
        k = 1
f2.write("le nombre total de substances : "+str(len(liste)))
f.close()
f2.close()

#####################################################################


#SUPPRIMER LES DOUBLONS ET ORDONNER SUBST.DIC########################

f = open("subst.dic", "r", encoding='utf_16')
liste = f.readlines()
liste2 = []
for i in liste:
    if i not in liste2:
        liste2.append(i)

liste2.sort(key=locale.strxfrm)
f.close()
f = open("subst.dic", "w", encoding='utf_16')
for i in liste2:
 f.write(i)
f.close()

#####################################################################