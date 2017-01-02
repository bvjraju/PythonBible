# Get users email address

email = input(" Enter your email address:  ").strip()

# slice user name

user = email[0:email.index("@")]

# slice domain name

domain = email[email.index("@")+1:]

# format output message

output = "your user name is {} and Domain name is {}" .format(user, domain)

# Display out put message

print(output)
