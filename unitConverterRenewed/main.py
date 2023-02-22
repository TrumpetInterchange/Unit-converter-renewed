import conversion as cv
import functions as f


f.init() #The program starts up
while True:
    f.layout() 
    option_what = input() #Usr choose what to convert

    if f.isIntger(option_what) == True: #Usr responded correctly
        if int(option_what) == 1: #Usr chose tempreature
            f.tempLayout()
            option_how = input() #Usr choose how to convert

            while f.isIntger(option_how) == False: #and the input was not correct
                f.notValidResponse('integer')
                f.tempLayout()
                option_how = input()

            #now the user finally got it right
            
            if int(option_how) == 1: #Celsius to Fahrenheit
                conversion = input('Enter the value you want to convert from\n')

                while f.isFloat(conversion) == False: #Checking the response...
                    f.notValidResponse('float')
                    conversion = input('Enter the value you want to convert from\n')
                    
                #When successful
                print(
                    f'{conversion} degrees Celsius equals to {cv.C2F(float(conversion))} Fahrenheit!'
                )

            if int(option_how) == 2: #Fahrenheit to Celsius
                conversion = input('Enter the value you want to convert from\n')

                while f.isFloat(conversion) == False: #Checking the response...
                    f.notValidResponse('float')
                    conversion = input('Enter the value you want to convert from\n')
                    
                #When successful
                print(
                    f'{conversion} degrees Fahrenheit equals to {cv.F2C(float(conversion))} Celsius!'
                )

            if int(option_how) == 3: #Celsius to Kelvin
                conversion = input('Enter the value you want to convert from\n')

                while f.isFloat(conversion) == False: #Checking the response...
                    f.notValidResponse('float')
                    conversion = input('Enter the value you want to convert from\n')
                    
                #When successful
                print(
                    f'{conversion} degrees Celsius equals to {cv.C2K(float(conversion))} Kelvin!'
                )
                
            if int(option_how) == 4: #Kelvin to Celsius
                conversion = input('Enter the value you want to convert from\n')

                while f.isFloat(conversion) == False: #Checking the response...
                    f.notValidResponse('float')
                    conversion = input('Enter the value you want to convert from\n')
                    
                #When successful
                print(
                    f'{conversion} Kelvin equals to {cv.K2C(float(conversion))} Celsius!'
                )
            
            if int(option_how) == 5: #Fahrenheit to Kelvin
                conversion = input('Enter the value you want to convert from\n')

                while f.isFloat(conversion) == False: #Checking the response...
                    f.notValidResponse('float')
                    conversion = input('Enter the value you want to convert from\n')
                    
                #When successful
                print(
                    f'{conversion} degrees Fahrenheit equals to {cv.F2K(float(conversion))} Kelvin!'
                )

            if int(option_how) == 6: #Kelvin to Fahrenheit
                conversion = input('Enter the value you want to convert from\n')

                while f.isFloat(conversion) == False: #Checking the response...
                    f.notValidResponse('float')
                    conversion = input('Enter the value you want to convert from\n')
                    
                #When successful
                print(
                    f'{conversion} Kelvin equals to {cv.K2C(float(conversion))} Fahrenheit!'
                )

        elif int(option_what) == 2: #Usr chose velocity
            pass
        elif int(option_what) == 3: #Usr chose mass
            pass
        elif int(option_what) == 4: #Usr chose to quit
            print('Shut down successful')
            break
        else: #it was an intger but out of range
            f.notValidResponse('integer')

    else: #Usr didn't respond correctly(not an integer)
        f.notValidResponse('integer')       

