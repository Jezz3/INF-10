import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
# Für inline Plot mit Optionen in Jupyter, ansonsten auskommentieren
%matplotlib widget
plt.close('all')

# Spin-Konfiguration entpacken und Spalten in Variablen speichern
s, sx, sy, sz = np.loadtxt("./Bilder/J160sc/spinDomanwand1.csv", unpack = True)

# Auswahl entlang welcher Spins die z-Komponente untersucht werden soll
spins = range(2350,2400,1)

# z-Komponente der Spins
y1 = []
for i in spins:
    y1.append(sz[i])

# Position der Spins auf der x-Achse
x1 = range(len(y1))

# Funktion an die gefittet wird
def tanhfit(x, y_0, x_0, a, b):
    return(y_0+a*np.tanh((x-x_0)/(b/2)))
           
# Fit der Funktion anhand der Daten aus y1 und x1. Speicher der berechneten Variablen und der Covarianz
popt, pcov = curve_fit(tanhfit, x1, y1)

# Breite b des Tanges ausgeben und Betrag nehmen
print("Breite:", abs(popt[3]))

# Für das Plotten der gefitteten Kurve mehr x-Datenpunkte erstellen damit Verlauf schöner ist
xfit1=np.linspace(0,len(y1),100)

# Einstellungen des Plottes
plt.style.use(['science',"grid",'no-latex'])
plt.rcParams['figure.figsize'] = [7, 5]
plt.figure()

# Daten Plotten
plt.plot(x1,y1,"*", markersize="2", color = "orange")

# Fit Plotten
plt.plot(xfit1,tanhfit(xfit1, *popt),"-", markersize="2", color = "orange")

plt.show()
