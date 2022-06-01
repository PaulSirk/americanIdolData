import pandas as info

class examine():
    def __init__(self, datafile):
        self.datafile = info.read_csv(datafile)

    def outputData(self) -> None:
        print(self.datafile)
    
    def filterBy(self) -> None:
        undecided: bool = True
        while undecided:
            idolData: str = input("Which column do you want to filter by? ")
            options: list = ["Winner number", "First Name", "Last Name", "Age", "Gender",
            "Race", "Birth Year", "State", "Year"]
            
            print(*options, sep="\n")
            if idolData in options:
                undecided = False
                if idolData.lower == "state":
                    self.filterByState()


    def filterByState(self, state) -> None:
        filteredState = self.datafile.where(self.datafile["State"] == state)
        print(filteredState)
        
        def userInput(func) -> None:
        decided: bool = False

        while not decided:
            num = input("Input in a number to filter by. ")
            if num.isdigit():
                y = int(num)
                def inner(y):
                    x = func(y)
                    print(x)
                    return x
                return inner(y)
            else:
                print("\n\tType in a valid number.\n")
        return inner(num)

    @userInput
    def ageFilter(self, num: int):
        filteredAge = self.datafile.where(self.datafile["Age"] == num)
        return filteredAge

    def numFilter(self):
        x = self.userInput(self.ageFilter)
