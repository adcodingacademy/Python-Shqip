import urllib.request
# hapni një lidhje me një URL duke përdorur urllib
webUrl  = urllib.request.urlopen('https://raw.githubusercontent.com/adcodingacademy/Python-shqip/main/operator%C3%ABt_e_krahasimit.py')

#merrni kodin e rezultatit dhe printojeni atë
print("Rezulatati: " + str(webUrl.getcode()))

# lexoni të dhënat nga URL dhe printoni ato
data = webUrl.read()
print (data)
