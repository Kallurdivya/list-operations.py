L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h'] 
print(L[2]) 
print(L[2][2]) 
print(L[2][2][0]) 
print(L[-3]) 
my_list = [_ for _ in 'abcdefghi'] 
print("------------------- Indexing and Slicing -------------------") 
print("slicing ",my_list[5:]) 
print("slicing ",my_list[:4]) 
print(L[-3][-1]) 
print(L[-3][-1][-2])  
print("------------------- Length -------------------") 
print(len(L)) 
print(len(L[1])) 
print("------------------- Concatenation -------------------") 
test_list3 = [1, 4, 5, 6, 5] 
test_list4 = [3, 5, 7, 2, 5] 
print("Concatenated list using + : "+ str(test_list3)) 
print("------------------- Member Ship -------------------") 
l=[1 ,2 ,3] 
print("2 contains in list ", 2 in l)  
print("------------------- Interation -------------------") 
for i in range(0,len(l)): 
    print(l[i]) 