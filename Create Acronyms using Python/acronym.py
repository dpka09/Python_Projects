text= input("Enter a phrase: \n")

txt=text.split()

a=" "
for i in txt:
    a=a+str(i[0]).upper()
print(a)