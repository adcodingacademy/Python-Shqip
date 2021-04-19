# Veprimet aritmetike që mund të kryhen në Python
# veprime që kryhen nga dy operandë dhe një operator
# opernadët janë vlerat majtas dhe djathtas operatorit
# operatori është shenja aritmetike që kryen veprimin e caktuar

# Operatorët:

# mbledhja : +
# zbritja: -
# pjesëtimi: / (për numrat dhjetorë) dhe // (për numrat e plotë)
# shumëzimi: *
# ngitja në fuqi: **
# modulus: % (pjesa e mbetur nga pjesëtimi i plotë)

print(10 + 3)
print(10 - 3)
print(10 / 3)
print(10 // 3)
print(10 * 3)
print(10 ** 3)
print(10 % 3)

# Caktimi i shtuar (ose caktimi i përbërë) është emri që u jepet operatorëve të caktuar 
# të caktimit në gjuhë të caktuara programimi (veçanërisht ato që rrjedhin nga C). 
# Një caktim i shtuar përdoret zakonisht për të zëvendësuar një pohim kur 
# një operator merr një ndryshore si një nga argumentet e tij dhe pastaj cakton rezultatin përsëri në të njëjtën ndryshore. 
# Një shembull i thjeshtë është x + = 1 i cili zgjerohet në x = x + (1). 
# Ndërtime të ngjashme shpesh janë në dispozicion për operatorë të ndryshëm binarë.

# Rritja e vlerës me 1 njësi (increment)
x = 10
# x = 10 + 1 është e barabartë me:
x +=1
print(x)

# Zvogëlimi i  vlerës me 1 njësi (decrement)
x = 10
# x = 10 - 1 është e barabartë me:
x -=1
print(x)

x = 10
x -= 2
print(x)
x += 2
print(x)
x *= 2
print(x)
x /= 2
print(x)
