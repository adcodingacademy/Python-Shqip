# Listat në Python

# Llojet bazë të të dhënave:
# 1. Numrat e plotë: 1, 2, -1
# 2. Numrat dhjetorë: 12.1, -12.1
# 3. Seritë e karaktereve: "përshëndetje", 'programues', '12a'

# Llojet e përbërë të të dhënave:
# 1. Listat përdoren për të shfaqur një listë objektesh p.sh. një listë numrash.


# Listat duhet të ruhen në një variabël
# Elementët e listës vendosen në kllapa katrore dhe ndahen me presje
# sintaksa: emri_variablës = [ "elementët e listës", "të" , "ndarë me presje"]

emrat = ["Ardian", "Armand", "Albert"]
numrat = [23, 25, 31]
print(emrat) # printon listës në të njëjtën mënyrë siç është shkruajtur në kod
print(numrat)

# për të marrë elementë të veçantë nga listat:
# shkruhet emri i listës dhe brenda kllapave katrore shkrueht indeksi i elementit
print(emrat[1]) # për elementin e dytë tek lista e emrave
print(numrat[0]) # për elementin e parë tek lista numrat

print("Përshëndetje "  + emrat[1])
print("Mosha juaj është:  "+ str(numrat[1])) # str() për të konevrtuar numrin në seri karakteresh

# indeksimi negativ në lista (veçori e Python)
print(emrat[-1]) # merr elementin e fundit në fund të listës

# për të zëvendësuar një element të listës ne mund të trajtojmë listën si një variabël
# shkruajmë emrin e listës dhe numrin e indeksit që duam të ndryshojmë
# më pas shkruajmë vlerën që do të vendoset në indeksin e caktuar

# p.sh. komanda e mëposhtëme zëvendëson vlerën Ardian me Agron:
emrat[0] = "Agron"
print(emrat[0])  # printon Agron

# për të caktuar një varg vlerash nga një listë shkruajmë dy indekse:
# indeksin e fillimit : (në mes të dy indeksëve)
# indeksin e përfundimit të listës ( i cili nuk jepet)
emrat1 = ["Armand", "Albert", "Alfred", "Almario", "Agron", "Astrit"]
print(emrat1[0:3]) 
# shprehja e mësipërme nuk e modifikon listën tonë: kthen një listë të re
print(emrat1)
