import random
random.seed(0)

signal = [random.randint(1,25) for i in range(10)]
print(signal)

#lambda function is used with map(lambda_function, list) and filter(lambda_functioon, list)
#syntax: lambda argument: Expression

odd = filter(lambda x: x%2==1,signal)
even = filter(lambda x: x%2==0, signal)

print(f"The Odd numbers are: {list(odd)}")
print(f"The Even numbers are: {list(even)}")

squares = map(lambda x: x**2, signal)
print(f"Squares are: ", list(squares))