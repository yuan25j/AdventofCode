my_file = open("adventof code\input4.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
#print(data_into_list)
my_file.close()

result = 0
#solution for part one
# for x in data_into_list:
#     oneLeft = ""
#     oneRight = ""
#     twoRight = ""
#     twoLeft = ""
#     firstDashIndex = x.index("-")
#     firstCommaIndex = x.find(",")
#     secondDashIndex = x.find("-", firstCommaIndex)
    
#     # print(firstDashIndex) 
#     # print(secondDashIndex)
#     #below two lines are right
#     oneLeft = x[0:firstDashIndex]
#     oneRight = x[firstDashIndex + 1: firstCommaIndex]
#     twoLeft = x[firstCommaIndex + 1: secondDashIndex]
#     twoRight = x[secondDashIndex + 1: len(x)]
#     # print(oneLeft)
#     # print(oneRight)
#     # print(twoLeft)
#     # print(twoRight)
#     oneLeft = int(oneLeft)
#     oneRight = int(oneRight)
#     twoLeft = int(twoLeft)
#     twoRight= int(twoRight)
#     if oneLeft >= twoLeft and oneRight <= twoRight:
#         result += 1
#     elif oneLeft <= twoLeft and oneRight >= twoRight:
#         result += 1
    
# print(result)

#part 2 solution
for x in data_into_list:
    oneLeft = ""
    oneRight = ""
    twoRight = ""
    twoLeft = ""
    firstDashIndex = x.index("-")
    firstCommaIndex = x.find(",")
    secondDashIndex = x.find("-", firstCommaIndex)
    
    # print(firstDashIndex) 
    # print(secondDashIndex)
    #below two lines are right
    oneLeft = x[0:firstDashIndex]
    oneRight = x[firstDashIndex + 1: firstCommaIndex]
    twoLeft = x[firstCommaIndex + 1: secondDashIndex]
    twoRight = x[secondDashIndex + 1: len(x)]
    # print(oneLeft)
    # print(oneRight)
    # print(twoLeft)
    # print(twoRight)
    oneLeft = int(oneLeft)
    oneRight = int(oneRight)
    twoLeft = int(twoLeft)
    twoRight= int(twoRight)
    if twoLeft <= oneRight <= twoRight:
        result += 1
    elif twoLeft <= oneLeft <= twoRight:
        result += 1
    elif oneLeft <=twoLeft <= oneRight:
        result += 1
    elif oneLeft <= twoRight <= oneRight:
        result += 1
print(result)
