with open("All_Contacts.txt","r") as f1:
    all_contacts=f1.readlines()
    l1=len(all_contacts)

unique_contacts=[]

for phno in all_contacts:
    phno=phno.strip()
    phno=phno.strip("\n")
    if phno not in unique_contacts:
        unique_contacts.append(phno)
        
l2=len(unique_contacts)

unique_contacts.sort()

f2=open("Unique_Contacts.txt","w")

for i in unique_contacts:
    f2.write(i+"\n")
    
print("Duplicate Contacts deleted =",l1,"-",l2,"=",l1-l2)
print("The unique contacts have been moved to 'Unique_Contacts' from 'All_Contacts' in your current directory")
f2.close()