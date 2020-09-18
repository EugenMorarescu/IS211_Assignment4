import time
import random
from timeit import Timer

def sequential_search(a_list,item):
    start=time.time()
    pos = 0
    found = False
    
    while pos<len(a_list) and not found:
        if a_list[pos]==item:
            found = True
        else:
            pos= pos+1
    end=time.time()
    
    return found,end-start

def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    
    end = time.time()
    return found,end-start



def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1        
            else:
                first = midpoint + 1
    end = time.time()
    return found, end-start


def binary_search_recursive(a_list, item):
    start=time.time()
    if len(a_list) == 0:
        end=time.time()
        return False,end-start
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end=time.time()
        return True,end-start
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)
        
def timed(func,l):
        
        Tot=0
        T=Timer('for i in l: func(i,-1)', 'from __main__ import l,func')
        Tot+= T.timeit(number=1)
        avg=(Tot/100)
        return avg
        

if __name__ == '__main__':
    
    TotL1=[]
    TotL2=[]
    TotL3=[]
    
    
    
    for i in range(100):
        list1 = random.sample(range(1, 501), 500)
        TotL1.append(list1)
        
        list2 = random.sample(range(1, 1001), 1000)
        TotL2.append(list2)
        
        list3 = random.sample(range(1, 10001), 10000)
        TotL3.append(list3)
    
    ssAvg=ossAvg=bsiAvg=bsrAvg=0
    
    l=TotL1
    func=sequential_search
    ssAvg+=timed(func,l)
    l=TotL2
    func=sequential_search
    ssAvg+=timed(func,l)
    l=TotL3
    func=sequential_search
    ssAvg+=timed(func,l)
    
    l=TotL1
    l.sort()
    func=ordered_sequential_search
    ossAvg+=timed(func,l)
    l=TotL2
    l.sort()
    func=ordered_sequential_search
    ossAvg+=timed(func,l)
    l=TotL3
    l.sort()
    func=ordered_sequential_search
    ossAvg+=timed(func,l)
    
    l=TotL1
    l.sort()
    func=binary_search_iterative
    bsiAvg+=timed(func,l)
    l=TotL2
    l.sort()
    func=binary_search_iterative
    bsiAvg+=timed(func,l)
    l=TotL3
    l.sort()
    func=binary_search_iterative
    bsiAvg+=timed(func,l)
    
    l=TotL1
    l.sort()
    func=binary_search_recursive
    bsrAvg+=timed(func,l)
    l=TotL2
    l.sort()
    func=binary_search_recursive
    bsrAvg+=timed(func,l)
    l=TotL3
    l.sort()
    func=binary_search_recursive
    bsrAvg+=timed(func,l)
    
        
    print("Sequential Search took %10.7f seconds to run, on average" % (ssAvg))
    print("Ordered Sequential Search took %10.7f seconds to run, on average" % (ossAvg))
    print("Binary Search Iterative took %10.7f seconds to run, on average" % (bsiAvg))
    print("Binary Search Recursive took %10.7f seconds to run, on average" % (bsrAvg))