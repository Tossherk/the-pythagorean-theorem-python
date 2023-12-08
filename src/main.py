from triangles import *

print("Choose what do you want to do: ")
print("1. Calculate the hypotenuse")
print("2. Calculate the adjoining A")
print("3. Calculate the adjoining B")

choice = input("Enter your choice (1/2/3):")

if choice == '1':
             a = float(input("enter A : "))
             b = float(input("enter B : "))
             print (a, "+", b, "=", Hypotenuse(a, b))
                 
elif choice == '2':
        c = float(input("enter C : "))
        b = float(input("enter B :"))
        
        print(c,"-", b, "=", AdjoiningA(c,b))
    
elif choice == '3':
        c = float(input("enter C : "))
        a = float(input("enter A :"))
        
        print (c,"-", a, "=", AdjoiningB(c,a)) 