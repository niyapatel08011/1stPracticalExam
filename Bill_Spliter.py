
while True:
    print("WELCOME TO BLL SPLITTER APP..!")
 
    print("")
 
    bill=float(input("Enter Total Bill Amount:- "))
    people=int(input("Enter Number Of People:- "))
    tip=float(input("Enter tip percentage(0/5/10/15/20):- "))
    print("")

    Tip_amount=(tip/100)*bill    
    print(f"Tip Amount:- {Tip_amount}")
    

    Total_bill=bill+Tip_amount
    print(f"Total Bill(with tip):- {Total_bill}")
    

    per_person=Total_bill/people
    print(f"Per Person:- {per_person}")
    print("")
        
    again=input("Would you like to calculate another bill? (yes/no) :")
    print("")
    if again.lower()!="yes":
      print("THANK YOU! for using Bill Splitter App. ")
      break
    continue
    
    

    

  