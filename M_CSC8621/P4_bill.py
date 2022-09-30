# Tariffs dict format as bellow:
# Tariffs = {1:[Tariff_1_flat, Tariff_1_mins, Tariff_1_texts]}

Tariffs = {}
Extra_Mins = 0.1
Extra_texts = 0.05

# Function to add new tariff options
def Available_tariffs (plan, tariff_flat, tariff_mins, tariff_texts):
    Tariffs [plan] = [tariff_flat, tariff_mins, tariff_texts]

# Function to calculate extra cost from usage
def calc_ext (incl, used, rate):
    extra_used = used - incl
    if extra_used > 0:
        extra = extra_used * rate
    else:
        extra_used = 0
        extra = 0
    return (extra_used, extra)

# Function to calculate extra cost from usage 2 (type 1 = calls, 2 = texts)
def calc_ext_2 (plan, type_, used):
    if type_ == 1:
        rate = Extra_Mins
        incl = Tariffs.get(plan)[type_]
    elif type_ == 2:
        rate = Extra_texts
        incl = Tariffs.get(plan)[type_]
    else:
        return print ("Incorrect type")
    extra_used = used - incl
    if extra_used > 0:
        extra = extra_used * rate
    else:
        extra_used = 0
        extra = 0
    return (extra_used, extra)


# Assignment Task 7
# Also prevents some invalid responses
def get_user_info():
    get_tariff = True
    while get_tariff == True:
        plan = input ("Please enter tariff option: ('1' or '2')\t")
        if plan == '1' or plan == '2':
            get_tariff = False
        else:
            print ("Please enter a valid response: ('1' or '2')\t")
    get_minutes = True
    while get_minutes == True:
        minutes = input ("Please enter call time in minutes:\t")
        if minutes.isdigit() == True:
            get_minutes = False
        else:
            print ("Please enter a valid response:\t")    
    get_texts = True
    while get_texts == True:
        texts = input ("Please enter number of texts:\t")
        if texts.isdigit() == True:
            get_texts = False
        else:
            print ("Please enter a valid response:\t")

    user_info = (plan, minutes, texts)
    return user_info

# Assignment Task 8
def extra_call(incl, used):
    extra = float (used) - float (incl)
    if extra > 0:
        cost = extra * Extra_Mins
    else:
        extra = 0
        cost = 0
    return cost

def extra_text(incl, used):
    extra = float (used) - float (incl)
    if extra > 0:
        cost = extra * Extra_texts
    else:
        extra = 0
        cost = 0
    return cost

def print_bill (user_info):
    print ("User's Tariff is :\t{}".format(Tariffs.get(int(user_info[0]))))
    flatrate = Tariffs.get(int (user_info[0]))[0]
    extra_call_cost = extra_call(Tariffs.get(int (user_info[0]))[1], user_info[1])
    extra_text_cost = extra_text(Tariffs.get(int (user_info[0]))[2], user_info[2])
    Total = flatrate + extra_call_cost + extra_text_cost
    print ("Total bill is:\t{:.2f}".format(Total))
    print ("Breakdown:\nFlat rate:\t{:.2f}\nExtra calls charge:\t{:.2f}\nExtra texts charge:\t{:.2f}".format(Total, extra_call_cost, extra_text_cost))

def main():
    Available_tariffs(1, 20, 200, 150)
    Available_tariffs(2, 35, 400, 350)
    print ("Extra phone bills from function 1:\n{}\n{}".format(calc_ext(100, 50, 0.1), calc_ext(50, 100, 0.05)))
    print ("Extra phone bills from function 2:\n{}\n{}".format(calc_ext_2(1, 1, 180), calc_ext_2(1, 2, 180)))

    # Assignment Task 7 & 8
    print_bill(get_user_info())

if __name__ == "__main__":
    main()