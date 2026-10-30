import requests
url="https://wttr.in/Trzcianka?format=j1"
url2="https://wttr.in/Poznan?format=j1"
odpowiedz=requests.get(url)
odpowiedz2=requests.get(url)
dane=odpowiedz.json()
dane2=odpowiedz2.json()
temperatura=dane['current_condition'][0]['temp_C']
temperatura2=dane2['current_condition'][0]['temp_C']

print(f"Aktualna temperatura w Trzcaince to {temperatura}°C")
print(f"Aktualna temperatura w Poznaniu to {temperatura2}°C")