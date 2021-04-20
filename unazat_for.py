# Unazat for 
# Unazat for përdoren për të përsëritur një listë dhe aksesuar secilin element veçmas

# Le të deklarojmë një listë numrash:

numra = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
# nëse printojmë këtë listë afishohet në të njëjtën mënyrë siç e kemi shkruajtur
print(numra) # afishon [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

# nëse duam të printojmë secilin element veçmas përdorim unazën for (për)
# shkruajmë fjalën kyçe for
# më pas deklarojmë variablën e unazës
# shkruajmë fjalën kyçe in për të përcaktuar nga do të merren rezultatet
# shkruajmë emrin e listës dhe dypikëshin: për të filluar një bllok kodi

for elementë in numra: # kjo është unaza for
# me këtë unazë for mund të përsërisim të gjithë elementët e listës
# në secilën përsëritje variabla e unazës do të mbajë një vlerë
# kështu elementi i parë do të jetë elementi i parë në listën ku do të marrim rezultatet:
# elementë = 1, elementë =2 etj.
    print(elementë) # afishon 1,2, 3, 4, 5, 6, 7, 8, 9, 10

# kjo mund të bëhet edhe me unazën while:

i = 0
while i < len(numra):
    print(numra[i])
    i = i + 1
