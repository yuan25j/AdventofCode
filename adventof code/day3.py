my_file = open("input3.txt", "r")
  
# reading the file
data = my_file.read()
  
# replacing end splitting the text 
# when newline ('\n') is seen.
data_into_list = data.split("\n")
print(data_into_list)
my_file.close()
for x in data_into_list:
    first = x[0:len(x)/2]
    last = x[len(x)/2-1:len(x)-1]
    print(first)
    