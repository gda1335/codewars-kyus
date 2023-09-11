# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).
# count_by(2,5) #should return [2,4,6,8,10]

def count_by(x, n):
    arr=[]
    for i in range(1,n+1):
        i*=x
        arr.append(i)
    return arr



print(count_by(1, 5))    

##once x: baslangic sayisi n de nereye kadar gidiceği 
#2 4 6810 
#2 nin katlarinidolascak n ekadar o zaman n'ni forla n'e kadar dolascaz.
#ve her defasinda x: baslangic sayisi ile artis elemani olan iyi carpicaz ve bir arr'e aticaz