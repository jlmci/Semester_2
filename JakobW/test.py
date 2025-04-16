from my_classes import Subject, Supervisor, Experiment, person
from my_functions import deleteurl

if __name__ == "__main__":
    """

    # Erstellen eines Leistungstests
    supervisor = Supervisor("FirstName", "LastName")
    subject = Subject("FirstName", "LastName", "female", "2000-01-01") #age wurde auf geburtsdatum geändert
    # Geburtsdatum im Format YYYY-MM-DD
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)


    print(experiment.get_experiment_info())"""

    getapiperson=person("Ross", "Tester")
    #person.post(getapiperson)
    Subjecttoaddemail = Subject(getapiperson.first_name, getapiperson.last_name, "male", "2000-01-01") 
    Subject.update_email(Subjecttoaddemail, "this.is.an.email@web.at", "TesRos")
    #deleteurl("http://127.0.0.1:5000/person/1")



   