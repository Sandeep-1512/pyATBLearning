sandeep = (1,2,3,4,5)
#sandeep1 = (6,7,8,9,10)
#new_tuple = (sandeep, sandeep1)
#print(new_tuple)
#print(new_tuple[1][1])
#print(new_tuple[0][4])

sandeep2 = list(sandeep)  #Convertig tuple to list)
#print(sandeep2)
sandeep2.append(8) #append to insert new value
#print(sandeep2)
sandeep=tuple(sandeep2) #reconverting list to tuple
print(sandeep)