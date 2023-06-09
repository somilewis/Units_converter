# Lewis Muthomi
# 1250 01
# 17 october 2022
# Lab 9

# This program will  convert convert inches to centimeters,centimeters to
# inches, Grams to ounces,Ounces to grams,Kilometers to Miles, or
# Miles to kilometers


# User greetings
print('Welcome to my conversion program')
print()
print('Enter I to convert from Inches to Centimeters')
print('Enter C to convert from Centimeters to Inches')
print('Enter O to convert from Ounces to Grams')
print('Enter G to convert from Grams to Ounces')
print('Enter M to convert from Miles to kilometers')
print('Enter K to convert from kilometers to Miles')
print()


# Create a variable
runProgram = 'y'

while runProgram == 'y':

    # Get user input conversion
    conversionUnit = input('Enter the type of conversion you would like to do: ').upper()
    print()
    
    # Error check program
    while conversionUnit not in ['I','C','O','G','M','K']:
        conversionUnit = input('INPUT ERROR: Please enter a I or C or O or G or M or K: ').upper()

    # Get user input measure/weight
    measure = float(input('Enter a measure/weight you want to convert: '))
    print()


    # Do conversions, calculations and display results
    if conversionUnit == 'I':
        measureConvert = measure * 2.54
        print(measure,'inches equals', format(measureConvert, ',.2f'), 'centimeters')
    elif conversionUnit == 'C':
        measureConvert = measure / 2.54
        print(measure, 'centimeters equals', format(measureConvert, ',.2f'), 'inches')
    elif conversionUnit == 'O':
        measureConvert = measure * 28.3495231
        print(measure, 'ounces equals', format(measureConvert, ',.2f'), 'grams')
    elif conversionUnit == 'G':
        measureConvert = measure / 28.3495231
        print(measure, 'grams equals', format(measureConvert, ',.2f'), 'ounces')
    elif conversionUnit == 'M':
        measureConvert = measure * 1.609344
        print(measure, 'miles equals', format(measureConvert, ',.2f'), 'kilometers')
    else:
        measureConvert = measure / 1.609344
        print(measure, 'kilometers equals', format(measureConvert, ',.2f'), 'miles')
    print()
        

     # Program loop
    again = input('Would you like to make another conversion?(y/n) ').lower()
    print()
    
    # Error check loop
    while again != 'y' and again != 'n':
       again = input('INPUT ERROR: Please type a y or n: ').lower()
  
    if again == 'n':
        runProgram = 'false'

# Exit message
print()
print ('Have a nice day!!!!')

      
      
