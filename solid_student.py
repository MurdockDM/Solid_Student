class Student:

    def __init__(self, first_name, last_name, age, cohort_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cohort_number = cohort_number
        

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in Cohort {self.cohort_number}."
        
    def __repr__(self):
        return f"{self.full_name} is {self.age} years old and is in Cohort {self.cohort_number}."  

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0    

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("This requires a string")

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter          
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("This requires a string")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0 

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("This requires an integer input")

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError("This requires an integer input")

    @property
    def full_name(self):
        try:
            return self.first_name + " " + self.last_name
        except AttributeError:
            return 0        

chad = Student("Chad", "Mullins", 24, 46)

print(chad)
