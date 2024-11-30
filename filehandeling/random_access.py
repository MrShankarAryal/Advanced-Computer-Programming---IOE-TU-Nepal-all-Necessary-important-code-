with open("std_ran_acess.bin","wb")as file:
    file.write(b"ID: kce080bel023\nName: shankar aryal\nAge: 20 \nAddress: gaindakotID: kace080bel003\nName: anupam poudel\nAge: 20 \nAddress: Dharan")

with open("std_ran_acess.bin","rb")as file:
     #read file last 6 bytes worlds only
     file.seek(-6,2)
     print(file.tell())
     content=file.read(6)
     print(content.decode())
     #file cursore last
     file.seek(0,2)
     print(file.tell())
     content2=file.read()
     print(content2.decode())
 
     #file curse biging
     file.seek(0)
     print(file.tell())
     content3=file.read()
     print(content3.decode())