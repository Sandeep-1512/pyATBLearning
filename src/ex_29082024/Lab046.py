my_list = [1,2,3,3,4,4]

##print(my_list)
##print(len(my_list))  ##length always start from 1

print(my_list[5])
print(my_list[3])
print(my_list[4])
my_list[3] = "Sandeep"
my_list[1] = "Gurnoor"
my_list[0] = "Kamal"

print(my_list)

for element in my_list:
    print(element)
my_list.append(7)
my_list.append(8)
my_list.append(9)
my_list.append(10)
my_list.extend([11,12,13])
my_list.insert(-15,"Sodhi")
my_list.remove(3)
my_list.remove(4)
my_list.remove("Kamal")
my_list.reverse()
print(my_list)
print(len(my_list))