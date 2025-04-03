admin_password = 'superadmin'


def admin():
    def manbar():#manbar ay manage of barber
        print("The manage of barber is comming soon ")

    def mansched():#mansched ay manage of barber
        print("The manage of schedule is comming soon ")

    print("welcome back admin\n")
    while True:
        print(" 1.manage barber \n 2.manage schedule \n 10. exit")
        choose = input("enter your operator: ").strip()
        if choose == '1':
            manbar()
        elif choose == '2':
            mansched()
        elif choose == '10':
            return 
        else:
            print("invalid choice pls try again")


