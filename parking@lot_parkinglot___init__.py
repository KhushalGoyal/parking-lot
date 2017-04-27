import pandas as pd

def creating_parking_lot(totalCars):
    totalCarsList = [1+x for x in range(totalCars)]
    #print(totalCarsList)
    print "Created a parking lot with" ,totalCars,"slots \n"
    df = pd.DataFrame(index=range(0, totalCars), columns=['RegistrationSlotNo','CarNo','Colour'], dtype='float')
    df['RegistrationSlotNo']=totalCarsList
    return  df
