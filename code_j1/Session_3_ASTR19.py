#session 3 prompt ASTR_19

#Write a Python program that defines a function f(x)
#that returns x**3 + 8. In the main function of the program,
#call f(x) with x = 9 and print the result.
#Use an if statement that executes if the result is larger
#than 27 and prints “YAY!”.

def main(x):

    def f(x):
        return (x**3 + 8)
    
    print(f(x))
        
    if f(x) >= 27:
        print("YAY!")
    
    

if __name__=="__main__":

  main(9)


