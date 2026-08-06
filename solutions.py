# Check if a number is positive, negative, or zero.
# num=int(input("enter n:"))
# print("positive") if num>0 else print ("negative or zero")



# check if even or odd 
# num=int(input("enter n:"))
# print("even") if num%2==0 else print("odd")


# find greater of two numbers
# num1=int(input("enter n:"))
# num2=int(input("enter n:"))
# print("num1 is greater") if num1>num2 else print("num2 is greater")




# find larger among 3 numbers
# num1=int(input("enter n:"))
# num2=int(input("enter n:"))
# num3=int(input("enter n:"))
# if num1>num2 and num1 >num3:
#     print("num1 is greater")
# elif(num2>num3 and num2>num1):
#     print("num2 is greater")
# else:
#     print("num3 is greater")



# check leap year
# num=int(input("enter n:"))
# print("leap year")if num%4==0 and num%1000!=0 or num%400==0 else print("not a leap year ")




# check vowel and consonent
# vowel='a','e','i','o','u'
# char=input("enter char:")
# print("it is vowel")if char in vowel else print("it is consonant")


# check if number is divisible by 5 and 11
# num=int(input("Enter num:"))
# print("it is divisible by both") if num%5==0 and num%11==0 else print("it is not divisible by both")






# check the age eligiblity for vote
# age=int(input("enter age:"))
# print("eligible") if age>=18 else print("not eligible")





# grade calculator
# marks=input("enter marks:")
# match marks//10:
#     case 10:
#         print("A++")
#     case 9:
#         print("A")
#     case 8:
#         print("B++") 
#     case 7:
#         print("B") 
#     case 6:
#         print("C++") 
#     case 5:
#         print("C") 
#     case _:
#         print("F") 



# electricity bill calculator
# unit=int(input("enter unit:"))
# if 0<unit<100:
#     print(unit*3)
# elif(100<unit<200):
#     print(unit*5)
# elif(unit>=200):
#     print(unit*7)
# else:
#     print("invald output")



# income tax generator
# payment=int(input("enter payment:"))
# if payment<=300000:
#     tax=0
# elif(300000<payment<800000):
#     tax=(payment-50000)*0.5
# elif(payment>800000):
#     tax=(payment-100000)*0.10
# else:
#     print("invalid input")




# simple calculator
# n1=int(input("Enter n:"))
# n2=int(input("Enter n:"))
# op=input("enter oprator:")
# match op:
#     case "+":
#         print(n1+n2)
#     case "-":
#         print(n1-n2)
#     case "*":
#         print(n1*n2)
#     case "/":
#         print(n1/n2)
#     case _:
#         print("invalid oprator")



# # ATM withdrawal
# pin1=1234
# pin=int(input("enter pin:"))
# if pin==pin1:
#     print("pin matched")
# else:
#     print("try again! ")
# amt=int(input("enter amount:"))
# if amt>=500:
#     print("recieved amount",amt)
# else:
#     print("atleast 500 , try diffrent account",amt)




# login system
# password_set=191984
# ph_num=int(input("enter phone number:"))
# password=int(input("enter password:"))
# if password==password_set:
#     print("unlocked")
# else:
#     print("not matched try again!")




# chessboard square colour
# coord = input("Enter coordinate: ")

# column = coord[0]      
# row = int(coord[1])    

# if column == 'a' or column == 'c' or column == 'e' or column == 'g':
#     if row == 2 or row == 4 or row == 6 or row == 8:
#         print("White")
#     else:
#         print("Black")

# elif column == 'b' or column == 'd' or column == 'f' or column == 'h':
#     if row == 1 or row == 3 or row == 5 or row == 7:
#         print("White")
#     else:
#         print("Black")

# else:
#     print("Invalid input")



# # rock paper scissor
# player1=input("enter :")
# player2=input("enter :")
# if player1=="paper" and player2=="rock":
#     print("player1 wins!!")
# elif( player1=="rock" and player2=="paper"):
#     print("player2 wins!!")
# elif(player1=="scissors" and player2=="paper"):
#     print("player1 wins!!")
# elif(player1=="paper" and player2=="scissors"):
#     print("player2 wins!!")
# elif(player1=="rock" and player2=="scissors"):
#     print("player1 wins!!")
# elif(player1=="scissors" and player2=="rock"):
#     print("player2 wins!!")
# else:
#     print("invalid command")




# print reverse of a number 
# num=int(input("enter  num:"))
# rev=0
# for i in range(1,len(str(num))+1):
#     digit=num%10
#     rev=rev*10 + digit
#     num//=10
# print(rev)



# #sum of odd number
# n=int(input("enter n:"))
# total=0
# for i in range(1,n+1):
#     if i%2!=0:
#         total+=i
#         n//=10
# print(total)


# # count no of  digit
# n=int(input("enter n:"))
# count=0
# for i in range(1,len(str(n))+1):
#     count+=1
# print(count)




# # armstrong number 
# n=int(input("enter n:"))
# sum=0
# b=len(str(n))
# for i in range(1,b+1):
#     digit=n%10
#     sum+=digit**b
#     n//=10
# print(sum)



# strong number 
# n=int(input("enter n:"))

# sum=0
# for i in range(1,len(str(n))+1):
#     digit=n%10
#     fact=1
#     for j in range(1,digit+1):
#         fact*=j
#     sum+=fact
#     n//=10
# print(sum)





