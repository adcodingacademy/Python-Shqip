# Deklarimi i listave

# emërtimi_i_listës = [ elementët e listës të ndarë me presje dhe në thonjëza ]

lista1 = []
# këtu lista1 është një listë boshe
# elementët në listë futen në kllapa katrore dhe ndahen me presje
# indekset në Python fillojnë nga 0 për elementin e parë
lista1.append(1)
# përdorimi i metodës .append(x) për të shtuar vlerën x në listë
lista1.append(2)
lista1.append(3)
print(lista1[0]) # printon 1
print(lista1[1]) # printon 2
print(lista1[2]) # printon 3
print(lista1)

# printon 1,2,3
for x in lista1:
# për vlerën e x në listën tonë do të printojë x
# kemi tre vlera të mundshme kështu do të printojë 1, 2, 3
# rezultati do të shfaqet në rreshta të ndarë sepse është një unazë
# dhe çdo rresht i përket një rezultati nga lista
    print(x)


# listë me të gjithë elementët

lista2 = [ "BMW", "Ford", "Audi"]
print(lista2[0])
print(lista2[1])
print(lista2[2])
for makina in lista2:
    print(makina)
