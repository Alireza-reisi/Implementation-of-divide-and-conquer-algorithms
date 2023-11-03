import random


def quick_sort(first,last):
    global List
    if first<last :
        av_index=partition(first,last)
        quick_sort(first,av_index-1)
        quick_sort(av_index+1,last)
    
    


# --------------------------------
# 
def partition(first,last):
    global List
    subject=List[first]
    i=first
    j=last
    while i<j:
        while List[i]<=subject and i<last: 
            i=i+1
        while List[j]>subject and j>first:
            j=j-1
        if i<j:
            swapper=List[i]
            List[i]=List[j]
            List[j]=swapper
    swapper=List[first]
    List[first]=List[j]
    List[j]=swapper
    return j


# ------------------------------
# input number List and make a number List with type "int"
List=input("Enter your List: ")  # List is global
List=List.split()

for i in range(0,len(List)): #type casting: list indexes turn to int 
    List[i]=int(List[i])
# test: -->  List=[61,5,37,1,26,11,59,15,48,19]
    
# ------------------------------
# mixed List 
random.shuffle(List)
# ----------------------------
# sorting List 
quick_sort(0,len(List)-1)
print(List)