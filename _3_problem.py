#Write a Python program to count the number of even and odd numbers from a series of numb

list = [1,2,3,4,5,6,7,8,9]
even = 0
odd = 0
for i in (list):
    if(i % 2 == 0): 
        even = even + 1
    else:
         odd = odd + 1
        
print("Even no in list",even)  
print("Odd no in list",odd)