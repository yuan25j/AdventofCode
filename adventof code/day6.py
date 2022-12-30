from collections import Counter

my_file = open("adventof code\input6.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
#print(data_into_list)
#print(data_into_list)
my_file.close()
wholeString = data_into_list[0]
#part one solution
for i in range(len(wholeString)-3):
    temp = ""
    temp += wholeString[i]
    temp += wholeString[i+1]
    temp += wholeString[i+2]
    temp += wholeString[i+3]
    #print(temp)
    freq = Counter(temp)
 
    if(len(freq) == len(temp)):
        print(i + 3)
        break
    #part 2 solution
for i in range(len(wholeString)-14):
    temp = ""
    for k in range(14):
        temp += wholeString[i+k]
    
    #print(temp)
    freq = Counter(temp)
 
    if(len(freq) == len(temp)):
        print(i + 14)
        break
    