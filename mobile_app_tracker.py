# Main module of my program that handles all logic
import gui, database
from in_app_purchase import IAP
from app import App

# This function handles the users choice
def user_choice():
    chosen = False # Tracks if choice is handled
    while chosen != True:
        # Get menu option choice
        choice = gui.get_choice()
        # Handle menu option choice
        chosen = handle_menu_choice(choice)

# This function handles the menu option choice
def handle_menu_choice(choice):
    # Enter sale(s) information
    if choice == '1':
        iap_list = gui.create_new_sale(database.app_names())
        if iap_list != None:
            new_purchase = IAP(app_name=iap_list[0], purchase_name=iap_list[1], price=iap_list[2], amount=iap_list[3], date=iap_list[4], purchase_state=iap_list[5], percent_off=iap_list[6])
            database.add_in_app_purchase(new_purchase) # Send to db
    # Display Sale(s) Information
    elif choice == '2':
        # Get query infor and send it to get purchase list
        in_app_purchase_list = database.get_purchase_list(gui.get_query_information())
        gui.show_information(in_app_purchase_list) # Show information
    # Display total money made
    elif choice == '3':
        gui.show_information(database.get_all_sales())
    # Enter new app info
    elif choice =='4':
        new_app = gui.new_app()
        app = App(app_name=new_app[0], items=new_app[1])
        database.add_new_app(app)
    # Find top selling app
    elif choice =='5':
        gui.top_selling_app(database.get_all_sales())
    elif choice =='6':
        id_to_delete = gui.get_id_delete(database.list_of_ids(), database.get_all_sales())
        if id_to_delete != None and id_to_delete != -1:
            database.delete_by_id(id_to_delete)
        elif id_to_delete == None:
            gui.message("Not deleting anything.")
        else:
            gui.message("That ID does not exist")
    elif choice == 'q':
        True
    else:
        gui.message("Please select a valid menu option.")
        return False # Choice not handled
    return True



# Main function
def main():
    while True:
        # Show main menu
        gui.show_menu()
        user_choice()
        # Check if the user wants to continue
        choice = gui.get_user_continue()
        if choice.lower() == 'n':
            break # Stop loop
    gui.message("Exiting program.")


# Run
if __name__ == '__main__':
    main()
