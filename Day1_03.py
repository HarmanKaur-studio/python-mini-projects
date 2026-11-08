# Length function
#1
print("-------Length function-----")
print(len(input("Enter your name: ")))

#2
print("Integer Length calculation: ")
num_str=input("Enter number: ")
print(len(str(num_str)))

#3
name=input("Enter your name: ")
Length=len(name)
print("Hello " + name)
print("Total letters in your name: " + str(Length))
# python cannot concatenate string and number so convert the integer variable Length to string

#----------------------------------------------------------------------------------------------

#Exercise-Variable
#We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.
glass1="milk"
glass2="juice"
print("Before Exchange:")
print("Glass 1 contains: " + glass1)
print("Glass 2 contains: " + glass2)
glass3=glass1
glass1=glass2
glass2=glass3
print("After Exchange")
print("Glass 1 contains: " + glass1)
print("Glass 2 contains: " + glass2)