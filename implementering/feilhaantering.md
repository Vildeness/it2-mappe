# vern mot kjøretidsfeil og logiske feil i prgrammer

## Kjøretidsfeil

Håndtering av kjøretidsfeil gjøres med nøkkelordene try og excpet.
python forsøker å kjøre kodeblokken som ligger under `try`, hvis python får en feilmelding, vil den kjøre kodeblokken som ligger under except. 

```python

try:    
    alder = int(input("alder:"))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("feil: aldeer må være heltall")

print("koden fortsetter")

```

### Ekspert tips: whilde-løkke med try-except

```python
while True:
    try: 
        alder = int(input("alder: "))
        break
    except:
        print("alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")

```

## logiske feil

for å oppdage logiske feil i pyhton program kan vi bruke nøkkelordet assert, for å forsikre oss om at koden gir korekte svar

eksempel:

```python
assert 10 > 5 #10 er større enn 5 derfor gjør denne ingeting
assert 20 > 20 # 10 er ikke større enn 20 derfor gir denne en feilmelding

```

test av funskjoner
```python
assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(4,3) == 12

```
###eksperttips: håndtering av kjøretidsfeil og logisk feil

```python
while True:
    try: 
        alder = int(input("alder: "))
        assert alder >= 0
        break
    except:
        print("alder må være et positivt heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
```
