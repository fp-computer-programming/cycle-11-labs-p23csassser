# Creator CS 2/1/2023

grades = {'Mid Year Project Presention': 100,
          'Mid Year Project Proposal': 90,
          'Mid Year Project Code': 97,
          'Mid Year Project Reflection': 93}
# print all grades
print(grades.values())
# Print all assignment names
for k in grades: 
    print(k)
# print all above 70
for k in grades:
    if grades[k] > 70:
        print(f'{k} | Grade {grades[k]}')

for k in grades: 
        print(f'{k} | Grade {grades[k]}')