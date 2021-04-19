# Operatorët logjikë
# Përdoren për të ndërtuar rregulla kompleksë dhe kushte

# Operatori and
# Nëse të dy shprehjet boolean janë True vlera e shprehjes është True
# në të kundërt False
çmimi = 25
print(çmimi > 10 and çmimi < 30)

# Hapat që ndjekt programi:
# Ruan në memorie vlerën e variablës çmimi që është vlera 25
# Shkon tek komanda print dhe vlerëson shprehjet
# Për komandën çmimi > 10 vlerëson shprehjen si të vërtetë pasi 25 është më e madhe se 10
# Më pas kalon tek komanda and që i kërkon programit edhe një tjetër kusht
# Për komandën çmimi < 30 vlerëson shprehjen si të vërtetë pasi 25 nuk është më e madhe se 30
# pasi vlerësohet shprehja afishon True

# Operatori or
# Nëse njëra nga dy shprehjet boolean është True vlera e shprehjes është True
# në të kundërt False
çmimi = 5
print(çmimi > 10 or çmimi < 30)

# Operatori not
# Ndryshon logjikën e shprehjes
# nëse shprehja është False afishon True
# nëse shprehja është True afishon False
çmimi = 5
print(not çmimi < 4)
# këtu çmimi është më i madh se 4 dhe vlera e shprehjes: çmimi < 4 është False
# operatori not do të afishoje True
