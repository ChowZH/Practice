import os
import time
import A2_person as pers

def clrscn ():
    # Pauses for 1 sec then clears terminal
    time.sleep (1)
    os.system ("cls")

def dob_format (dob):
    # Concatenates date into all digits
    alldigit = dob[0] + dob[1] + dob[3] + dob[4] + dob[6] + dob[7] + dob[8] + dob[9]
    return alldigit

def main():
    # main program loop (while __run_ true: run, otherwise end program)
    __run_ = True
    while __run_ == True:
        # get user input on desired function:
        # 1. Create new entry
        # 2. List all/Search by category
        # 3. Edit old entry
        clrscn()
        # Get initial user input for desired function
        __get_input = True
        while __get_input == True:
            __user_input = input ("Please select an option:\n1. Create new entry.\n2. List all/search by category.\n3. Edit existing entry.\n4. Cancel.\n")
            
            # Create new entry
            if __user_input == "1":
                entry_check = True
                while entry_check == True:
                    clrscn()
                    # Get entry details
                    new_name = input ("Please enter your name:\n")
                    new_add = input ("Please enter your address:\n")
                    num_check = True # Checks for valid phone number
                    while num_check == True:
                        new_num = input ("Please enter your phone number (44XXXXXXXXXX):\n")
                        if new_num.isdigit() == True and len(new_num) == 12:
                            new_num = int (new_num)
                            num_check = False
                        else:
                            new_num = input ("Please enter a valid number (44XXXXXXXXXX):\n")
                    dob_check = True # Checks for valid dob
                    while dob_check == True:
                        new_dob = input ("Please enter your birthday (dd/mm/yyyy):\n")
                        dob_dig = dob_format (new_dob)
                        if dob_dig.isdigit() == True and len(new_dob) == 10 and new_dob[2] == "/" and new_dob[5] == "/":
                            dob_check = False
                        else:
                            new_dob = input ("Please enter your birthday in the advised format (dd/mm/yyyy):\n")
                    clrscn()
                    print("Please check the entered details:\nName:\t\t{}\nAddress:\t{}\nPhone Num:\t{}\nBirthday:\t{}\n" .format(new_name, new_add, new_num, new_dob))
                    check_query_validity = True # Checks if input is "y/n", if not, repeats
                    while check_query_validity == True:
                        check_query = input ("Are the details correct? (y/n)\t")
                        if check_query.upper() == "Y":
                            check_query_validity = False
                            entry_check = False
                        elif check_query.upper() == "N":
                            check_query_validity = False
                            entry_check = True
                        else:
                            check_query_validity = True
                            check_query = input ("Please enter a valid response.\nAre the details correct? (y/n)\t")

                f = open ("DATABASE.in", "r")
                count = 1
                for _ in f.readlines():
                    if "ID:" in _:
                        count += 1
                f.close()
                
                f = open ("DATABASE.in", "a+")
                f.write ("Name:\t\t{}\nAddress:\t{}\nPhoneNum:\t{}\nBirthday:\t{}\nID:\t\t\t{}\n\n".format(new_name, new_add, new_num, new_dob, count))
                print ("ID for user {} is :\t\t{}".format(new_name, count))
                f.close()

                time.sleep (2)
                __get_input = False
            
            # List all/Search by category
            elif __user_input == "2":
                # Get search option
                search_check = True
                while search_check == True:
                    clrscn()
                    search_option = input ("What would you like to search for?\n1. List all.\n2. Search by name.\n3. Search by address.\n4. Search by phone number.\n5. Search by birthday.\n6. Search by ID.\n7. Cancel.\n") 
                    if search_option == "1": # List all
                        f = open ("DATABASE.in", "r")
                        for _ in f.readlines():
                            if "Name:" in _:
                                for word in _.split():
                                    print ("{}\t" .format(word), end = "")
                                print ("\r")
                            elif "PhoneNum:" in _:
                                for word in _.split():
                                    print ("{}\t" .format(word), end = "")
                                print ("\r")
                            elif "ID:" in _:
                                for word in _.split():
                                    print ("{}\t" .format(word), end = "")
                                print ("\r")
                        f.close()
                        input ("Press anything to continue:\n")
                        search_check = False
                    elif search_option == "2": # By name
                        search_name = input ("Please enter the name:\n")
                        f = open ("DATABASE.in", "r")
                        for _ in f.readlines():
                            if search_name in _:
                                for word in _.split():
                                    print ("{}\t" .format(word), end = "")
                                print ("\r")
                        f.close()
                        input ("Press anything to continue:\n")
                        search_check = False
                    elif search_option == "3": # By address
                        search_add = input ("Please enter the address:\n")
                        f = open ("DATABASE.in", "r")
                        for _ in f.readlines():
                            if search_add in _:
                                for word in _.split():
                                    print ("{}\t" .format(word), end = "")
                                print ("\r")
                        f.close()
                        input ("Press anything to continue:\n")
                        search_check = False
                    elif search_option == "4": # By phone number
                        search_num = input ("Please enter the phone number:\n")
                        f = open ("DATABASE.in", "r")
                        for _ in f.readlines():
                            if search_num in _:
                                for word in _.split():
                                    print ("{}\t" .format(word), end = "")
                                print ("\r")
                        f.close()
                        input ("Press anything to continue:\n")
                        search_check = False
                    elif search_option == "5": # By birthday
                        f = open ("DATABASE.in", "r")
                        f.close()
                        input ("Press anything to continue:\n")
                        search_check = False
                    elif search_option == "6": # By ID
                        f = open ("DATABASE.in", "r")
                        f.close()
                        input ("Press anything to continue:\n")
                        search_check = False
                    elif search_option == "7": # Cancel
                        search_check = False
                        clrscn()
                        exit()
                    else: # Invalid response
                        search_option = input("Please enter a valid response.\n")
                        search_check = True
                __get_input = False
            # Edit old entry
            elif __user_input == "3":
                # open file to write
                f = open ("DATABASE.in", "w")
                
                
                # close file
                f.close()
                print ("Option 3.")
                __get_input = False
            elif __user_input == "4":
                clrscn()
                exit()
            else:
                print ("Invalid.")
                __get_input = True
            clrscn()

        # Main loop repeat check
        __get_input = True
        while __get_input == True:
            __user_input = input ("no more? 1, 2\n")
            # Repeat main loop
            if __user_input == "1":
                print ("Rerun.")
                __run_ = True
                __get_input = False
            # Exit main loop
            elif __user_input == "2":
                print ("End.")
                __run_ = False
                __get_input = False
            # Input check
            else:
                print ("Invalid.")
                __get_input = True
            clrscn()

if __name__ == "__main__":
    main()