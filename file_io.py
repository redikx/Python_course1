countries = ["Luxembourgi", "Germany", "Poland", "France", "Belgium"]

# Create new file
with open("new_file.txt", 'w') as file_w:
    for country in countries:
        print(country,file=file_w)

# Read from file line by line
with open("new_file.txt", 'r') as file_r:
    line = file_r.readline()
    while line:
        print("Linia : " + line, end='' )
        line = file_r.readline()
    print('*'*40)

# Read from file all lines
with open("new_file.txt", 'r') as file_r2:
    lines_w = file_r2.readlines()
    for line in lines_w:
        print(line,end='')
    print('*'*40)

# Read file skipping last line (or any shard, reverse etc)
with open("new_file.txt", 'r') as file_r3:
    lines2 = file_r3.readlines()
    for line in lines2[0:len(lines2)-1:]:
        print(line,end='')


