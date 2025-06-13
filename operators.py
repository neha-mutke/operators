num1=22
num2=21

f1 = 20.3
f2 = 12.8

str1 = "jay"
str2 = "viru"

list1 = [20,49,57,"sai"]
# print(type(list1))
list2 = [79,"fhj",89,90]

t2 = (23,2,3,4)
t1 = (20,50,30,"viru")

complex1 = 4+6j
complex2 = 3+2j

s1=set()
s1.add("sai")
s1.add(1)
s1.add(4)
# print(type(s1),s1)
s2 = set()
s2.add(6)
s2.add(5)
# print(type(s2),s2)

##addion operator

print("addition of two num :-",num1 + num2) #addition of two integers 
print("addition of two float values :- ",f1 + f2)  
print("addition of two string := ",str1 + str2)
print("addition of two list:- ",list1 + list2)
print("addition of two tuple :- ",t1+t2)
print("addition of two complx numpers :- ",complex1+complex2)
print("addition of two set:- ",s1+s2)  # unsupported operand type(s) for +: 'set' and 'set'

print("addion of num and float :-",num1+f1) #42.3
print("addion of num and string :-",num2+str1) #unsupported operand type(s) for +: 'int' and 'str'
print("addion of num and list :- ",num2+list1) #unsupported operand type(s) for +: 'int' and 'list'
print("addion of num and tuple :-",num2+t1) #unsupported operand type(s) for +: 'int' and 'tuple'
print("addion of num and complex num :- ",num1+complex1) #(26+6j)
print("addion of num and set := ",num1+s1) #unsupported operand type(s) for +: 'int' and 'set'
      
print("addition of floating value and string :-",f1+str1) #not supoorted
print("addition of floating value and list :-",f1+list1)   #not supoorted
print("addition of floating value and tuple:- ",f1+t1)     #not supoorted
print("addition of floating value and complex num :- ",f1+complex1) #(24.3+6j)
print("addition of floating value and set :-",f1+s1)    #not supoorted

print("addion of string and list :-",str1+list1) #not supoorted
print("addion of string and tuple :-",str1+t1)    #not supoorted
print("addion of string and complex num:- ",str1+complex1)    #not supoorted
print("addion of string and set :-",str1+s1)  #not supoorted

print("addion of list and tuple:-",list2+t1) #not supoorted
print("addion of list and complex num:-",list1+complex1) #not supoorted
print("addion of list and set:-",list1+s1) #not supoorted

#substraction operator

print("substraction of two num :-",num1 - num2) #addition of two integers 
print("substractio of two float values :- ",f1 - f2)  
print("substractio of two string := ",str1 - str2)
print("substractio of two list:- ",list1 - list2)
print("substractio of two tuple :- ",t1-t2)
print("substractio of two complx numpers :- ",complex1-complex2)
print("substractio of two set:- ",s1-s2)

print("substraction of num and float :-",num1-f1) 
print("substraction of num and string :-",num2-str1) 
print("substraction of num and list :- ",num2-list1) 
print("substraction of num and tuple :-",num2-t1) 
print("substraction of num and complex num :- ",num1-complex1) 
print("substraction of num and set := ",num1-s1)


print("substraction of floating value and string :-",f1-str1) #not supoorted
print("substraction of floating value and list :-",f1-list1)   #not supoorted
print("substraction of floating value and tuple:- ",f1-t1)     #not supoorted
print("substraction of floating value and complex num :- ",f1-complex1) #(24.3+6j)
print("substraction of floating value and set :-",f1-s1)

print("substraction of string and list :-",str1-list1) #not supoorted
print("substraction of string and tuple :-",str1-t1)    #not supoorted
print("substraction of string and complex num:- ",str1-complex1)    #not supoorted
print("substraction of string and set :-",str1-s1)  #not supoorted

print("substraction of list and tuple:-",list2-t1) #not supoorted
print("substraction of list and complex num:-",list1-complex1) #not supoorted
print("substraction of list and set:-",list1-s1) #not supoorted

#multipication operator

print("multiplication of two num :-",num1 * num2)  
print("multiplication  of two float values :- ",f1 * f2)  
print("multiplication  of two string := ",str1 * str2) #not supported
print("multiplication  of two list:- ",list1 * list2) #not supported
print("multiplication  of two tuple :- ",t1*t2) #not supported
print("multiplication  of two complx numpers :- ",complex1*complex2)
print("multiplication  of two set:- ",s1*s2)  #not supported 

print("multiplication  of num and float :-",num1*f1) 
print("multiplication  of num and string :-",num2*str1) 
print("multiplication  of num and list :- ",num2*list1) #not supported
print("multiplication of num and tuple :-",num2*t1)    #not supported 
print("multiplication  of num and complex num :- ",num1*complex1) 
print("multiplication  of num and set := ",num1*s1)  #not supported


print("multiplication of floating value and string :-",f1*str1) #not supoorted
print("multiplication  of floating value and list :-",f1*list1)   #not supoorted
print("multiplication  of floating value and tuple:- ",f1*t1)     #not supoorted
print("multiplication  of floating value and complex num :- ",f1*complex1) 
print("multiplication  of floating value and set :-",f1*s1) #not supoorted

print("multiplication  of string and list :-",str1*list1) #not supoorted
print("multiplication  of string and tuple :-",str1*t1)    #not supoorted
print("multiplication  of string and complex num:- ",str1*complex1)    #not supoorted
print("multiplication  of string and set :-",str1*s1)  #not supoorted

print("multiplication  of list and tuple:-",list2*t1) #not supoorted
print("multiplication  of list and complex num:-",list1*complex1) #not supoorted
print("multiplication  of list and set:-",list1*s1) #not supoorted



