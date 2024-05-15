#email

email = input("Enter email_ ").strip()
#username

user = email[:email.index("@")]

domain = email[email.index("@")+1:]

output = "username is {} and domain is {}"
output = output.format(user,domain)

print(output)

#print(user)
#print(domain)