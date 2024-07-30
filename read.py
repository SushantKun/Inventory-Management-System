#Naming the function read
def read():
    try:
        with open('equipments.txt', 'r') as file:
            ac = {}
            for line_num, line in enumerate(file, start=1):
                line = line.strip()  # remove leading/trailing whitespace
                if not line:  # skip empty lines
                    continue
                parts = line.split(', ')
                if len(parts) != 4:  # skip lines with invalid format
                    print(f"Skipping line {line_num}: invalid format ({line})")
                    continue
                ac[line_num] = parts
    except FileNotFoundError:
        print("equipments.txt not found")
        ac = {}
    return ac

def tab(str_val):
    """Returns tab characters based on the length of the given string"""
    if len(str_val) <= 8:
        return "\t\t"
    else:
        return "\t"


def table(product_data):
    """Displays a formatted table of product data"""
    print(
        "|---------------------------------------------------------------------------------|")
    print("|S/N. \t Name \t\t\tBrand Name  \t Price \t\t\tQuantity          |")
    print(
        "|---------------------------------------------------------------------------------|")

    # Loop through each product in the product_data dictionary
    for key, values in product_data.items():
        print(f"{key}.   {values[0]} \t\t {values[1]} \t\t {values[2]} \t\t {values[3]}")
        print(
            "|-----------------------------------------------------------------------------|")
