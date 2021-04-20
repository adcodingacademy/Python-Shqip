# Funksioni range()
# Funksioni range() përdoret për të gjeneruar një seri numrash
# Funksioni range() është funksion i ntegruar
numra = range(5)
# krijojmë funksionin range: range()
# kalojmë një vlerë në të: 5
# kjo do të printojë një objekt range
# një objekt range është një objekt që mund të ruaje një sekuencë numrash
# numra = range(5) është një objekt që mban vlerat nga 0 - 5 duke përjashtuar 5
print(numra) # afishon range(0, 5) pasi është paraqitja e objektit range()
# për të shikuar numrat në këtë rang duhet të përsërisim këtë rnag vlerash me unazën for
# unaza for mund të përdoret në çdo objekt që paraqet një seri elementësh
for numrat in numra:
    print(numrat)

# Shembull 2
# Përcaktojmë vlerë fillestare të rangut: 5
# dhe vlerën fundore të vargut: 10 (e cila nuk përfshihet)
numra2 = range(5, 10)
for i in numra2:
    print(i)

#shembulli 3
# Për të kaluar numrat në një listë me hapa (step)
# vendosim argumentin e tretë step (hapi) 2, 3 etj. për të kaluar aq numra sa kemi nevojë
numra2 = range(0, 10, 2)
for i in numra2:
    print(i)

# shembulli 4
# kur nuk duam të ruajmë rangun e vlerave në një variabël 
for i in range(5):
    print(i)
