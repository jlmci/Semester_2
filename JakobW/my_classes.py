import requests
import json
class person():
    def __init__(self, first_name, last_name):
        
        self.first_name = first_name
        self.last_name = last_name
        self.id = last_name[0:3]+first_name[0:3]
    def post(self):
        # Paket mit dem Python wie ein Browser agieren kann
      

      my_data = {"id": self.id,"firstName": self.first_name,"lastName": self.last_name}
      data_json = json.dumps(my_data)

          # Übermittlung und speichern der response Objects
      response = requests.post(url = 'http://127.0.0.1:5000/person/', data = data_json)
      response.text
      print(response.text)

       
class Subject(person):
    """A class that represents a subject in an experiment."""
    def __init__(self, first_name, last_name, sex, birthdate):

      super().__init__( first_name, last_name)
      self.sex = sex
      self.__birthdate = birthdate

    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      from my_functions import calc_estimate_max_hr, berechne_alter
      # Geburtsdatum im Format YYYY-MM-DD 
      # in my functions.py wurde die Funktion berechne_alter definiert
      # die das Alter in Jahren berechnet
      age= berechne_alter(self.__birthdate)
      return calc_estimate_max_hr(age, self.sex)
    
    def get_subject_info(self):
      return {
          "first_name": self.first_name,
          "last_name": self.last_name,
          "birthdate": self.__birthdate, #mit zwei__ wird die Variable privat gemacht
          "sex": self.sex,
            "estimate_max_hr": self.estimate_max_hr()   # hier wird die Funktion estimate_max_hr aufgerufen
      }
    
              

class Supervisor():
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name

    def get_supervisor_info(self):
      return {
          "first_name": self.first_name,
          "last_name": self.last_name
      }

class Experiment():
    def __init__(self, name, date):
      self.name = name
      self.date = date

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      self.supervisor = supervisor

    def get_experiment_info(self):
      return {
          "experiment_name": self.name,
          "date": self.date,
          "supervisor": self.supervisor.get_supervisor_info(),
          "subject": self.subject.get_subject_info()
      }
