# Mënyra e parë:

numri_1 = int (input("Shkruaj numrin e parë:"))
numri_2 = int (input("Shkruaj numrin e dytë: "))

shuma = numri_1 + numri_2
print("Shuma e " , numri_1 ,"+", numri_2, "është", shuma)

# Mënyra e dytë (për numrat e plotë):
numri_1 = input("Shkruaj numrin e parë:")
numri_2 = input("Shkruaj numrin e dytë: ")

shuma = int(numri_1) + int(numri_2)
print("Shuma e " , numri_1 ,"+", numri_2, "është", shuma)

# Mënyra e dytë (për numrat dhjetorë):
numri_1 = input("Shkruaj numrin e parë:")
numri_2 = input("Shkruaj numrin e dytë: ")

shuma = float(numri_1) + float(numri_2)
print("Shuma e " , numri_1 ,"+", numri_2, "është", shuma)

# Mënyra e tretë:
numri_1 = input("Shkruaj numrin e parë:")
numri_2 = input("Shkruaj numrin e dytë: ")

shuma = float(numri_1) + float(numri_2)
# konvertojmë float në str
print("Shuma e " + str(numri_1) , "+ " + str(numri_2) , "është", shuma)
