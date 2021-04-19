kursi = "python për fillestarët"
# seria e karaktereve (string) më sipër është një objekt në Python
# ky string ka disa aftësi:
# Metodat kthejnë një seri të re karaktersh.

# Metoda capitalize : bën shkronjën e parë të madhe

kursi1 = kursi.capitalize()
print(kursi1)
# print(kursi) do të afishonte python për fillestarët pa asnjë ndryshim
# ose me metodën tjetër:
print(kursi.capitalize())
# Metoda lower() bën shkronjat e vogla
print(kursi.lower())
# Metoda find() gjen se ku ndodhet karakteri i përcaktuar në serinë e karaktereve
# Afishon pozicionin e parë ku gjendet 
# 1 në këtë rast sepse gjendet si karakteri i dytë
# numërimi fillon nga 0 në python
print(kursi.find('y'))
# Metoda replace() zëvendëson një shprehje me një tjetër aty ku haset kjo shprehje
print(kursi.replace('për', 'me'))
# Metoda find() gjen se ku ndodhet karakteri i përcaktuar në serinë e karaktereve
print(kursi.find('python'))
# ose mund të përdoret edhe in për të gjetur se ku ndodhet karakteri i përcaktuar në serinë e karaktereve
print('python' in kursi)
