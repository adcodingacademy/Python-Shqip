import numpy
import scipy
from scipy import stats

shpejtësia = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x1= numpy.mean(shpejtësia)
# Mesatarja (ang.mean) 
# Vlera mesatare e një grupi të dhënash (shuma e të gjitha vlerave e pjestuar me numrin e të gjitha vlerave)
# Metodë e NumPy

x2= numpy.median(shpejtësia)
# Mesorja (ang. median) 
# Vlera e mesit e një grupi të dhënash (të renditura) 
# Nëse janë dy vlera mesatarja e këtyre dy vlerave të mesit (për lista me numër artikujsh çift).
# Metodë e NumPy

x3= stats.mode(shpejtësia)
# Moda (ang.mode)
# Vlera që përsëritet më shumë në një grup të dhënash
# Metodë e SciPy
# from scipy import stats

x4= numpy.std(shpejtësia)
# Devijimi standart (ang. standart deviation)
# Devijimi standard është masa e variacionit ose shpërhapjes së të dhënave, apo shpërndarjes së probabilitetit.
# Devijimi standart është rrënja katrore e variacionit
# Metodë e NumPy

x5= numpy.var(shpejtësia)
# Variacioni (ang. variance)
# Variacioni është një tjetër numër i cili tregon se sa të shpërndara janë vlerat. 
# Në rast se ju shumëzoni devijimin standart me vetveten, ju merrni variancën.
# Metodë e NumPy

x6= numpy.percentile(shpejtësia, 90)
# Përqindja (ang. percentile)
# Përqindjet përdoren në statistika për t'ju dhënë një numër që përshkruan vlerën që një përqindje e caktuar e vlerave janë më të ulëta se.
# Metodë e NumPy
# numpy.percentile(x, numri i përqindjes)

print("1. Mesatarja e shpejtësisë është:", x1)
print("2. Mesorja e shpejtësisë është:", x2)
print("3. Moda e shpejtësisë është:", x3)
print("4. Devijimi standart i shpejtësisë është:", x4)
print("5. Variacioni i shpejtësisë është:", x5)
print("6. Përqindja e shpejtësisë është:", x6)
