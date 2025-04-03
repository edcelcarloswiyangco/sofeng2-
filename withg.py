# Dictionary to store accounts and their car details
accounts = {}

def create_account():
    """Create a new account."""
    print("\n=== Create Account ===")
    username = input("Enter a username: ").strip()
    if username in accounts:
        print("This username already exists. Please choose a different one.")
    else:
        password = input("Enter a password: ").strip()
        accounts[username] = {'password': password, 'car_details': {}}
        print("Account created successfully!")

def login():
    """Log in to the system."""
    print("\n=== Login ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in accounts and accounts[username]['password'] == password:
        print("Login successful!")
        return username  # Return the username of the logged-in account
    else:
        print("Invalid username or password. Please try again.")
        return None

def car_name(user):
    """Register a new car with its color."""
    carname = input("Enter the car name to register: ").strip()
    if carname in accounts[user]['car_details']:
        print(f"The car brand '{carname}' is already registered.")
    else:
        color = input("Choose the color you want: ").strip()
        accounts[user]['car_details'][carname] = {'color': color}
        print(f"Car '{carname}' with color '{color}' has been registered.")
        print(accounts[user]['car_details'])

def add(user):
    """Update the color of an existing car."""
    carname = input("Enter the car name to update: ").strip()
    if carname in accounts[user]['car_details']:
        color = input("Choose the new color you want: ").strip()
        accounts[user]['car_details'][carname]['color'] = color
        print(f"The color of car '{carname}' has been updated to '{color}'.")
        print(accounts[user]['car_details'])
    else:
        print(f"The car '{carname}' is not registered. Please register it first.")

def show(user):
    """Show all registered cars for the logged-in user."""
    if accounts[user]['car_details']:
        print("Your registered cars:")
        for carname, details in accounts[user]['car_details'].items():
            print(f"- {carname}: {details}")
    else:
        print("No cars registered yet.")

def show_specific(user):
    """Show details of a specific car brand."""
    carname = input("Enter the car name to view details: ").strip()
    if carname in accounts[user]['car_details']:
        print(f"Details of '{carname}': {accounts[user]['car_details'][carname]}")
    else:
        print(f"The car brand '{carname}' is not registered.")


while True:
    print("\n=== Welcome to the Car Registration System ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ").strip()

    if choice == '1':
        create_account()
    elif choice == '2':
        user = login()
        if user:
            # Once logged in, show the car registration system
            while True:
                print("\nChoose an option:")
                print("1. Register a new car")
                print("2. Update car color")
                print("3. Show all cars")
                print("4. Show details of a specific car")
                print("5. Logout")
                choose = input("Enter your choice (1-5): ").strip()
                
                if choose == '1':
                    car_name(user)
                elif choose == '2':
                    add(user)
                elif choose == '3':
                    show(user)
                elif choose == '4':
                    show_specific(user)
                elif choose == '5':
                    print("Logged out successfully!")
                    break
                elif choose == '10':
                    x = input("enter: ")
                    if x == '1':
                        print(accounts)
                    else:
                        break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
    elif choice == '3':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

 