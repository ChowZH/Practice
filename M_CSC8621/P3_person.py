def create_person (name, height, weight):
    details = {"name":name, "height":height, "weight":weight}
    return details

def format_display (name):
    print("Name:\t{}\nHeight:\t{} M\nWeight:\t{} Kg".format(name['name'], name['height'], name['weight']))

# Assignment Task 5
def calc_bmi (name):
    BMI = float (name['weight'])/(float (name['height'])**2)
    name["BMI"] = BMI
    return BMI

# Assignment Task 6
def bmi_status (name):
    if name['BMI'] < 18.5:
        name["status"] = 'underweight'
    elif 18.5 <= name['BMI'] < 25:
        name["status"] = 'Healthy'
    elif 25 <= name['BMI'] < 30:
        name["status"] = 'Overweight'
    else:
        name["status"] = 'Obese'

def more_display (name):
    print("Name:\t{}\nHeight:\t{} M\nWeight:\t{} Kg\nBMI:\t{}\nStatus:\t{}".format(name['name'], name['height'], name['weight'], name['BMI'], name['status']))

def main():
    dude_A = create_person("testboi1", 1.9, 86)
    format_display (dude_A)

    # Assignment Task 5
    print ("Answers for assignment task 5:\n")
    print ("BMI of {0} is {1:.2f}".format (dude_A.get("name"), calc_bmi(dude_A)))
    
    # Assignment Task 6
    print ("Answers for assignment task 6:\n")
    bmi_status (dude_A)
    more_display (dude_A)


if __name__ == "__main__":
    main()