experimente :list= []
first_experiment_id : int= 0 #hier beiliebige Zahl als int eintragen
from datetime import datetime

for i in range(10):
  now = datetime.now()
  this_day:str = now.strftime("%Y-%m-%d")
  try:
    if type(first_experiment_id) != int:
      raise TypeError
    dictionary:dict = {"Id_Nummer": int(first_experiment_id) + i, "Versuchsleiter" : "Janick", "Datum" : this_day } #typecasting auf int zum abfangen von floats
    experimente.append(dictionary)
  except TypeError: #zum abfangen von anderen datentypen
    print("first_experiment_id must be integer")
    break
  except: #zum Abfangen von sonstigen Fehlern
    print("Something went wrong")
    break
  finally:
    counter:int = 0
    if i == 9:
      for j in experimente:
        if j["Id_Nummer"] % 2 == 0:
          counter += 1

      for k in range(5):
        print(experimente[k])

      print("Anzahl der geraden Id´s: " + str(counter))
