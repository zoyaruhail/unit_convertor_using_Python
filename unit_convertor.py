def unit_convertor():
    try:
        print("||Welcome To Unit Convertor||")
        while True:
            #Main Menu
            main_menu = int(input("Main Menu\n1. Length/Distance \n2. Weight/Mass \n3. Temperature \n4. Speed \n5. Time \n6. Area \n7. Volume \n8. Energy \n9. Pressure \n10. Digital Storage \n11. To exit \nChoose theme in which you want to convert the units: "))
            if main_menu == 1: #Length convertor
                print("||Welcome to Length/Distance Section||")
                try:
                    while True:
                        length = int(input("Length Menu \n1. Kilometeres(Km) to Miles \n2. Miles to Kilometers(Km) \n3. Meters to Feet(ft) \n4. feet(ft) to Meters \n5. Back to Main Menu \nChoose from the Length Menu: "))
                        if length == 1:
                            km = float(input("Kilometers:- "))
                            miles = km*0.621371
                            print(f"{km}Km is {miles}Miles")
                        elif length == 2:
                            miles = float(input("Miles:- "))
                            km = miles*1.60934
                            print(f"{miles}Miles is {km}Km")
                        elif length == 3:
                            meter = float(input("Meters:- "))
                            feet = meter*3.28084
                            print(f"{meter}m is {feet}ft")
                        elif length == 4:
                            feet = float(input("Feets:- "))
                            meter = feet*0.3048
                            print(f"{feet}ft is {meter}m")
                        elif length == 5:
                            print("Returning back to Main Menu")
                            break
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 2: #weight Convertor
                print("||Welcome to Weight/Mass Section||")
                try:
                    while True:
                        weight = int(input("Weight Menu \n1. Kilogram(Kg) to Pounds \n2. Pounds to Kilogram(kg) \n3. Gram to Ounces \n4. Ounces to Grams \n5. Back to Main Menu \nChoose from the Weight Menu: "))
                        if weight == 1:
                            kg = float(input("Kilograms:- "))
                            pounds = kg*2.20462
                            print(f"{kg}Kg is {pounds}Pounds")
                        elif weight == 2:
                            pounds = float(input("Pounds:- "))
                            kg = pounds*0.453592
                            print(f"{pounds}Pounds is {kg}Kg")
                        elif weight == 3:
                            gram = float(input("Grams:- "))
                            ounces = gram*0.035274
                            print(f"{gram}g is {ounces}Ounces")
                        elif weight == 4:
                            ounces = float(input("Ounces:- "))
                            gram = ounces*28.3495
                            print(f"{ounces}Ounces is {gram}g")
                        elif weight == 5:
                            print("Returning back to Main Menu")
                            break
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 3: #temperature Convertor
                print("||Welcome to Temperature Section||")
                try:
                    while True:
                        temp = int(input("Temperature Menu \n1. Celcius to Fehrenheit \n2. Fehrenheit to Celcius \n3. Celcius to Kelvin \n4. Kelvin to Celcius \n5. Back to Main Menu \nChoose from the Temperature Menu: "))
                        if temp == 1:
                            c = float(input("Celcius:- "))
                            f = (c*(9/5))+32
                            print(f"{c}Celcius is {f}Fehrenheit")
                        elif temp == 2:
                            f = float(input("Fehrenheit:- "))
                            c = (f-32)*(5/9)
                            print(f"{f}Fehrenheit is {c}Celcius")
                        elif temp == 3:
                            c = float(input("Celcius:- "))
                            k = c+273.15
                            print(f"{c}Celcius is {k}Kelvin")
                        elif temp == 4:
                            k = float(input("Kelvin:- "))
                            c = k-273.15
                            print(f"{k}Kelvin is {c}Celcius")
                        elif temp == 5:
                            print("Returning back to Main Menu")
                            break
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 4: #Speed Convertor
                print("||Welcome to Speed Section||")
                try:
                    while True:
                        speed = int(input("Speed Menu \n1. Kilometer per hour (km/h) to Miles per hour (mph) \n2. Miles per hour (mph) to Kilometer per hour (km/h) \n3. Meter per second (m/s) to Kilometer per hour (km/h) \n4. Back to Main Menu \nChoose from the speed Menu: "))
                        if speed == 1:
                            kmh = float(input("Kilometers per hour:- "))
                            mph = kmh*0.621371
                            print(f"{kmh}Km/h is {mph}mph")
                        elif speed == 2:
                            mph = float(input("Miles per hour:- "))
                            kmh = mph*1.60934
                            print(f"{mph}mph is {kmh}Km/h")
                        elif speed == 3:
                            mps = float(input("Meter per second:- "))
                            kmh = mps*3.6
                            print(f"{mps}m/s is {kmh}kmh")
                        elif speed == 4:
                            print("Returning back to Main Menu")
                            break                            
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 5: #Time Convertor
                print("||Welcome to Time Section||")
                try:
                    while True:
                        time = int(input("Time Menu \n1. Seconds to Minutes \n2. Minutes to Hours \n3. Back to Main Menu \nChoose from the speed Menu: "))
                        if time == 1:
                            s = float(input("Seconds:- "))
                            m = s/60
                            print(f"{s}Seconds is {m}Minutes")
                        elif time == 2:
                            m = float(input("Minutes:- "))
                            h = m/60
                            print(f"{m}Minutes is {h}Hours")
                        elif time == 3:
                            print("Returning back to Main Menu")
                            break                            
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 6: #Area Convertor
                print("||Welcome to Area Section||")
                try:
                    while True:
                        area = int(input("Area Menu \n1. Square Meters to Square Feets \n2. Square Feets to Square Meters \n3. Acres to Hectors \n4. Back to Main Menu \nChoose from the speed Menu: "))
                        if area == 1:
                            sqm = float(input("Square Meters:- "))
                            sqf = sqm*10.7639
                            print(f"{sqm}Square Meters is {sqf}Square Feets")
                        elif area == 2:
                            sqf = float(input("Square Feets:- "))
                            sqm = sqf*0.92903
                            print(f"{sqf}Square Feets is {sqm}Square Meters")
                        elif area == 3:
                            a = float(input("Acres:- "))
                            h = a*0.404686
                            print(f"{a}Acres is {h}Hectares")
                        elif area == 4:
                            print("Returning back to Main Menu")
                            break                            
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 7: #Volume Convertor
                print("||Welcome to Volume Section||")
                try:
                    while True:
                        volume = int(input("Volume Menu \n1. Liters to Gallons(US) \n2. Gallons(US) to Liters \n3. Cubic Meters to Cubic Feets \n4. Back to Main Menu \nChoose from the speed Menu: "))
                        if volume == 1:
                            l = float(input("Litres:- "))
                            g = l*0.264172
                            print(f"{l}Litres is {g}Gallons(US)")
                        elif volume == 2:
                            g = float(input("Gallons(US):- "))
                            l = g*3.78541
                            print(f"{g}Gallons(US) is {l}Litres")
                        elif volume == 3:
                            cm = float(input("Cubic Meters:- "))
                            cf = cm*35.3147
                            print(f"{cm}Cubic Meters {cf}Cubic Feets")
                        elif volume == 4:
                            print("Returning back to Main Menu")
                            break                            
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 8: #Energy Convertor
                print("||Welcome to Energy Section||")
                try:
                    while True:
                        energy = int(input("Energy Menu \n1. Joules to Calories \n2. Calories to Joules \n3. KilowattHours to Joules \n4. Back to Main Menu \nChoose from the speed Menu: "))
                        if energy == 1:
                            j = float(input("Joules:- "))
                            c = j*0.239006
                            print(f"{j}Joules is {c}Calories")
                        elif energy == 2:
                            c = float(input("Calories:- "))
                            j = c*4.184
                            print(f"{c}Calories is {j}Joules")
                        elif energy == 3:
                            kwh = float(input("KilowattHour:- "))
                            j = kwh*3.6*(10**6)
                            print(f"{kwh}KilowattHour is {j}Joules")
                        elif energy == 4:
                            print("Returning back to Main Menu")
                            break                            
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 9: #Pressure Convertor
                print("||Welcome to Pressure Section||")
                try:
                    while True:
                        pressure = int(input("Pressure Menu \n1. Pascals to Atmospheres \n2. Atmospheres to Pascals \n3. Back to Main Menu \nChoose from the speed Menu: "))
                        if pressure == 1:
                            p = float(input("Pascals:- "))
                            atm = p*9.86923*(10**(-6))
                            print(f"{p}Pa is {atm}Atm")
                        elif pressure == 2:
                            atm = float(input("Atmospheres:- "))
                            p = atm*101325
                            print(f"{atm}Atm is {p}Pa")
                        elif pressure == 3:
                            print("Returning back to Main Menu")
                            break                            
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 10: #Digital Storage Convertor
                print("||Welcome to Digital Storage Section||")
                try:
                    while True:
                        data = int(input("Digital Storage Section Menu \n1. Bytes to KiloBytes \n2. KiloBytes to MegaBytes \n3. MegaBytes to GigaBytes \n4. Back to Main Menu \nChoose from the speed Menu: "))
                        if data == 1:
                            b = float(input("Bytes:- "))
                            kb = b/1024
                            print(f"{b}Bytes is {kb}KB")
                        elif data == 2:
                            kb = float(input("KiloBytes:- "))
                            mb = kb/1024
                            print(f"{kb}KB is {mb}MB")
                        elif data == 3:
                            mb = float(input("MegaBytes:- "))
                            gb = mb/1024
                            print(f"{mb}MB is {gb}GB")
                        elif data == 4:
                            print("Returning back to Main Menu")
                            break                            
                        else:
                            print("Invalid Input")
                except ValueError:
                    print("Only Enter Numerical Values")
            elif main_menu == 11:
                print("Thanks For Using Unit Convertor have a nice day!!")
                break
            else:
                print("Invalind Input")
    except ValueError:
        print("Please Enter Only Numerical Values!!")   


unit_convertor()