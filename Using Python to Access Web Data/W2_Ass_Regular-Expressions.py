import re

fopen=open('regex_sum_853290.txt')
sum=0
for line in fopen:
    numbers = re.findall('[0-9]+', line)
    for num in numbers:
        sum = sum+int(num)
print(sum)
