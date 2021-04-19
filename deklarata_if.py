# Deklarata nëse
# if statement

# Deklarata if përdoret për të marrë vendime

# if kushti :


# ruajmë vlerën e variablës temperatura në memorie e cila është 30
temperatura = 25
# kontrollojmë:
#  nëse vlera e temperaturës është më e madhe ose e barabartë me 30
if temperatura >=30:
# Nëse shprehja vlerësohet si True (e saktë) atëherë afishohet
    print("Temperaturë shumë e nxehtë.")
    print("Le të shkojmë në plazh.")
# Nëse shprehja vlerësohet si False nuk afishohet asgjë

# Nuk është pjesë e bllokut të kodit
# Afishohet gjithmonë
print("Programi përfundoi me sukses!")

# Për të shtuar një kusht tjetër përdorim fjlaën elif (shkurtim për lese if)

temperatura = 25

if temperatura >=30:
# Nëse shprehja vlerësohet si True (e saktë) atëherë afishohet
    print("Temperaturë shumë e nxehtë.")
elif temperatura ==25:
    print("Le të shkojmë në plazh.")
# mund të vendosim sa më shumë kode elif
elif temperatura < 30:
    print("Është nxehtë")
else:
    print("Më mirë jo!")
