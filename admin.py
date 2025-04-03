barberaccount = {}
admin_password = 'superadmin'

def create_accBarber():
    barberuser = input("Enter the username of the barber: ").strip()
    
    if barberuser in barberaccount:
        print("This user is already registered.")
    else:
        barbername = input("Enter the name of the barber: ").strip()
        barberpassword = input("Enter the password of the barber: ").strip()
        
     
        barberaccount[barberuser] = {
            "name": barbername,
            "password": barberpassword
        }
        
        print(f"Barber {barbername} added successfully!")

def delete_accBarber():
    barberuser = input("Enter the username of the barber to delete: ").strip()
    
    if barberuser in barberaccount:
        del barberaccount[barberuser]
        print(f"Barber {barberuser} deleted successfully!")
    else:
        print("Barber not found.")

def manbar():  
    while True:
        print("\nManage Barbers")
        print("1. Add/Create a barber account")
        print("2. Delete a barber account")
        print("3. Back to Admin Menu")

        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            create_accBarber()
        elif choice == '2':
            delete_accBarber()
        elif choice == '3':
            return  
        else:
            print("Invalid choice, please try again.")

def mansched():  
    print("The schedule management system is coming soon...")

def admin(): 
    print("Welcome back, Admin!\n")
    
    while True:
        print("\nAdmin Menu")
        print("1. Manage Barbers")
        print("2. Manage Schedule")
        print("3. Exit to Main Menu")

        choose = input("Enter your choice: ").strip()
        
        if choose == '1':
            manbar()
        elif choose == '2':
            mansched()
        elif choose == '3':
            return  
        else:
            print("Invalid choice, please try again.")
