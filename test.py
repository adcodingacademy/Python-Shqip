# Kodi i mëposhtëm importon (nga komanda import) modulin TKinter (tkinter) të 
# cilit do t'i referohemi si (nga komanda as) tk (ose një emër tjetër të cilin mund të caktoni sipas dëshirës).
import tkinter as tk

# Kodi i mëposhtëm krijon një dritare të re dhe e cakton atë në variablën dritare.
dritare = tk.Tk()

# Kodi i mëposhtëm përdor klasën tk.Label  për të shtuar tekst në dritare. 
# Ai krijon një shtojcë Label me tekstin "Përshëndetje, Tkinter" dhe e cakton atë një variable të quajtur përshëndetje:
pershendetje = tk.Label(text="Përshëndetje, Tkinter")

pershendetje.pack()
