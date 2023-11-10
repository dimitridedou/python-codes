array=[] #make list
x=i=0
# append value
while (x!=-1):
    x=int(input(" Give Num :"))
    if (x!=-1):
        array.append(x)
    i=i+1
N=len(array)
print("ΑΡΧΙΚΗ ΛΙΣΤΑ EINAI",array) # print list before sorting
print("")
for i in range(1,N,1): # start sort
   print(str(i)+"η Μεγαλη επεναληψη")
   print("--------------------------------------------------------------")
   for j in range(N-1,i-1,-1):
        print("")
        print("Συγκρινει τους αριθμους ",array[j-1]," και ",array[j])
        if array[j]<array[j-1]:
            array[j],array[j-1]= array[j-1],array[j]
            print("Το ",array[j]," δεν ειναι μικροτερο απο το",array[j-1])
            print("")
            print("Aρα η νεα λιστα ειναι : ", array)
        else:
            print("Η λιστα παραμενη οπως εχει διοτι το",array[j],
                  str("ειναι μεγαλυετρο απο το"),array[j-1])
   print("--------------------------------------------------------------")
   print("")
   print("")
   print("")
print("H τελικη λιστα είναι :", array) # print list after sorting
            
  
