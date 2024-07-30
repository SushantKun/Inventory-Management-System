# Import required modules
import read,operation
from datetime import datetime
now = datetime.now()

#Get current time
current_time = now.strftime("%H:%M:%S")
print("\t \t \t \t \t \t",current_time)

# Welcome message
print("|***************************************************|")
print("|           Welcome to Zap's Rental Shop!           |")
print("|---------------------------------------------------|")
print("|                Jhumka, Sunsari.                   |")
print("|***************************************************|")
print("|   Please select an option from the menu below:    |")
print("|---------------------------------------------------|")

# Main loop
running = True
while running:
    # Read in the list of assets
    assets = read.read()

    # Display the menu options
    print("\nMenu Options:")
    print("|_____________________________________________________________|")
    print("|             1. View available Equipment to Rent             |")
    print("|             2. Rent an Equipment                            |")
    print("|             3. Return an Equipment                          |")
    print("|             4. Exit                                         |")
    print("|_____________________________________________________________|")

    # Get the user's choice
    while True:
        try:
            cust_option = int(input("\nEnter an option to continue: "))
            if cust_option < 1 or cust_option > 4:
                print("Invalid input. Please only enter option that ranges from  1 to 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please only enter option that ranges from  1 to 4.")

    # Execute the chosen option
    if cust_option == 1:
        print("\nHere are all the available items in stock ")
        read.table(assets) # Display available items
    elif cust_option == 2:
        operation.rent(assets) # Call function to handle equipment rental
    elif cust_option == 3:
        operation.Return(assets) # Call function to handle equipment return
    elif cust_option == 4:
        print("\nThank you for visiting Zap's Rental Shop!")
        print("For any information, you can call us at 025-562152")
        running = False # Exit the main loop
    else:
        print("\nInvalid input. Please enter valid input!.")