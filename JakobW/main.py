from my_functions import build_person, build_experiment
if __name__ == "__main__":
    # build a person
    my_dictenary= build_person("Max","Musterman", "male", 25)
    print(my_dictenary)
    # build an experiment
    experiment = build_experiment("My first experiment", "20.03.2025", "Supervisor1", "Teilnehmer")
    print(experiment)