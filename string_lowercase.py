first_string = "SMART NINJA IS AWESOME!"
second_string = "SmArT nInJa Is AwEsOmE!"

str_one="Happy"
str_two ="Day"

if(first_string.lower() == second_string.lower()): #returns the lowercased string from the given string. It converts all uppercase characters to lowercase.
    print("The strings are exactly the same.")
    print("{0} {1}".format(str_one, str_two) + "!!") #In programming, counting starts with 0. That's why {0} means the first string.
else:
    print("The strings are not same.")