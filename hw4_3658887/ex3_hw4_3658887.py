import numpy as np
import scipy.special
import cmath

def full(stack):
    """
    prints entire stack
    """
    try:
        for i in range(len(stack)-1):
            print(stack[i])
    except:
        print('error')

def swap(stack):
    """
    swaps last two entries in the stack
    """
    try:
        stack_copy = stack[:]
        stack[-2] = stack_copy[-1]
        stack[-1] = stack_copy[-2]
    except:
        print('not enough entries')
    return stack

def copy(stack):
    """
    copies the last entry in the stack
    """
    try:
        return stack[-1]
    except:
        print('error')

def paste(data):
    """
    prints out the copy but does not add it to the stack
    """
    try:
        print(data)
    except:
        print('error')

def clear():
   return []
#######################Splitting data for binary operations
def binary_op_data(stack):
   try:
       return stack[0:-2], stack[-2], stack[-1]
   ## If not enough data, do nothing
   except:
       return stack

#############################################
######################Binary operations#########
#############################################
def add(a,b):
   return a+b

def substract(a,b):
   return a-b

def multiply(a,b):
   return a*b

def divide(a,b):
    try:
        return a/b
    except:
        print("tried to divide by zero. Returning last value")
        return b

def exp2(a,b):
    """
    a^b
    """
    try:
        return a**b
    except:
        print('error. Returning last value')
        return b

def log2(a,b):
    """
    log(a) with base b
    """
    try:
        return np.log(a) / np.log(b)
    except:
        print('tried to take log of negative value. Returning last value')
        return b

#############################################
#########################unary operations
#########################################
def sin(a):
  return np.sin(a)

def cos(a):
  return np.cos(a)

def tan(a):
  return np.tan(a)

def log(a):
    try:
        return np.log(a)
    except:
        print('error')

def log10(a):
    try:
        return np.log10(a)
    except:
        print('error')

def exp(a):
    try:
        return np.exp(a)
    except:
        print('error')

def sqrt(a):
    try:
        return np.sqrt(a)
    except:
        print('error')

def inv(a):
    try:
        return 1/a
    except:
        print('error')

def cosh(a):
    try:
        return np.cosh(a)
    except:
        print('error')

def sinh(a):
    try:
        return np.sinh(a)
    except:
        print('error')

def tanh(a):
    try:
        return np.tanh(a)
    except:
        print('error')

def gamma(a):
    try:
        return scipy.special.gamma(a)
    except:
        print('error')

def conj(a):
    try:
        return np.conj(a)
    except:
        print('error')

def arcsin(a):
    try:
        return np.arcsin(a)
    except:
        print('error')

def arccos(a):
    try:
        return np.arccos(a)
    except:
        print('error')

def arctan(a):
    try:
        return np.arctan(a)
    except:
        print('error')

def arcsinh(a):
    try:
        return np.arcsinh(a)
    except:
        print('error')

def arccosh(a):
    try:
        return np.arccosh(a)
    except:
        print('error')

def arctanh(a):
    try:
        return np.arctanh(a)
    except:
        print('error')

###########################This is the update of the stack: the heart of the calculator
def input_next(stack, temp_copy):
    next= input()
    
    try:
        if next == 'e':
            next = np.e
        if next == 'pi':
            next = np.pi
    except:
        pass
    
    #################### Check if number
    try:
       stack+=[complex(next)]
    except:
       pass
####################### Check if known unary (one argument) or binary  (two argument) operations
    try:
        if next in unaryops:
            if cmath.isnan(unaryops[next](stack[-1])) == False and cmath.isinf(unaryops[next](stack[-1])) == False:
                stack[-1]=unaryops[next](stack[-1])
            else:
                print('error')
        if next in binaryops:
            #    print(next) #########Used for debugging
            ######################### When we call this function, if stack too short, will reurn wrong list of parameters and cause an exception
            stack, a, b= binary_op_data(stack)
            u=binaryops[next](a, b)
            if cmath.isnan(u) == False and cmath.isinf(u) == False:
                stack=stack+[u]
            else:
                print('error')
    except:
         pass
    
    if next == 'full':
        full(stack)
        
    if next == 'swap':
        swap(stack)
    
    if next == 'copy':
        temp_copy = copy(stack)

    if next == 'paste':
        try:
            paste(temp_copy)
        except:
            print('error')
        
####################Clear stack condition
    if next=='clear':
       stack= clear()

################### Quit program
    if next=='quit':
        exit()

#################### help: list implemented fucntions
    if next=="help":
        print(list(binaryops.keys()), list(unaryops.keys()), "full, swap, copy, paste, clear, quit")

##################### Return the stack and exit function
    return stack, temp_copy







####################This is the main program: the rest are functions

print("This is an easy reverse polish notation calculator. Enter help for help")

binaryops={'+': add, '-':substract, '*': multiply ,'/':divide, 'exp2':exp2, 'log2':log2}
unaryops={'sin':sin, 'cos':cos, 'tan':tan, 'log':log, 'log10':log10, 'exp':exp, 'sqrt':sqrt, 'inv':inv, 'cosh':cosh, 'sinh':sinh, 'tanh':tanh, 'gamma':gamma, 'conj':conj, 'arcsin':arcsin, 'arccos':arccos, 'arctan':arctan, 'arcsinh':arcsinh, 'arccosh':arccosh, 'arctanh':arctanh}

stack=[]
temp_copy = 'error'

while  True:
    ################Update
    stack, temp_copy =input_next(stack, temp_copy)
   ##################Print last number (like in normal calculators).
    try:
        print(stack[-1])
   ####################UNless the memory is clear
    except:
        print("Stack empty")

