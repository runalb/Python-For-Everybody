#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

list = []
fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    words = line.split()
    for word in words:
        if word in list:
            continue
        list.append(word)
print(sorted(list))
