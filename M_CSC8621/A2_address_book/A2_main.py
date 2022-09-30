import os, time
import A2_person as p

def clrscn(): # Clear terminal
    time.sleep (1)
    os.system("cls")

def invalid_input(): # Invalid input response
    print ("Please enter a valid response.")
    time.sleep (1)

def dob_format (dob): # Concatenates date into all digits
    alldigit = dob[0] + dob[1] + dob[3] + dob[4] + dob[6] + dob[7] + dob[8] + dob[9]
    return alldigit

def main():
    os.system("cls")
    print ("Address Book Program:\n")
    __run_ = True           # Main program loop. If user enters "q", exit.        
    while __run_ == True:   # Main program loop. If user enters "q", exit.
        address_book = list() # Read DATABASE.in and append to list address_book
        f = open("DATABASE.in")
        DATABASE_list = f.readlines()
        count = 0
        for entry_line in DATABASE_list:
            count += 1
            entry_data = entry_line.rstrip().split(":")
            entry = p.Person(entry_data[0], entry_data[1], entry_data[2], entry_data[3], count)
            address_book.append(entry)
        f.close()

        # Main menu
        user_input = input ("Please select an option:\n1. Create new entry.\n2. List all/search by category.\n3. Edit existing entry.\nq. Quit program.\n")
        
        # Option 1 from main menu
        if user_input == "1": # Create new entry
            clrscn
            entry_check = True
            while entry_check == True: # Get entry details
                clrscn()
                
                # Get new entry name
                name_check = True # Prevent special character ":"
                while name_check == True: 
                    new_name = input ("Please enter your name:\n") # Get name in new_name
                    if ":" in new_name: # If ":" exist prompt to remove
                        new_name = input ("Please refrain from using the ':' symbol:\n")
                    else: # No ":", continue
                        name_check = False
                
                # Get new entry address
                add_check = True # Prevent special character ":"
                while add_check == True:
                    new_add = input ("Please enter your address:\n") # Get address in new_add
                    if ":" in new_add: # If ":" exist prompt to remove
                        new_add = input ("Please refrain from using the ':' symbol:\n")
                    else: # No ":", continue
                        add_check = False

                # get new entry phone number    
                num_check = True # Checks for valid phone number
                while num_check == True:
                    new_num = input ("Please enter your phone number (44XXXXXXXXXX):\n") # Get number in new_num
                    if new_num.isdigit() == True and len(new_num) == 12: # Check if all digits and fits number length
                        new_num = int (new_num)
                        num_check = False
                    else:
                        new_num = input ("Please enter a valid number (44XXXXXXXXXX):\n")
                
                dob_check = True # Checks for valid dob
                while dob_check == True:
                    new_dob = input ("Please enter your birthday (dd/mm/yyyy):\n") # Get dob in new_dob
                    dob_dig = dob_format (new_dob)
                    if dob_dig.isdigit() == True and len(new_dob) == 10 and new_dob[2] == "/" and new_dob[5] == "/": # Check if fits format dd/mm/yyyy
                        dob_check = False
                    else:
                        print ("Please enter your birthday in the advised format (dd/mm/yyyy)\n")
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
            count += 1
            entry = p.Person(new_name, new_add, new_num, new_dob, count)
            print ("New entry confirmed.")
            address_book.append(entry) # Append new entry to end of list
            f = open ("DATABASE.in", "a")
            f.write(f"{new_name}:{new_add}:{new_num}:{new_dob}\n") # Update DATABASE.in with new list
            f.close()
            clrscn()
        
        # Option 2 from main menu
        elif user_input == "2": # List all/search by category
            search_check = True
            while search_check == True: # Get search option
                clrscn()
                
                # Search menu
                search_option = input ("What would you like to search for?\n1. List all.\n2. Search by name.\n3. Search by address.\n4. Search by phone number.\n5. Search by birthday.\n6. Cancel.\n")
                
                # Search option 1
                if search_option == "1": # All
                    clrscn()
                    for entry in address_book:
                        print (entry)
                    input ("Press enter to continue.")
                
                # Search option 2
                elif search_option == "2": # By name
                    clrscn()
                    user_search = input ("Please enter your query (name):\n")
                    for entry in address_book:
                        if user_search in entry.name:
                            print (entry)
                    input ("Press enter to continue.")
                
                # Search option 3
                elif search_option == "3": # By address
                    clrscn()
                    user_search = input ("Please enter your query (address):\n")
                    for entry in address_book:
                        if user_search in entry.address:
                            print (entry)
                    input ("Press enter to continue.")
                
                # Search option 4
                elif search_option == "4": # By phone number
                    clrscn()
                    user_search = input ("Please enter your query (phone number):\n")
                    for entry in address_book:
                        if user_search in entry.p_num:
                            print (entry)
                    input ("Press enter to continue.")
                
                # Search option 5
                elif search_option == "5": # By birthday
                    clrscn()
                    user_search = input ("Please enter your query (date/month/year):\n")
                    for entry in address_book:
                        if user_search in entry.dob:
                            print (entry)
                    input ("Press enter to continue.")
                
                # Search option 6
                elif search_option == "6": # Cancel
                    print ("Cancel search.")
                    time.sleep (2)
                    search_check = False
                    clrscn()
                    break
                
                # Search option exception
                else:
                    invalid_input ()

        # Option 3 from main menu
        elif user_input == "3": # Edit existing entry
            clrscn()
            edit_check = True
            while edit_check == True:
                
                # Request edit target (unique roll number)
                user_edit = input ("Please enter roll number of entry to edit:\n")
                roll_num_check = True
                while roll_num_check == True:
                    if user_edit.isdigit() == True and int (user_edit) - 1 < count: # Check if roll number is valid
                        clrscn()

                        # Display edit target
                        print (address_book[int (user_edit) - 1])
                        confirm_check = True
                        while confirm_check == True: # Confirm entry to edit
                            confirm = input ("Is this the entry to edit? (y/n)\n")
                            
                            # Edit entry
                            if confirm.upper() == "Y":
                                clrscn()
                                entry_check = True
                                # Identical to new contact detail acquisition
                                while entry_check == True: # Get entry details
                                    clrscn()
                                    name_check = True # Prevent special character ":"
                                    while name_check == True:
                                        new_name = input ("Please enter your name:\n") # Get name in new_name
                                        if ":" in new_name:
                                            new_name = input ("Please refrain from using the ':' symbol:\n")
                                        else:
                                            name_check = False
                                    
                                    add_check = True # Prevent special character ":"
                                    while add_check == True:
                                        new_add = input ("Please enter your address:\n") # Get address in new_add
                                        if ":" in new_add:
                                            new_add = input ("Please refrain from using the ':' symbol:\n")
                                        else:
                                            add_check = False
                                        
                                    num_check = True # Checks for valid phone number
                                    while num_check == True:
                                        new_num = input ("Please enter your phone number (44XXXXXXXXXX):\n") # Get number in new_num
                                        if new_num.isdigit() == True and len(new_num) == 12:
                                            new_num = int (new_num)
                                            num_check = False
                                        else:
                                            new_num = input ("Please enter a valid number (44XXXXXXXXXX):\n")
                                    
                                    dob_check = True # Checks for valid dob
                                    while dob_check == True:
                                        new_dob = input ("Please enter your birthday (dd/mm/yyyy):\n") # Get dob in new_dob
                                        dob_dig = dob_format (new_dob)
                                        if dob_dig.isdigit() == True and len(new_dob) == 10 and new_dob[2] == "/" and new_dob[5] == "/":
                                            dob_check = False
                                        else:
                                            print ("Please enter your birthday in the advised format (dd/mm/yyyy)\n")
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
                                
                                # Edits entry in address_book list
                                address_book[int (user_edit) - 1] = p.Person(new_name, new_add, new_num, new_dob, int(user_edit) - 1)
                                f = open ("DATABASE.in", "w")
                                
                                # Overwrite DATABASE.in with new list
                                for entry in address_book:
                                    f.write(f"{entry.name}:{entry.address}:{entry.p_num}:{entry.dob}\n")
                                f.close()

                                # Exit all while loops to main menu
                                confirm_check = False
                                roll_num_check = False
                                edit_check = False
                                clrscn()
                            
                            # Wrong entry
                            elif confirm.upper() == "N":
                                
                                # Exit while loop to get entry target
                                roll_num_check = False
                                break
                            
                            # Invalid entry target confirm response
                            else:
                                print ("Please enter a valid response.\n")
                    
                    # Invalid roll number response
                    else:
                        user_edit = input ("Please enter a valid roll number.\n")

        # "q" from main menu
        elif user_input.upper() == "Q": # Quit program
            __run_ = False
            clrscn ()
            break

        # Main menu exception
        else:
            invalid_input ()
    
    input ("Closing address book program. Press enter to close.")
    clrscn()

if __name__ == "__main__":
    main()