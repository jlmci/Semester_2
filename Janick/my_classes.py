class Person():
   def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name


class Subject(Person):
    def __init__(self, first_name, last_name, sex, birthdate): #bir
      super().__init__(first_name, last_name)
      self.sex = sex
      self.__birthdate = birthdate

    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      from my_functions import calc_estimate_max_hr, berechne_alter
      age = berechne_alter(self.__birthdate)
      return calc_estimate_max_hr(age, self.sex)
    
    def get_subject_info(self):
      return {
          "first_name": self.first_name,
          "last_name": self.last_name,
          "birthdate": self.__birthdate,
          "sex": self.sex,
            "estimate_max_hr": self.estimate_max_hr()
      }
    
class Supervisor(Person):
    def __init__(self, first_name, last_name):
      super().__init__(first_name, last_name)

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


