# This module handles all gui elements of my program

# Show menu
def show_menu():
    print(
    '''
    1) Enter Sale(s) Information
    2) Display Sale(s) Information
    3) Show Total Profit
    4) Add New App to records
    5) Find Top Selling App
    6) Delete Sale by ID
    q) Quit
    '''
    )

# Get user choice
def get_choice():
    choice = input("Select menu option: ")
    return choice

# Handles if the user would like to continue the program
def get_user_continue():
    choice = input("Would you like to continue? (y/n)")
    return choice

# Get information on new sale and return the in app purchase object
def create_new_sale(app_name_list):
    while True: # Loop until an app that exists is typed in
        if len(app_name_list) == 0:
            print("No apps exist yet please enter one in the 'Enter app info' menu")
            return None
        print("Your current apps: ")
        for name in app_name_list:
            print("App: " + name)
        app_name = input("Enter the name of the app: ").lower()
        if app_name in app_name_list:
            break # Exit loop
        else:
            print("That app is not on record yet please enter it on the 'Enter app info' menu")
            return None


    purchase_name = input("Enter the in app item purchased: ").lower()
    state = input("Enter the name of the state where the purchase was made: ")
    price = input("Enter the price of each purchase: ")
    amount = input("Enter the amount of purchased items: ")
    date = input("Enter the date of the purchase(s) (mm/dd/yyyy): ")
    sale_percent = input("Enter the sale percentage off? (Enter 0 if not on sale): ")
    return [app_name, purchase_name, price, amount, date, state, sale_percent]

# Get information on new app information
def create_new_app():
    app_name = input("Enter the name of the app: ")

# Get list of purchases based on
def get_query_information():
    print(
    '''
    Options to search for:
    App Name
    Purchase Name
    Date
    State
    '''
    )
    column = input("What would you like to search the records for? ").lower()
    value = input("Search for what " + column + "? ")
    return [column, value] # Return the user entered search

# Show information based on list of purchases
def show_information(in_app_purchase_list):
    total_sales = 0 # Track amount of sales
    total_earnings = 0 # Track total earnings
    for purchase in in_app_purchase_list:
        total_sales += purchase.amount
        total_earnings += purchase.amount * purchase.price * ((100 - int(purchase.percent_off)) / 100)
        print(purchase)
    print("Total Sales: " + str(total_sales))
    print("Total Earnings: " + str(total_earnings))

# Create new app menu
def new_app():
    app_name = input("Enter the name of the new app to track: ").lower()
    app_items = input("Enter a list of in app purchases (separate each with ;): ")
    return [app_name, app_items]

# Calculate top selling app
def top_selling_app(db_query):
    top_selling_dictionary = {}
    for item in db_query:
        if item.app_name not in top_selling_dictionary.keys():
            top_selling_dictionary.update({item.app_name: item.amount * item.price})
        else:
            value = top_selling_dictionary[item.app_name]
            top_selling_dictionary.update({item.app_name: value + item.amount * item.price})
    top_seller = ['None', -1]
    for app in top_selling_dictionary.keys():
        if top_selling_dictionary[app] > top_seller[1]:
            top_seller = [app, top_selling_dictionary[app]]
    print("Your top seller is: " + str(top_seller[0]) + " making $" + str(top_seller[1]))

# Get id to Delete
def get_id_delete(id_list, all_sales):
    for item in all_sales:
        print(item)
    user_input = None
    try:
        user_input = int(input("Enter the id to delete (Enter -1 to cancel): "))
    except(NumberFormatException):
        print("Please enter a valid integer")
    if user_input == -1:
        return None
    else:
        if user_input in id_list:
            return user_input
        else:
            return None

# Handle printing messages
def message(message):
    print(message)
