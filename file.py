# read data in  txt file 

f = open("/home/sarfaraz_alam/Music/python_code/ hassan.txt","r")

print(f.read())


# write date in txt  file 

f =open("/home/sarfaraz_alam/Music/python_code/ hassan.txt","a")

f.write("this is extra data in hassan.txt file ")
f.close()

# reopen file and read data 

f1 = open ("/home/sarfaraz_alam/Music/python_code/ hassan.txt", "r")
print(f1.read())
f1.close()

