try:    
    alder = int(input("alder:"))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("feil: aldeer må være heltall")

print("koden fortsetter")

while True:
    try: 
        alder = int(input("alder: "))
        assert alder >= 0
        break
    except:
        print("alder må være et positivt heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")

