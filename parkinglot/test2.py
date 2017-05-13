import parkinglot

def main():
    stack = []
    totalCars = int(input("For how many Cars you want to create a parking space \n"))
    carslot = parkinglot.creating_parking_lot(totalCars)
    print carslot.to_string(index=False)," \n",
    count = 1
    while True:
        print "\n"
        value = int(input(
            "To park your vehicle press 1 \n"
            "To leave from the parking lot press 2 \n"
            "To See the status press 3 \n"
            "To access the database press 4 \n"
            "To Exit press 5 \n"))
        if value == 1:
            platenumber, colour = (raw_input("To park your Vehicle enter your Car Plate number and Colour \n")).split(" ")
            if len(stack)==0:
                carslot.loc[carslot['RegistrationSlotNo'] == count, 'CarNo'] = platenumber
                carslot.loc[carslot['RegistrationSlotNo'] == count, 'Colour'] = colour
                #print count, "^^^^^^^^^"
                if count > totalCars:
                    print "Sorry No More Space \n"
                    break
                count += 1
            else:
                val = stack.pop()
                carslot.loc[carslot['RegistrationSlotNo'] == val, 'CarNo'] = platenumber
                carslot.loc[carslot['RegistrationSlotNo'] == val, 'Colour'] = colour
                if count > totalCars:
                    print "Sorry No More Space \n"
            #print carslot.to_string(index=False)," \n"
        elif value == 2:
            #print carslot.to_string(index=False)," \n"
            slot = int(raw_input("Enter your Registration Slot number :\n"))
            stack.append(slot)
            carslot.loc[carslot['RegistrationSlotNo'] == slot, 'CarNo'] = "Na"
            carslot.loc[carslot['RegistrationSlotNo'] == slot, 'Colour'] = "Na"
            #print carslot, "\n^^^^^^^^^"
            #print stack
        elif value == 3:
            print carslot.to_string(index=False)," \n"
        elif value == 4:
            print carslot.to_string(index=False),"\n"
            while True:
                data = int(input("To get Registration Slot Number using colour press 1 \n"
                                 "To get Car Number using colour press 2 \n"
                                "To get Car Number with Registration number press 3 \n"))
                if data == 1:
                    col = raw_input("Enter your car colour :\n")
                    pdata = carslot[carslot.Colour == col]
                    print "Your Registration Slot Number : ",pdata.RegistrationSlotNo.to_string(index=False), "\n"
                    break
                elif data == 2:
                    col = raw_input("Enter your car colour :\n")
                    pdata1 = carslot[carslot.Colour == col]
                    print "Your Car Number : ",pdata1.CarNo.to_string(index=False), "\n", "\n"
                    break
                elif data == 3:
                    try:
                        regnum = raw_input("Enter your registration number :\n")
                        padata2 = carslot[carslot.RegistrationSlotNo == regnum]
                        if padata2.RegistrationSlotNo == regnum:
                            print "Your Car Number : ",padata2.CarNo.to_string(index=False), "\n"
                    except ValueError:
                        print "Not Fount", "\n"
        elif value == 5:
            break
