# Unazat while në Python
# while loops

# Unazat while përdoren për të përsëritur një bllok kodi disa herë

# Për shembull për të printuar numrat nga 1-5

# Mënyra e parë:
print("1")
print("2")
print("3")
print("4")
print("5")

# Mënyra e dytë
# me përdorimin e unazës while
# shkurtohen rreshtat e kodit

# fillojmë me deklarimin e një variable dhe i vendosim numrin tonë fillestar, 1 në këtë rast

nr_parë = 1

# më pas shkruajmë fjalën kyçe while (ndërsa) dhe më pas shkruajmë një kusht
# për të krijuar kushtin mund të përdorim operatorët e krahasimit
# më pas shkruajmë dypikëshin dhe fillojmë bllokun e kodit

while nr_parë <= 5:
    print(nr_parë) # për të printuar vlerat e nr_parë
    nr_parë = nr_parë + 1 
# për të rritur vlerat e variablës me nga 1 njësi
# në rast se nuk e shkruajmë shprehjen e mësipërme nr_parë do të jetë i barabartë me 1 dhe kodi do të ekzekutohet pa mbarim
# për aq kohë që ky kusht është i vërtetë kodi që kemi shkruajtur në bllokun while do të ekzekutohet

# Për përsëritjen e parë i <=5 Python do të ekzekutojë rreshtin e kodit:
# print(nr_parë) 
# nr_parë = nr_parë + 1 
# do të printojë nr_parë në terminal më pas nr_parë do të bëhet 2 dhe 
# kontrolli kalon tek kushti (ku Python vlerëson shprehjen) për çdo numër tjetër
# 1_000 e bën numrin më të lexueshëm

# shembull 2

i = 1
while i<=10:
    print(i* "*") # shumëzim i një numri me një seri karakteresh
    print(i* "-")
    i = i + 1
