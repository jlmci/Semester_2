import my_functions as mf
import datetime

if __name__ == "__main__":
    
    #age = input("Enter age:")
    #sex = input("Enter gender:")
    #first_name = input("Enter first name:")
    #last_name = input("Enter last name:")
    experiment_name = input("Enter experiment name:")
    supervisor = input("Enter supervisor:")
    subject = input("Enter subject:")
    date  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #person = mf.build_person(first_name, last_name, sex, age)
    experiment = mf.build_experiment(experiment_name, date, supervisor, subject)

    print(experiment)
    
