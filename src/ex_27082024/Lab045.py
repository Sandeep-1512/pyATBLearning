my_shoping_list = ["clothes", "Phone cover", "Grocery"]
print(my_shoping_list[0])
print(len(my_shoping_list))

def bring_more_list(my_new_list):
    my_new_list.append("shoes")
    return my_new_list

def bring_more_list(my_list):
    more_item = input("Enter new item to be included: \n" )
    my_list.append(more_item)
    return my_list

i = bring_more_list(my_shoping_list)
print(i)
print(len(my_shoping_list))

