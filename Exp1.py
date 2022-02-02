import csv 

file = open('C:\\Users\\HP\\Desktop\\AI-2043_Mchine Learning\\finds.csv')
all_rows = csv.reader(file)

data = []
for row in all_rows:
    data.append(row)
    print(row)

hypothesis = []    

for instance in data:
    if hypothesis:
        if instance[-1] == 'Yes':    
            for attribute_indx in range(len(hypothesis)):
                if instance[attribute_indx] != hypothesis[attribute_indx]:
                    hypothesis[attribute_indx] = '?'    
    else:
        hypothesis = instance[:-1]

print(hypothesis)


ask_user = list(input().split(' '))

for attribute_ind in range(len(hypothesis)):
    if hypothesis[attribute_ind] !=  '?' and ask_user[attribute_ind] == hypothesis[attribute_ind]:
        pass
    if hypothesis[attribute_ind] !=  '?':
        pass
    else:
        print('will not go out')
        break


