# Ky është një koment, pjesë kodi që nuk ekzekutohet

# Kjo deklaratë printon (afishon) në ekran fjalën Përshëndetje!
print("Përshëndetje!")

# Python përdor nxjerrjen në kryerradhë për të ndarë një bllok kodi
# Nuk përdoret pikëpresja (;)

if 5 > 2:
  print("Python është gjuhë programimi e interpretuar!") 
  
# ■ Variablat 

# Variablat nuk kanë ndonjë komandë për t'u deklaruar
# Një variabël krijohet në momentin që ju i nënshkruani (përcaktoni) një vlerë asaj.
# Caktimi i vlerës bëhet nga operatori i caktimit të vlerës që është shenja e barazimit (=)
# më poshtë x  është variabël e tipit integer (numër i plotë)
x = 4 

# variabla x është tani i tipit string (sekuencë karakteresh)
x = "3. Ardian" 

# Rregullat për emërtimet e variablave në Python:
# ●	Një emër variable duhet të fillojë me një shkronjë ose me karakterin e nënvijëzimit (ang. underscore)
# ●	Në emër variable nuk mund të fillojë me një numër
# ●	Një emër variable mund të përmbajë vetëm karaktere alfanumerike dhe shenja nënvijëzimi (A-z, 0-9 dhe _ )
# ●	Emrat e variablave janë të rastit të ndjeshëm  (mosha, Mosha dhe MOSHA janë tre variabla të ndryshme).

print(x)

# Python ju lejon të caktoni vlerat variablave të shumta në një linjë kodi:
x, y, z = "Portokall", "Banane", "Qershi"
print(x)
print(y)
print(z)

# Ose ju mund të përcaktoni të njëjtën vlerë variablave të shumta në një linjë kodi:
x = y = z = "Python"
print(x)
print(y)
print(z)

# Deklarata print e Python përdoret shpesh për të afishuar variablat:
# Për të kombinuar edhe tekstin edhe variablën, Python përdor shpesh karakterin + :
x = "gjuhë programimi!"
print("Python është " + x)

# Ju mund të përdorni karakterin + për të shtuar një variabël tek një variabël tjetër:
x = 5
y = 10
print(x + y)

# Në rast se provoni të kombinoni një string me një numër, Python do të gjenerojë një gabim në kod:
'''
x = 5
y = "Ardian"
print(x + y) 
Mesazhi i gabimit:
TypeError: unsupported operand type(s) for +: 'int' and 'str' 
'''
# Lloji i gabimit: Tip i pa mbështetur i operandit (njërës nga vlerat në mbledhje) për + ‘integer’ dhe ‘string’

# ■ Variablat globale

# Variablat që krijohen jashtë një funksioni (si në të gjithë rastet e mësipërme) njihen si variabla globale. 
# Variablat globale mund të përdoren nga të gjithë, edhe brenda funksioneve edhe jashtë tyre.
# Kodi i mëposhtëm është dhënë për të shpjeguar variablat globale, do të merremi më vonë me funksionet
x = "gjuhë programimi!" # variabël globale

def funksion1():
  print("Python është " + x) # Python është + vlera e variablës globale
funksion1()

# Nëse ju krijoni një variabël me të njëjtin emër brenda një funksioni, kjo variabël do të jetë variabël lokale dhe do të mund të përdoret vetëm brenda funksionit ku është përcaktuar. 
# Variabla globale që ishte përcaktuar më parë do të qëndrojë siç ishte, globale dhe me vlerën e saj origjinale (të pandryshuar):
# Krijoni një variabël brenda një funksioni, me të njëjtin emër si variabla globale:
x = "gjuhë programimi!" # variabla globale

def funksion2():
  x = "gjuhë fantastike!" # variabla lokale
  print("Python është " + x)

funksion2()

print("Python është " + x) # merr vlerën e variablës globale

# Fjala kyçe global (globale)

# Normalisht, kur ju krijoni një variabël brenda një funksioni, variabla është lokale dhe mund të përdoret vetëm brenda atij funksioni.
# Për të krijuar një variabël globale brenda një funksioni, ju mund të përdorni fjalën kyçe global. 
# Në rast se ju përdorni fjalën kyçe global, variabla i përket rrezes së veprimit globale (pra në të gjithë programin). 
def funksion3():
  global x  # variabla x do të jetë variabël globale
  x = "gjuhë fantastike!"
  print("Python është " + x)
funksion3()

print("Python është " + x) # merr vlerën e variablës globale

# Gjthashtu, përdorni fjalën kyçe global në rast se dëshironi të ndryshoni vlerën e një variabël globale brenda një funksioni.
# Për të ndryshuar vlerën e një variable globale brenda një funksioni, referohuni variablës që dëshironi t’i ndryshoni vlerën duke përdorur fjalën kyqe global:

x = "gjuhë programimi!" # në këtë rast është variabël globale pasi është përcaktuar jashtë funksionit

def funksion4():
  global x # variabla x bëhet variabël globale
  x = "gjuhë fantastike!"

funksion4()

print("Python është " + x) # merr vlerën e variablës x brenda funksionit

# ■ Llojet e të dhënave të integruara (ang. built-in)

# Në programim, lloji i të dhënave është një koncept i rëndësishëm.
# Variablat mund të ruajnë të dhëna të llojeve të ndryshme, dhe llojet e ndryshme mund të bëjnë gjëra të ndryshme.
# Python ka të parazgjedhur llojet e mëposhtme të të dhënave të integruara, në këto kategori:

# Tipi tekst:	
# str (për sekeucat e karaktereve)

# Tipet numerike:	
# int (numër i plotë, integer) 
# float (numër me pikë dhjetore) 
# complex (numër i përbërë)

# Tipet e sekuencave:
# list (listë) 
# tuple (tufë) 
# range (vazhdimësi vlerash)

# Tipet hartë:	
# dict (fjalor)

# Tipet listuese:	
# set (kolekison) 
# frozenset (seti i pandryshueshëm)

# Tipet boolean:	
# bool (Vlerat boolean janë shprehje që marrin vetëm vlerat e vërtetë (ang. True) ose e gabuar (ang. False))

# Tipet binare:
# bytes, (Bytes përmbajnë bajtë të vetëm - i pari është i pandryshueshëm ndërsa i dyti është një sekuencë e ndryshueshme. Kujdes në përdorimin e karakterit pasi ky lloj tipi i të dhënave pranon vetëm shkronja letrare ASCII.)
# bytearray (Lloji i bytearray është një sekuencë e ndërrueshme e numrave të plotë në rangun 0 <= x <256.), 
# memoryview (Kthen një objekt të pamjes së kujtesës të argumentit të dhënë.)

#Ju mund të merrni (gjeni) tipin e të dhënave të çdo objekti duke përdorur funksionin type() :
# Printo (afisho) tipin e të dhënave të variablës (ndryshores) x:
x = 5
print(type(x))
