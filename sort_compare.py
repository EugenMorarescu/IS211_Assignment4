import time
import random
from timeit import Timer

def insertion_sort(a_list):
    
    start=time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
    
        a_list[position] = current_value
    
    end=time.time()
    
    return a_list, end-start



def shell_sort(a_list):
    start=time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2
    end=time.time()
    
    return(a_list,end-start)

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            
            a_list[position] = a_list[position - gap]
            position = position - gap
            
            a_list[position] = current_value

def python_sort(list):
    list.sort()
    
def timed(func,l):
        
        Tot=0
        T=Timer('for i in l: func(i)', 'from __main__ import l,func')
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
                
    avgIS=avgSS=avgPS=0

    l=TotL1
    func=insertion_sort
    avgIS+=timed(func,l)
    l=TotL2
    func=insertion_sort
    avgIS+=timed(func,l)
    l=TotL3
    func=insertion_sort
    avgIS+=timed(func,l)
    
    l=TotL1
    func=shell_sort
    avgSS+=timed(func,l)
    l=TotL2
    func=shell_sort
    avgSS+=timed(func,l)
    l=TotL3
    func=shell_sort
    avgSS+=timed(func,l)
    
    l=TotL1
    func=python_sort
    avgPS+=timed(func,l)
    l=TotL2
    func=python_sort
    avgPS+=timed(func,l)
    l=TotL3
    func=python_sort
    avgPS+=timed(func,l)
    
    
    print("Insertion Sort took %10.7f seconds to run, on average" % (avgIS))
    print("Shell Sort took %10.7f seconds to run, on average" % (avgSS))
    print("Python Sort took %10.7f seconds to run, on average" % (avgPS))