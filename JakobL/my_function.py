def calc_estimate_max_hr(age_years : int , sex : str) -> int:
  """
  See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ for different formulas
  """
  if sex == "male":
    max_hr_bpm =  223 - 0.9 * age_years
  elif sex == "female":
    max_hr_bpm = 226 - 1.0 *  age_years
  else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
    max_hr_bpm  = input("Enter maximum heart rate:")
  return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    person_dict = { "first_name" : first_name,
             "last_name" : last_name,
             "age" : age,
             "estimate_max_hr" : calc_estimate_max_hr(age,sex)}
    return person_dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    experiment_dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject
            }
    return experiment_dict

def ask_name() -> str:
    """Asks the user for their name."""
    try :
        name = input("What is your name? ")
        return name
    except Exception as e:
        print("Please enter a valid name")
        ask_name()

def ask_number() -> int:
    """Asks the user for a number."""
    try:
        number = int(input("Enter a number: "))
        return number
    except Exception as e:
        print("Please enter a valid number")
        ask_number()

def ask_sex() -> str:
    """Ask the user for the sex"""
    sex_string = input("Enter sex (w/m): ")
    if sex_string == "w":
        return "female"
    elif sex_string == "m":
        return "male"
    else:
        print("Please enter 'w' or 'm'")
        ask_sex()


def berechne_alter(date_of_birth):
    """Berechnet das Alter basierend auf dem Geburtsdatum im Format YYYY-MM-DD."""
    # Beispiel: 2004-08-01
    from datetime import datetime
    heute = datetime.today()
    # Konvertiere das Geburtsdatum in ein datetime-Objekt
    date_of_birth = datetime.strptime(date_of_birth, "%Y-%M-%d")
    # Berechnung des Alters
    alter = heute.year - date_of_birth.year - ((heute.month, heute.day) < (date_of_birth.month, date_of_birth.day))
    return alter
