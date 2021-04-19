pesha = float(input("Pesha: "))
njësia = str(input("Në (K)g apo L(b)s: "))
if njësia.upper() == "K": 
    pesha_konvertuar = pesha / 0.45
    print("Pesha në paund është" + str(pesha_konvertuar) +  "Lbs.")

else:
    pesha_konvertuar = pesha * 0.45
    print("Pesha në kilogramë është" + str(pesha_konvertuar) + "Kg.")
