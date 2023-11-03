import random

def Found(List,n,first,last):
    if first==last:
        return List[first]
    av_index=partition(List,first,last)
    k=av_index+1
    if n==k:
        return(List[av_index])
    
    elif n > k:
        n=n-k
        x=Found(List,n-k,av_index+1,last)
        
    elif n < k:
        x=Found(List,n,first,av_index-1)
        
    return(x)

def partition(List,first,last):
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
# ========================================

# ------------------------------
# input number List and make a number List with type "int"
List=input("Enter your List: ")  # List is global
List=List.split()
n=input("Enter i: ")

#type casting: list indexes turn to int 
for i in range(0,len(List)): 
    List[i]=int(List[i])
    
# ------------------------------
# mixed List 
random.shuffle(List)
# ----------------------------
# found 
x=Found(List,n,0,len(List)-1)
print(x)