def endurance():
    try:
        fuel = int(input("Fuel value : "))
        fuel_consumption = int(input("Fuel Consumption : "))
        endurance = fuel / fuel_consumption
        return(endurance)
    except ZeroDivisionError as err:
        print(f"Fuel consumption can't be 0, Error : {err}")
        return(0)
    except ValueError as err: 
        print(f"Fuel consumption can't be alph, Error : {err}")
        return(0)


if (__name__=="__main__"):
    en = endurance()
    print(f"The endurance calucated is :{en:1.2f}")