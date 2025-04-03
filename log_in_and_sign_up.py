import admin as ad


account = {}

def login():
    print("Please log in to your Account ")
    email = input("Enter your email here: ")
    password = input("Enter your password here: ")
    if email in account and account[email]['password'] == password:
        print("Log in is successfully ")
        return email
    else:
        print("Invalid username or password. Please try again.")
        return None
    
def signup():
    email = input("Enter your desire email: ").strip()
    if email in account:
        print("This email is Already owned by other ")
    else:
        password = input("Enter your password: ").strip()
        account[email] = {'password': password}
        print("Account created successfully!")

    

def loginasbarber():
    print("Please log in to your Account ")
    barber_email = input("Enter your email here: ").strip()
    password = input("Enter your password here: ").strip()
    if barber_email in account and account[barber_email]['password'] == password:
        print("Log in is successfully ")
        return barber_email
    else:
        print("Invalid username or password. Please try again.")
        return None
    


while True:
    print("Welcome to our Booking a Barbers/shop ")
    print("1.Log in")
    print("2.Sign up")
    print("3.Log in as barber")

    choose = (input("Enter the number you Choose: ")).strip()
    if choose == '1':
        login()
    elif choose == '2':
        signup()
    elif choose == '3':
        loginasbarber()
    elif choose == 'admin':
        attempts = 0
        while attempts < 3:
                adm= input("Enter the password of admin: ").strip().lower()
                if adm == ad.admin_password:
                    ad.admin()
                    break
                
                elif adm != ad.admin_password:
                    print("wrong password pls try again")
                    attempts+=1
        else:
            print("Too many failed attempts. Returning to the main menu.")            
                              
    else:
        print("Invalid choice")
    