# # perfect number 
# n=int(input("enter n:"))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# if n==sum:
#     print("strong number")
# else:
#     print("not")





# # factorial of a number
# fact=1
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     fact*=i
# print(fact)





# # fibonacci series
# n=int(input("enter n:"))
# a,b=0,1
# for i in range(1,n+1):
#     print(a)
#     a,b=b,a+b


# # prime number 
# n=int(input("enter n:"))
# if n<1:
#     print("not prime")
# else:
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")


# gcd
# rem=0
# n1=int(input("enter n:"))
# n2=int(input("enter n:"))
# for i in range(len(str(n2))):
#     rem=n1%n2
#     n1=n2
#     n2=rem
# print(n2)





# # count vowels 
# count=0
# char=input("enter char:")
# vowel='a','e','i','o','u'
# for ch in char:
#     if ch in vowel:   
    
#         count+=1
# print(count)






# # count vowels 
# count=0
# char=input("enter char:")
# vowel='a','e','i','o','u'
# for ch in char:
#     if ch in vowel:   
    
#         count+=1
# print(count)







# # print fibonacci series
# n=int(input("enter n:"))
# a,b=0,1
# for i in range(1,n+1):
#     print(a)
#     a,b=b,a+b



# # count digits
# n=int(input("enter n:"))
# count=0
# b=len(str(n))
# for i in range(1,b+1):
#     n//=10
#     count+=1
# print(count)    




# # sum of digit
# n=int(input("enter n:"))
# total=0
# for i in range(1,n+1):
#     digit=n%10
#     total+=digit
#     n//=10
# print(total)




# # strong number 
# n=int(input("enter n:"))
# sum=0
# temp=n
# for i in range(1,len(str(n))+1):
#     digit=temp%10
#     fact=1
#     for j in range(1,digit+1):
#         fact*=j
#     sum+=fact
#     temp//=10
# if sum==n:
#     print("perfect number")
# else:
#     print("not")


# # perfect number 
# n=int(input("enter n:"))
# temp=n
# sum=0
# for i in range(1,n):
#     if temp%i==0:
#         sum+=i
# if sum==n:
#     print("perfect number")
# else:
#     print("not")


# # automorphic number
# n=int(input("enter n:"))
# temp=n
# sq=n**2
# for i in range(1,sq+1):
#     digit=sq%10
# if digit==n:
#     print("automorphic number")
# else:
#     print("not")



# # harshada number 
# n=int(input("enter n:"))
# temp=n
# sum=0
# for i in range(1,n+1):
#     digit=temp%10
#     sum+=digit
#     temp//=10
# if n%sum==0:
#     print("harshada number")
# else:
#     print("not")



# # neon number
# n=int(input("enter number"))
# sq=n**2
# sum=0
# b=len(str(sq))
# for i in range(1,b+1):
#     digit=sq%10
#     sum+=digit
#     sq//=10
# if sum==n:
#     print("it is neon number")
# else:
#     print("not ")



# # prime number
# n=int(input("enter n:"))
# if n<=1:
#     print("not prime")
# else:
#     for i in range(2,(int(n**0.5)+1)):
#         if n%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime nmuber")



# # n prime numbers
# n=int(input("enter n:"))
# for num in range(1,n+1):
#     if num<=1:
#         print("not prime")
#     else:
#         for j in range(2,int(n**0.5)+1):
#             if num%j==0:
#                 print(num,"not prime")
#                 break
#         else:
#             print(num,"prime")




# # twin prime
# n1=int(input("enter n1:"))
# n2=int(input("enter n2:"))
# if n1<=1 and n2<=1:
#     print("not prime")
# else:
#     for i in range(2,int(n1**0.5)+1) and (2,int(n2**0.5)+1):
#         if n1%i==0 and n2%i==0:
#             print("not prime")
#     else:
#         if n1-n2==2:
#             print(n1,n2,"twin prime")
#         else:
#             print(n1,n2,"not a twin prime")



# # prime factors
# n=int(input("Enter n:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
#     for j in range(2,(int(i**0.5)+1)):
#         if j%i==0:
#             print("not a prime factor")
#     else:
#         print("it is prime  factors")






# functions 



# function to add
# def main():
#     n1=int(input("enter n:"))
#     n2=int(input("enter n:"))
#     print(add(n1,n2))
# def add(x,y):
#     return x+y
# if __name__=="__main__":
#     main()


# # function to subtract
# def main():
#     n1,n2=int(input("Enter n1:")),int(input("Enter n2:"))
#     sub(n1,n2)
# def sub(x,y):
#     return x-y
# if __name__=="__main__":
#     main()



# # even odd 
# def main():
#     n=int(input("enter n:"))
#     print(even_odd(n))
# def even_odd(x):
#     return "even" if x%2==0 else "odd"
# if __name__=="__main__":
#     main()


# # function to check factorial
# def main():
#     n=int(input("enter n:"))
#     print(fact(n))
# def fact(x):
#     fact=1
#     for i in range(1,x+1):
#         fact*=i
#     return fact
# if __name__=="__main__":
#     main()




# # strings



# find string length
# n=input("enter n:")
# print(len(n))


# # reverse string
# n=input("enter n:")
# print(n[::-1])


# # palindrome
# n=input("enter n:")
# if n[::-1]==n:
#     print("it is a palindrome")
# else:
#     print("not")




# palindrome
n=input("enter n:")
if n[::-1]==n:
    print("it is a palindrome")
else:
    print("not")



