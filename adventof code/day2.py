my_file = open("input2.txt", "r")
  
# reading the file
data = my_file.readlines()
  
# replacing end splitting the text 
# when newline ('\n') is seen.

my_file.close()
score = 0
print(data)
# rock = 1, paper = 2, scissors = 3
# a = rock, b = paper, c = scissors
#for part 2, x = lose, y= tie, z = win
for x in data:
    if x[0] == "A":
        if x[2] == "X": #scissors
            score += 3 + 0
        elif x[2] == "Y": #rock for tie
            score += 1 + 3
        elif x[2] == "Z":
            score += 2 + 6
    if x[0] == "B": #paper
        if x[2] == "X":
            score += 1 + 0
        elif x[2] == "Y":
            score += 2 + 3
        elif x[2] == "Z":
            score += 3 + 6
            
    if x[0] == "C": #scissors
        if x[2] == "X": #choose paper to lose
            score += 2 + 0
        elif x[2] == "Y":
            score += 3 + 3
        elif x[2] == "Z": 
            score += 1 + 6
print(score)