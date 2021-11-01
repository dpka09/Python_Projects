email= input('Enter email :\n').strip()
username= email[:email.index("@")]
domain_name= email[email.index("@")+1:]

print(username)
print(domain_name)