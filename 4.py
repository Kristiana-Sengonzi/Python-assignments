
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
     if b == 0:
        return "Cannot divide by zero"
     
     return a/b
def get_number(prompt):
   while True:
      try:
         return float(input(prompt))
      except ValueError:
         print("Please enter a valid number")

def main():
    options=["1","2","3","4","5"]
    while True:
     print('Welcome to simple calculator ')
     print('Below are the options')
     print("1.Add")
     print("2.Subtract")
     print("3.Multiply")
     print("4.Divide")
     print("5.Exit calculator")
     selection=input("Select one of the options to proceed")
 
     if (selection in options):
          if selection =="5":
             print("Exiting calculator.....")
             break
          a=get_number("Enter first operand")
        
          b=get_number("Enter second operand")
        
        
          if selection =="1":
             print("Answer =",add(a=a,b=b))
             continue
          elif selection =="2":
             print("Answer =",subtract(a=a,b=b))
             continue
          elif selection =="3":
             print("Answer =",multiply(a=a,b=b))
             continue
          elif selection =="4":
             print("Answer =",divide(a=a,b=b))
             continue
          
     else:
         print("Invalid input.Select Again") 
         continue
        
if __name__=="__main__":
   main()
   
        
           



