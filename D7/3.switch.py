argument = int (input("Enter 0 or 1"))

match argument :
    case 0 :
        print(0)
    case 1 :
        print(1)
    case _ : 
        print("Wrong input")        