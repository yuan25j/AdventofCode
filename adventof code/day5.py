my_file = open("adventof code\input5.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
#print(data_into_list)
my_file.close()
#print(data_into_list)
stacks = [[],[],[],[],[],[],[],[],[]]
#print(data_into_list[7])
#solution for first part
# for i in range(len(data_into_list)):
#     #creates the stacks
#     if i <= 7:
#         for j in range(len(data_into_list[i])):
#             if data_into_list[i][j] != " " and data_into_list[i][j] != "[" and data_into_list[i][j] != "]":
#                 #print(j)
#                 #print(data_into_list[i][j])
#                 position = int((j -1) / 4)
#                 stacks[position].append(data_into_list[i][j])
#     elif i> 9:
#        # print(data_into_list[i])
#         firstSpaceIndex = data_into_list[i].find(" ")
#         secondSpaceIndex = data_into_list[i].find(" ", firstSpaceIndex + 1)
#         thirdSpaceIndex =  data_into_list[i].find(" ", secondSpaceIndex + 1)
#         firstVal = int(data_into_list[i][firstSpaceIndex+ 1:secondSpaceIndex + 1])
#         secondVal = int(data_into_list[i][thirdSpaceIndex + 1])
#         thirdVal = int(data_into_list[i][len(data_into_list[i]) - 1])
#         for k in range(firstVal):
#             stacks[thirdVal-1].insert(0, stacks[secondVal-1][0])
#             stacks[secondVal-1].pop(0)
        
            
            
        
# for x in stacks:
#     print(x[0])

#solution for part 2
for i in range(len(data_into_list)):
    if i <= 7:
        for j in range(len(data_into_list[i])):
            if data_into_list[i][j] != " " and data_into_list[i][j] != "[" and data_into_list[i][j] != "]":
                #print(j)
                #print(data_into_list[i][j])
                position = int((j -1) / 4)
                stacks[position].append(data_into_list[i][j])
    elif i> 9:
       # print(data_into_list[i])
        firstSpaceIndex = data_into_list[i].find(" ")
        secondSpaceIndex = data_into_list[i].find(" ", firstSpaceIndex + 1)
        thirdSpaceIndex =  data_into_list[i].find(" ", secondSpaceIndex + 1)
        firstVal = int(data_into_list[i][firstSpaceIndex+ 1:secondSpaceIndex + 1])
        secondVal = int(data_into_list[i][thirdSpaceIndex + 1])
        thirdVal = int(data_into_list[i][len(data_into_list[i]) - 1])
        for k in range(firstVal):
            stacks[thirdVal-1].insert(0, stacks[secondVal-1][firstVal-k-1])
            stacks[secondVal-1].pop(firstVal-k-1)
        
            
            
        
for x in stacks:
    print(x[0])