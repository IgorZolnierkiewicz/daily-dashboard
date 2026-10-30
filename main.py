import requests
url="https://wttr.in/Trzcianka?format=j1"
odpowiedz=requests.get(url)
dane=odpowiedz.json()
temperatura=dane['current_condition'][0]['temp_C']

print(f"Aktualna temperatura w Trzcaince to {temperatura}°C")