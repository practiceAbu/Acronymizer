
val = str(input("Enter the Phrase : "))

text = val.split()
a = ''
for i in text:
    a += str(i[0]).upper()


print(a)



