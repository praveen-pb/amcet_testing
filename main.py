

class BasicInfo:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_name_and_gender(self):
        return f"{self.name} - {self.gender}, this is it"

    def get_full_name(self):
        """
        we can add logics here
        """
        return f"{self.name} is full name amcet"

    def get_age(self, as_int=False):
        if as_int:
            return self.age

        return f"{self.age} is current age"

    def get_bank_details(self, bank_name):
        if type(bank_name) is not str:
            return "invalid bank name"

        match bank_name:
            # return true if user has account
            case "SBI":
                return True
            case "Indian":
                return False
            case "Axis":
                return True

    def get_balance(self, bank_name):
        if not isinstance(bank_name, str):
            return "invalid bank name to get balance"

        if bank_name == "SBI":
            return 10000
        elif bank_name == "Indian":
            return None
        elif bank_name == "Axis":
            return 50000

    def get_bank_details(self):
        return None


basic_info = BasicInfo("praveen", 25, "male")
keyword = basic_info.get_full_name()

basic_info_2 = BasicInfo("naveen", 28, "male")
keyword_2 = basic_info.get_full_name()
print(keyword)
