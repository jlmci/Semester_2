from my_function import build_experiment, build_person
 
if __name__ == "__main__":
     my_person = build_person("Jakob", "Ladurner", "male", 25)
     my_experiment = build_experiment("Experiment 1", "20.03.2025", "Supervisor_1" , "Jakob")
     print(my_person)
     print(my_experiment)