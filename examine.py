from curses.ascii import isdigit
from datetime import datetime
from tokenize import Decnumber
from unicodedata import name
import pandas as info
from datetime import datetime

class examine():
    def __init__(self, datafile):
        self.datafile = info.read_csv(datafile)

    def output_data(self) -> None:
        print(self.datafile)
    
    def filter_by(self) -> None:
        undecided: bool = True
        filter_operations = {"winner num": self.winner_num_filter, 'name': self.name_filter,  
        'age': self.ageFilter, 'gender': self.gender_filter, 'race': self.race_filter,
        'birthyear': self.birthyear_filter, "state": self.state_filter}
        
    def valid_int(self) -> int:
        while True:
            potential_num = input("Type in a number. ")
            if potential_num.isdigit() and int(potential_num) > 0:
                return int(potential_num)
            else:
                print("Type in a positive integer.")

    def winner_num_filter(self) -> None:
        win_num : int = self.valid_int()
        filtered_win = self.datafile.where(self.datafile['WinnerNum'] == win_num)

    def name_filter(self) -> None:
        undecided : bool = True
        decision : str = ''
        while undecided:
            decision = input("Do you want to filter by first name or last name?\n(Type in 'first' or 'last') ")
            decision = decision.lower()
            if decision == 'first' or decision == 'last':
                undecided = False

        named : str = input('Type in a name to filter by. ')
        named = named.lower()
        named = named.capitalize()
        filter_name = self.datafile
        if decision == 'first':
            filter_name = self.datafile.where(self.datafile['FirstName'] == named)
        else:
            filter_name = self.datafile.where(self.datafile['LastName'] == named)
        
        print(filter_name.dropna())

    def age_filter(self) -> None:
        age : int = self.valid_int()
        filter_age = self.datafile.where(self.datafile["Age"] == age)
        print(filter_age)

    def gender_filter(self) -> None:
        gender_unknown : bool = True
        gender : str = ''
        while gender_unknown:
            gender = input("Which gender do you want to filter by? (male or female) ")
            if gender == 'male' or gender == 'female':
                gender_unknown = False

        filter_gender = self.datafile.where(self.datafile['Gender'] == gender)
        print(filter_gender.dropna())

    def race_filter(self) -> None:
        race = input("Type in a race to search by. ")
        filter_race = self.datafile.where(self.datafile['Race'] == race)
        print(filter_race.dropna())

    def birthyear_filter(self) -> None:
        winner_birthyear : int = 0
        modern_year = datetime.today().year
        while True:
            winner_birthyear = self.valid_int()
            if 1970 <= winner_birthyear <= modern_year:
                break
            text = "Input a year between 1970 and {current_year}"
            print(text.format(current_year=modern_year))
        
        filter_birth = self.datafile.where(self.datafile['BirthYear'] == winner_birthyear)
        print(filter_birth.dropna())
    
    def state_filter(self) -> None:
        state = input("Which state do you want to filter by? ")
        filtered_state = self.datafile.where(self.datafile["State"] == state.upper())
        print(filtered_state.dropna())