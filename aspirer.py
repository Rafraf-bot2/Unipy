import re, sys, urllib.request

x = sys.argv[1]
j = ord(x[2])-ord(x[0])
x = x[0]


#CREER SUBST.DIC################################################

f = open("subst.dic", "w+", encoding='utf_16')
for k in range(j+1):
 lien = "http://localhost:"+sys.argv[2]+"/vidal/vidal-Sommaires-Substances-"+x+".htm"
 fp = urllib.request.urlopen(lien)
 mybytes = fp.read()
 mystr = mybytes.decode("utf8")
 fp.close()
 a = re.findall(r"<a href=\"Substance/.+\.htm\">(.+)</a>",mystr)
 for i in a:
    f.write(i+",.N+subst\n")
 x = chr(ord(x)+1)
f.close()

#################################################################

#CREER INFO.TXT##################################################

f = open("subst.dic", "r", encoding='utf_16')
f2 = open("info.txt", "w", encoding='utf_16')
t = f.readlines()
x = (t[0])[0]
k = 0
for i in t:
    if((i[0] == x[0]) and (i != t[len(t)-1])) or ((x[0] == "é" and i[0] == "e") or (x[0] == "e" and i[0] == "é")): k += 1
    else:
        if i == t[len(t)-1]: k += 1
        if x[0]=="é": x = "e"
        f2.write("le nombre de substances pour la lettre "+x[0]+": "+str(k)+"\n")
        x = i
        k = 1
f2.write("le nombre total de substances : "+str(len(t)))
f2.close()

#################################################################