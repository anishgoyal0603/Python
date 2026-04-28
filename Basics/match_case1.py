color = input("enter color : ")

match color:
    case "Green":
        print("Go")
        #break if we use break statement in match case it shows error
    case "Yellow":
        print("Look")
    case "Red":
        print("Stop")    
    case _:
        print("Wrong color!")        

 
