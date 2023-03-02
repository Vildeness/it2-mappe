

assert 10 > 5 #10 er større enn 5 derfor gjør denne ingeting

try:
    assert 20 > 20 # 10 er ikke større enn 20 derfor gir denne en feilmelding
except:
    print("hei på deg")

#oppgave: definer en funkjson med navn areal som tar inn høyde og en bredde og retunerer arealet av en rektangel med tilsvarende høyde og bredde

def areal(høyde, bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde

#oppgave: test funkjsonen areal på tre forskjellige rektnagler med assert

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(4,3) == 12

print("koden er ferdig")

