from datetime import date
 
import random
 
erstellungsdatum = date.today()   #Immer Tägliches Datum
 
gerade:int=0
 
 # Funktion zur Eingabe der Experiment-ID
 
def eingabe_experiment_id():
 
     while True:
 
         try:
 
             id_input = int(input("ID bitte: "))
 
             return id_input
 
         except ValueError:
 
             print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")
 
  
 
 # Funktion zur Eingabe des Versuchsleiters
 
def eingabe_versuchsleiter():
 
     while True:
 
         versuchsleiter_input = input("Name des Versuchsleiters: ").strip()
 
         if versuchsleiter_input:  # Überprüft, ob die Eingabe nicht leer ist dürfen auch zahlen dabei sein falls es zb trainer 4 gäbe
 
             return versuchsleiter_input
 
         else:
 
             print("Ungültige Eingabe. Bitte geben Sie einen gültigen Namen ein.")
 
  
 
first_experiment_id = eingabe_experiment_id()
 
Versuchsleiter = eingabe_versuchsleiter()
 
  
 
test:dict={}
 
  
 
for i in range(first_experiment_id,first_experiment_id+10): #erstellen von 10 dictionarys
 
     test[str(i)]= {
 
         "Ersteller": Versuchsleiter,
 
         "Erstellungsdatum": erstellungsdatum,
 
         "Testname": f"Leistungstest {i}",}
 
    
 
for j in range(first_experiment_id,first_experiment_id+5):
 
   print(test[str(j)])
 
  
 
for key in test.keys():
 
     if int(key) % 2:
 
      gerade+=1
 
print("Gerade Keys",gerade)