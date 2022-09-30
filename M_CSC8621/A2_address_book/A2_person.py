class Person:
    def __init__ (self, name, address, p_num, dob, roll_num):
        self.name = name
        self.address = address
        self.p_num = p_num
        self.dob = dob
        self.roll_num = roll_num

    def __str__ (self):
        string  = f"------------------\n"
        string += f"Name:\t\t{self.name}\n"
        string += f"Address:\t{self.address}\n"
        string += f"Phone Number:\t{self.p_num}\n"
        string += f"Birthday:\t{self.dob}\n"
        string += f"Roll Number:\t{self.roll_num}\n"
        string += f"------------------\n"
        return string