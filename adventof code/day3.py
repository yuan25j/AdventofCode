my_file = open("adventof code\input3.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
my_file.close()
result = 0
hash = {}
i = ord("A")
j = 27
while i <= ord("Z"):
    hash[chr(i)] = j
    i += 1
    j += 1
i = ord("a")
j = 1
while i <= ord("z"):
    hash[chr(i)] = j
    i += 1
    j += 1
print(hash)
#code for part 2
templst = []
for i in range (len(data_into_list)):
    print(i)
    templst.append(data_into_list[i])
    print(templst)
    if (i+1) % 3 == 0:
        for x in templst[0]:
            if x in templst[1] and x in templst[2]:
                # print(x)
                # print(hash[x])
                result += hash[x]
                # print(result)
                templst = []
                break
print(result)
        
    
        
        

#below code is for part 1
# for x in data_into_list:
#     first = x[0:int(len(x)/2)]
#     last = x[int(len(x)/2):len(x)]
#     #print(first)
#     #print(last)
#     for z in first:
#         if z in last:
#             #print(z)
#             #print(hash[z])
#             result += hash[z]
#             #print(result)
#             break
        
   
# print(result)