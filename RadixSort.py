
from random import randint

def RadixSort(list1,d):    
    for k in range(d):# k is used to check each digit, ex, 987, k=0, check 7; k=1,check 80; k=2, check 900
        s=[[] for i in range(10)]#because for each digit, there are 10 options from 0 to 9, so create 10 lists.
        print(s)
        for i in list1: #check each element in list1
            
            index_s=int(i/(10**k)%10) # ex, k=0, i/(10**k) move i to the current check digit(个位）
                                      # k=1, 10**k=10^1=10, move i to 十位数...
                                      # %10 mod,keep the current digit.
##            print(int(index_s))
            s[index_s].append(i) #check each value of each digits
            print(s)
            
        list1=[j for i in s for j in i]
    return list1

if __name__ == '__main__':
    TestList=[randint(1,999) for i in range(10)]
    print(TestList)
    SortList=RadixSort(TestList,3) # 3 means how many digits for the largest value
    print(SortList)
