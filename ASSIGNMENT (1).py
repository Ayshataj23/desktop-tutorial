#AYSHA TAJ
#1
a = [1, 2, 4, 2, 5, 2, 6]
b = []
for x in a:
     if x != 2: 
         b= b +[x] 
         print(b)

#2
nums = [9, 2, 11, 7, 11, 3]
largest = None 
second = None 
for x in nums:
     if largest is None or x > largest:
          if largest is None or x != largest:
              second = largest
              largest = x 
          elif x != largest and (second is None or x > second): 
              second = x
              print("Second largest distinct =", second)

#3
a = [10, 20, 30, 40, 50] 
first = a[0] 
for i in range(len(a)- 1):
     a[i] = a[i + 1] 
     a[-1] = first  
print(a) 

#4
a = [1, 2, 3, 4, 5]            
k = int(input("Enter index k (0..5): ")) 
value = 99                     
a = a + [0]                    
for i in range(len(a) - 1, k, -1): 
    a[i] = a[i - 1]             
a[k] = value                  
print(a)                       

#5
a = [5, 6, 7, 8, 9, 10]              
k = int(input("Enter index k (0..5): "))  
for i in range(k, len(a) - 1):       
    a[i] = a[i + 1]                  
a = a[:-1]                           
print(a)      

#6
line = input("Enter a line: ")   
word = ""
for ch in line:
    if ch != " ":
        word = word + ch        
    else:
        if word != "":
            words = words + [word] 
            word = ""
if word != "":
    words = words + [word]       
longest = ""
for w in words:
    if len(w) > len(longest): 
        longest = w
print("Longest:", longest)      
print("Length:", len(longest)) 

#7
s = input("Enter sentence: ")))
words = []
word = ""
for ch in s:
    if ch != " ":
        word = word + ch         
    else:
        if word != "":
            words = words + [word]  
            word = ""
if word != "":                        
    words = words + [word]       #
result = ""
for i in range(len(words)):
    if i == 0:
        result = words[i]        
    else:
        result = result + " | " + words[i]  
print(result)                   

#8
a = [3, 3, 2, 3, 1, 2, 4, 4]    
u = []                            
for x in a:                       
    if x not in u:                
        u = u + [x]               
print(u)                       

#9
a = [1, 1, 1, 2, 2, 3, 4, 4]    
seen = []                         
for x in a:
    if x in seen:                 
        continue
    count = 0                     
    for y in a:                   
        if y == x:
            count += 1
    print(x, "->", count)         
seen = seen + [x]       

#10
a = [8, 3, 5, 2, 9, 1]          
n = len(a)                        
for passno in range(n - 1):      
    for i in range(n - 1 - passno):  
        if a[i] > a[i + 1]:      
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
print(a)                          