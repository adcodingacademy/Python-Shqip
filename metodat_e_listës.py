# Metodat e listës

emra = ["Armand", "Albert", "Alfred", "Almario", "Agron", "Astrit"]
numra = [] # listë boshe

# për të shtuar një element të ri përdoret metoda append() - shto()
# kjo metodë e vendos elementin në vendin e parë bosh
numra.append(1) # kupto: tek lista numrat shto elementin 1
print(numra) # afishon [1]

# për të shtuar një element në një pozicion të caktuar përdoret metoda insert() - fut()
# kjo metodë e vendos elementin në vendin e caktuar brenda kllapave rrethore
# plotësohet indeksi ku do të vendoset dhe më pas edhe elementi që duam të shtojmë
emra.insert(0, "Ardian") # kupto: në listën emra fut elementin Ardian në pozicionin e parë (0)
print(emra)

# për të fshirë një element nga një listë përdoret metoda remove() - largo()
emra.remove("Ardian")
print(emra)

# për të fshirë të gjithë elementet nga një listë përdoret metoda clear() - pastro()
# kjo metodë nuk pret asnjë vlerë, nese jepni një arguement:
# do të merrni: TypeError list.clear() takes no argument (x given)
emra.clear()
print(emra)

# për të zbuluar nëse një element ekziston apo jo në listën tonë përdorim operatorin in - në
numra1 = [1,2,3,4,5,6]
print(1 in numra1) # kupto printo True ose False nëse 1 është në listën numra1

# print(1 in numra1) është një shprehje boolean: 
# afishon True nëse vlera e caktuar gjendet në listën tonë
print(9 in numra1)
# afishon False nëse vlera e caktuar nuk gjendet në listën tonë

# për të zbuluar se sa elementë janë në një listë përdorim funksionin e integruar len() - gjatësia()
# afishon një numër
print(len(numra1)) # kupto: printo gjatësinë e listës numra1
