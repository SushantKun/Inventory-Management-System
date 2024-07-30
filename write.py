import read, datetime


# Function to get the current date and time as a string
def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    return year + "_" + month + "_" + day


# Function to write the equipment data to a file
def write(ac):
    file = open('equipments.txt', 'w')
    for i in ac.values():
        file.write(", ".join(i) + "\n")
    file.close()


# Function to generate a returning invoice
def invoice_for(ac, assets, rentor_name):
    # Generate the filename for the invoice based on the rentor name and current date and time
    filename = rentor_name + "_" + date() + ".txt"
    file = open(filename, "w")
    # Write the header information to the file
    file.write("Return Bill\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t\tZap's Rental Shop\n")
    file.write("\t\t\t\t\t\tKathmandu, Nepal\n")
    file.write("\t\t\t\t\t\tDate: " + str(datetime.date.today()) + "\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Rentor: " + rentor_name + "\n")
    file.write("\n")
    # Write the table header to the file
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("S/N \tName \t\t Brand \t\tQuantity \t Unit Price\t Net Price\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    z = 1
    totalamt = 0
    # Loop through each item in the assets list and write the equipment information to the file
    for i in assets:
        index = i[0]
        overall_price = int(ac[index][2].replace("$", "")) * int(i[1])
        file.write(str(z) + read.tab(ac[index][0]) + ac[index][0] + read.tab(ac[index][0]) + ac[index][1] + read.tab(
            ac[index][1]) + "   " + str(i[1]) + "\t\t  " + ac[index][2] + "\t\t $" + str(overall_price) + "\n")
        z += 1
        totalamt += overall_price
    # Write the footer information to the file
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("Net Amount: $" + str(totalamt) + "\n")
    file.write("Gross Amount: $" + str(totalamt) + "\n")
    file.close()


# Function to generate a rent invoice
def bill_s(ac, assets, name_of_user, user_num, Extra_Charge):
    # Generate the filename for the invoice based on the customer name and current date and time
    filename = name_of_user + ".txt"
    file = open(filename, "w")
    # Write the header information to the file
    file.write("Rent Bill\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("\t\t\t\t\t\tZap's Rental Shop\n")
    file.write("\t\t\t\t\t\tJhumka, Sunsari\n")
    file.write("\t\t\t\tDate: " + str(datetime.date.today()) + "\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("\n")
    file.write("Customer Name: " + name_of_user + "\n")
    file.write("Contact Number: " + str(user_num) + "\n")
    file.write("\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("S/N\t Name\t\tBrand\t\tQuantity\tUnit Price\tNet Price\n")
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    z = 1
    totalamt = 0
    for i in assets:
        index = i[0]
        overall_price = int(ac[index][2].replace("$", "")) * int(i[1])
        file.write(str(z) + read.tab(ac[index][0]) + ac[index][0] + read.tab(ac[index][0]) + ac[index][1] + read.tab(
            ac[index][1]) + "   " + str(i[1]) + "\t\t  " + ac[index][2] + "\t\t $" + str(overall_price) + "\n")
        z += 1
        totalamt += overall_price
    file.write(
        "------------------------------------------------------------------------------------------------------------\n")
    file.write("Net Amount: $" + str(totalamt) + "\n")
    if Extra_Charge != 0:
        file.write("Extra Charge: $" + str(Extra_Charge) + "\n")
    file.write("Total Amount: $" + str(totalamt + Extra_Charge) + "\n")
    file.close()
