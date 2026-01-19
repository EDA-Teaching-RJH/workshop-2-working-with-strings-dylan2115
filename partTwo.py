import math  

def main(): 
    a = int(input("what is a? "))
    b = int(input("what is b? "))
    
    pythag(a,b)
def pythag(a,b):
     
    sa = a**2
    sb = b**2
    c = math.sqrt(sa + sb)
    print(c) 

main()
