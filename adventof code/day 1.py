my_file = open("input.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)
my_file.close()
result = []
counter = 0

for x in data_into_list:
    if x != '':
        intx = int(x)
        counter += intx
        result.append(counter)
    else:
        counter = 0
result.sort()
print(result[len(result)-1] + result[len(result)-3] + result[len(result)-2])

        
    
    
        
    
        
    