from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("FirstName", "LastName")
    subject = Subject("FirstName", "LastName", "female", "1990-01-01")
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)


    print(experiment.get_experiment_info())
    #print(subject.__birthdate)
    