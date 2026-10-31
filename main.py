import requests
pory_dnia=[
    {"etykieta": "Noc (0:00)", "indeks": 0},
    {"etykieta": "Rano (6:00)", "indeks": 2},
    {"etykieta": "Południe (12:00)", "indeks":4},
    {"etykieta": "Wieczór (18:00)", "indeks": 6}
]
dni=[
    {"nazwa": "Dzisiaj", "indeks": 0},
    {"nazwa": "Jutro", "indeks": 1},
    {"nazwa": "Pojutrze", "indeks": 2}
]
url="https://wttr.in/Trzcianka?format=j1"
url2="https://wttr.in/Poznan?format=j1"
odpowiedz=requests.get(url)
odpowiedz2=requests.get(url2)
dane=odpowiedz.json()
dane2=odpowiedz2.json()
temperatura=dane['current_condition'][0]['temp_C']
temperatura2=dane2['current_condition'][0]['temp_C']
opis_pogody=dane['weather'][0]['hourly'][2]['weatherDesc'][0]['value']
szanse_na_descz=dane['weather'][0]['hourly'][2]['chanceofrain']

print("Prognoza na 3 dni Trzcianka")
print()
for dzien in dni:
    print(f"--- {dzien['nazwa']} ---")
    dzien_idx=dzien["indeks"]
    for pora in pory_dnia:
        pora_idx=pora["indeks"]
        nazwa=pora["etykieta"]

        temp=dane['weather'][dzien_idx]['hourly'][pora_idx]['tempC']
        deszcz=dane['weather'][dzien_idx]['hourly'][pora_idx]['chanceofrain']
        opis=dane['weather'][dzien_idx]['hourly'][pora_idx]['weatherDesc'][0]['value']
        print(f"[{nazwa}] Temperatura: {temp}° | Deszcz: {deszcz}% | Opis: {opis}")
print()
print()
print("Prognoza na Poznan:")
print()
for dzien in dni:
    print(f"--- {dzien['nazwa']} ---")
    dzien_idx=dzien["indeks"]
    for pora in pory_dnia:
        pora_idx=pora["indeks"]
        nazwa=pora["etykieta"]

        temp=dane2['weather'][dzien_idx]['hourly'][pora_idx]['tempC']
        deszcz=dane2['weather'][dzien_idx]['hourly'][pora_idx]['chanceofrain']
        opis=dane2['weather'][dzien_idx]['hourly'][pora_idx]['weatherDesc'][0]['value']
        print(f"[{nazwa}] Temperatura: {temp}° | Deszcz: {deszcz}% | Opis: {opis}")