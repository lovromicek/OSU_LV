def total_euro():
    return radniSati * eurPoSatu

try:
    radniSati = int(input())
except:
    print("Molim unesite broj.")
    
eurPoSatu = 8.5
ukupnaZarada = total_euro()
print(ukupnaZarada)