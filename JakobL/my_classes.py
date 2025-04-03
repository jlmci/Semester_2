class Subject():
    def __init__(self, first_name, last, sex, age):
      self.first_name = first_name
      self.last_name = last
      self.sex = sex
      self.age = age

    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      from my_function import estimate_max_hr
      return estimate_max_hr(self.age, self.sex)
    
    def get_subject_info(self):
      return {
          "first_name": self.first_name,
          "last_name": self.last_name,
          "age": self.age,
          "sex": self.sex,
            "estimate_max_hr": self.estimate_max_hr()
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