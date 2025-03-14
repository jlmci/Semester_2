#Jakob Ladurner

# erstellen des Dicitonarys und hilfsvariablen inklusive des TypeHintings

power_test : dict = {}

first_experiment_id : int = 0

gerade_keys : int = 0


 

#Fehlerekennung der Eingabe: NUR Int erklaubt

try:

    first_experiment_id = int(input("Bitte gib die nummer des Ersten versuchs ein: "))


 

    # schleife zum erstellen des dictionarys

    for id_number in range(first_experiment_id,first_experiment_id+10):

        power_test[str(id_number)] = {"test_leader" : "Jakob Ladurner",

                                    "date" : "12.03.2025",

                                    "activity" : "Schwimmen",

                                    "distance_km" : 2}

       

    # for schleife zum augeben der ersten 5 test

    for i in range(first_experiment_id, first_experiment_id+5):

        print(power_test[str(first_experiment_id)])


 

    for key in power_test.keys():

        if int(key) % 2:

            gerade_keys += 1

    print("Menge der Geraden Keys: ", gerade_keys)


 

    print(power_test)

 

except:

    print("Bitte ein Int eingeben !!")
