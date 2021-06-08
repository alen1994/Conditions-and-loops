print("Hello new User! This is a program that converts kilometers into miles.")

while True:

    km = input("Kilometers: ")

    km = float(km.replace(",", "."))  # User can write number with ,  and .

    miles = km * 0.621371

    print(str(km) + " kilometers is " + str(miles) + " miles.")

    again = input("Would you like to do another conversion (y/n): ")

    if again.lower() != "y" and again.lower() != "yes":
        print("Good bye!")
        break
