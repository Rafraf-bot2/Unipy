import os
import sys
ar1=sys.argv[1]
ar2=sys.argv[2]
ar3=sys.argv[3]
os.system("python aspirer.py "+ar1+" "+ar2)
os.system("python enrichir.py "+ar3)
os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
####si les scripts se trouvent dans C:\Program Files (x86)\Unitex-GramLab\App il faut exec
####unitex.py en mode admin
####sinon il suffit simplement de mettre le chemin C:\Program Files (x86)\Unitex-GramLab\App dans la
####variable d'environnement PATH pour pouvoir utiliser UnitexToolLogger a partir de n'importe quel repertoire
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt")
os.system("UnitexToolLogger Compress subst.dic")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt subst.bin delaf.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s 12 -l 40 -r 55")
