from LOL_Info import LOL_Info

if __name__ == '__main__':
    LOL = LOL_Info()
    while True:
        menu1=input("Enter a game to start"+'\n'+"Available: LOL"+'\n')
        if menu1 == "LOL" or menu1=="lol":
            while True:
                LOL.start_Stats()
                LOL.get_info()
                menu2=input("¿Do you want to get stats from another account?"+'\n'+"enter y(yes) or n(no) to continue"'\n')
                if menu2=="n":
                    break
        else:
            break
    input("Press any key to continue"+'\n')
    
