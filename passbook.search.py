# Creating two empty lists for names and account_numbers of passbooks

names = []
account_numbers = []
num = 3

# run a for loop and take a input for name and account_numbers
# append the inputs into the list that  created earlier

for i in range(num):
    name = input("Name: ")
    account_number = input("Account Number: ") 
    names.append(name)
    account_numbers.append(account_number)

# print the format for output

print("\nName\t\t\tAccount Number\n")

# run a for loop over the variable and print the format for variables

for i in range(num):
    print("{}\t\t\t{}".format(names[i], account_numbers[i]))

#Store the user input to enter the search term:

search_term = input("\nEnter search term: ")
print("Search result:")
print("Pass book holder found")

# Search the term and print the account_number associated with it

if search_term in names:
    index = names.index(search_term)
    account_number = account_numbers[index]
    print("Name: {}, Account Number: {}".format(search_term, account_number))

# if search term not found print name not found

else:
    print("Pass book holder not found")