#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
sample_list=[8,2,3,0,7]
def sum(sample_list):
    total = 0
    for i in sample_list:
        total+=i
    return total    
print('sum of all the numbers in a list--->',sum(sample_list))