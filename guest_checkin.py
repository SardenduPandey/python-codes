##Code for a hotel where few guests checked in and checked out

'''Initally there were few guests'''
guests = open("guests.txt", "r+")               #'r+' = read and write 
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
print('Initial Guests:')
for i in initial_guests:
    guests.write(i + "\t")
    print(i.upper())
    
guests.close()

'''New guests chechek in '''
new_guests = ["Sam", "Danielle", "Jacob"]
with open("guests.txt", "a") as guests:         #'a' = append (to add elements in files)
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

'''Display the current guest staying in Hotel '''
with open("guests.txt") as guests:              #by deafult its 'r'
    print("\nChecking current Status...\nTotal Guest in Hotel\n")
    for line in guests:
        print(line)

'''Few guest checked out'''
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

'''Display the current guest staying in Hotel after checkout '''
with open("guests.txt") as guests:
    print("\nChecking current Status...\nTotal Guest in Hotel\n")
    for line in guests:
        print(line)


'''checking the status of 2 guest'''

print("Checking the status of 2 random Guests")
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))