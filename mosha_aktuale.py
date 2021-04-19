# 1. Importimi i modulit date class datetime 
from datetime import date

# krijimi i objektit data për datën e sotme

data_sotme = date.today()


ditëlindja = int (input("Shkruaj vitin e lindjes: "))
mosha = data_sotme.year - ditëlindja
print("Mosha juaj është: ", mosha)
