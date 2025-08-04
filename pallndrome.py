#  ask the user for a string
user_string = input("please enter a string: ")
# reverse the string
reversed_string = ""
for char in user_string:
    reversed_string = char + reversed_string
# check if the string is a palindrome
if user_string == reversed_string:
    print("the string is a palinedrome")
else:
    print("the string is not a palindrom")