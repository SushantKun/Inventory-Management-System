# Import necessary modules
import read
import write
import datetime
import math
import os

# Function to round a number up to the nearest multiple of 5
def round_up_to_nearest_multiple_of_5(number):
    return math.ceil(number / 5) * 5


# Function to handle the equipment rental process
def rent(ac):
    # Initialize variables and lists
    running=True
    assets=[]
    print("")

    # Get customer's name and contact number
    run = True
    while run:
        name_of_user = input("Enter the name of the customer: ")
        if name_of_user.isalpha() == True:
            run = False
        else:
            print("Invalid Name! Please enter valid name !")
            run = True
    # Get customer's contact number
    while running == True:
        try:
            rr = True
            while rr:
                user_num = int(input("Enter the contact number of the customer: "))
                if len(str(user_num)) == 10:
                    rr = False
                else:
                    print("Please enter number equal to 10")
                    rr = True
            # Break out of running once user enters a valid integer
            break
        except:
            print("")
            print("Invalid Input! Please enter only numeric input")
            print("")
    print("")

    # Select equipment to sell and get quantity for each
    while running==True:
        print("")
        print("Here is the list of items that are available for rent")
        read.table(ac)
        print("")

        # Select equipment to sell and get quantity for each
        while running == True:
            try:
                dicision_user = int(input("Enter the ID of the equipment which you want to rent: "))
                if dicision_user <= 0 or dicision_user > len(ac):
                    print("")
                    print("Invalid input! Please enter valid input and try again!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("*Error* Please only enter appropriate numeric value!")
                print("")
        print("")

        # running until user enters a valid integer option
        while running == True:
            try:
                selected_quantity = int(input("Enter the equipment quantity you want to rent: "))
                if selected_quantity <= 0 or selected_quantity > int(ac[dicision_user][3]):
                    print("")
                    print("*Error* Please enter valid input!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("*Error* Please enter only numeric value on the list to choose a quantity!")
                print("")
        print("")

        # extra selected equipment and quantity to list
        assets.append([dicision_user,selected_quantity])
        # Update inventory quantity
        ac[dicision_user][3]=str(int(ac[dicision_user][3])-selected_quantity)

        # Ask if user wants to extra more Equipments
        extra=input("Do you want to rent more items from the list? y/n ").lower()
        if extra=="y":
            continue
        else:
            break
    # Ask if user wants to add more Equipments
    z = 1
    totamt = 0
    for i in assets:
        index = i[0]
        overall_price = int(ac[index][2].replace("$", "")) * int(i[1])
        print(
            str(z) + "\t" + ac[index][0] + read.tab(ac[index][0]) + ac[index][1] + read.tab(ac[index][1]) + "   " + str(
                i[1]) + "\t\t" + ac[index][2] + "\t\t$" + str(overall_price))
        z += 1
        totamt += overall_price



    valid = True
    while valid:
        valid_charge = int(input("\nHow many days is the equipment being rent for ?: "))
        daysbasis = round_up_to_nearest_multiple_of_5(valid_charge)
        currentamt = (daysbasis / 5) - 1
        Extra_Charge = 0
        if valid_charge > daysbasis:
            Extra_Charge = currentamt * totamt
            valid = False
        elif valid_charge <= 0:
            print("*Error* Please enter the valid amount of days in numeric value")
            valid = True
        else:
            Extra_Charge = currentamt * totamt
            valid = False

    # Write updated inventory to file
    write.write(ac)
    print("")
    # Generate and display sale invoice
    print("                       Your invoice is being created...                                      \n")
    print("|*********************************************************************************************|")
    print("\t\t\t\t\t\t Zap's Rental Shop")
    print("\t\t\t\t\t\t Jhumka, Sunsari")
    print("\t\t\t\t\t\t Date: "+ str(datetime.date.today()))
    print("-----------------------------------------------------------------------------------------------")
    print("|                                                                                             |")
    print("Name of the Customer Name: "+name_of_user)
    print("Contact Number of the customer: "+str(user_num))
    print("|                                                                                             |")
    print("-----------------------------------------------------------------------------------------------")
    print("S/N\tName\t\tBrand\t\tQuantity\tUnit Price\tNet Price")
    print("-----------------------------------------------------------------------------------------------")
    z = 1
    totamt = 0
    for i in assets:
        index = i[0]
        overall_price = int(ac[index][2].replace("$", "")) * int(i[1])
        print(
            str(z) + "\t" + ac[index][0] + read.tab(ac[index][0]) + ac[index][1] + read.tab(ac[index][1]) + "   " + str(
                i[1]) + "\t\t  " + ac[index][2] + "\t\t$" + str(overall_price))
        z += 1
        totamt += overall_price
    print("-----------------------------------------------------------------------------------------------------------")
    print("Net Amount: $"+str(totamt))
    if Extra_Charge!=0:
        print("5 Days is Exceeded: $"+str(Extra_Charge))
        print("Charge after exceeding the 5 days limit: ",totamt)
    print("Total Amount: $"+str(totamt + Extra_Charge))
    write.bill_s(ac,assets,name_of_user,user_num,Extra_Charge)
    return valid_charge,totamt

# Function to handle the process of buying assets
def Return(ac):
    running = True
    assets = []

    # Ask for Returner's name
    print("")
    run = True
    while run:
        rentor_name = input("Enter the name of the customer returning the item: ").lower()
        directory_path = os.path.dirname(os.path.abspath(__file__))
        file_extension = ".txt"

        file_to_search = rentor_name + file_extension
        file_path = os.path.join(directory_path, file_to_search)

        if os.path.exists(file_path):
            print("User found on the system.")
            run = False
        else:
            print("User not found on the system.")
            run = True
    howmany = int(input("After How many days did the customer returned the Equipment?: "))



    # running to keep extra assets until user chooses to stop
    while running == True:
        print("")
        print("The list of equipment is shown below ...")
        # Display the list of assets available for purchase
        read.table(ac)
        print("")

        # Get the equipment option from user
        while running == True:
            try:
                dicision_user = int(input("Choose the equipment you want to return by entering its S.N: "))

                if dicision_user <= 0 or dicision_user > len(ac):
                    print("")
                    print("Invalid input! Please enter the correct value!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("*Error* Please enter valid input!")
                print("")
        print("")

        # Get the quantity of the equipment to return from user
        while running == True:
            try:
                selected_quantity = int(input("Enter the quantity of the Equipment to be returned: "))
                if selected_quantity <= 0:
                    print("")
                    print("Sorry the selected item might be low on stock!")
                    print("")
                    continue
                else:
                    break
            except:
                print("")
                print("Sorry an error occured! The item maybe out of stock")
                print("")
        print("")

        # add the equipment and quantity to the list of purchased equipment
        assets.append([dicision_user, selected_quantity])
        # Update the stock quantity of the purchased equipment in the product dictionary
        ac[dicision_user][3] = str(int(ac[dicision_user][3]) + selected_quantity)

        # Ask if user wants to extra more equipments to return
        extra = input("Is there more equipments needed to be Returned? y/n: ").lower()
        if extra == "y":
            continue
        else:
            break

    # Write the updated stock quantity to the equipment file
    write.write(ac)
    print("|*********************************************************************************************|")
    print("                    Kindly wait while we generate your bill...                               \n")
    print("|---------------------------------------------------------------------------------------------|")
    print("\t\t\t\t\t\tZap's Rental Shop")
    print("\t\t\t\t\t\tJhumka, Sunsari")
    print("\t\t\t\t\t\tPurchase Date: " + str(datetime.date.today()))
    print("|---------------------------------------------------------------------------------------------|")
    print("|                                                                                             |")
    print("Returner: " + rentor_name)
    print("|                                                                                             |")
    print("|---------------------------------------------------------------------------------------------|")
    print("S/N\tName\t\t\tBrand\t\t\t\t\tQuantity\t\t\tUnit Price\t\t\tNet Price")
    print("|*********************************************************************************************|")

    z = 1
    totalamount = 0
    # Iterate over the list of purchased assets to generate the invoice
    for i in assets:
        index = i[0]
        # aclculate the net price of the equipments
        overall_price = int(ac[index][2].replace("$", "")) * int(i[1])
        # Display the purchased equipments details in the invoice
        print(str(z) + "\t" + ac[index][0] + read.tab(ac[index][0]) + ac[index][1] + read.tab(ac[index][1]) + "   " +
              str(i[1]) + "\t\t  " + ac[index][2] + "\t\t$" + str(overall_price))
        z += 1
        totalamount += overall_price

    # Display the total amount and gross amount in the invoice
    print("------------------------------------------------------------------------------------------")

    print("Net Amount: $"+str(totalamount))
    print("Gross Amount: $"+str(totalamount))
    dayscount(howmany,totalamount)
    write.invoice_for(ac,assets,rentor_name)
    return howmany


def dayscount(howmany,totalamount):
    days_overdue = howmany
    if days_overdue > 0:
        fine_per_day = 10  # Adjust this value as needed
        overdue_fine = days_overdue * fine_per_day
        print(f"Overdue by {days_overdue} days. Fine: ${overdue_fine}")

    total_price_with_fine = totalamount + overdue_fine
    print("Total price with Fine: $" + str(total_price_with_fine) + "\n")