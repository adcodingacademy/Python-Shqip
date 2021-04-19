
# 1. Importimi i modulit date class datetime 
from datetime import date

# krijimi i objektit data për datën e sotme

data_sotme = date.today()


ditëlindja = int (input("Shkruaj vitin e lindjes: "))
mosha = ditëlindja - data_sotme.year
print("Mosha juaj është: ", mosha)
