def factorial(n):
    answer = 1
    for i in range(n):
        answer = answer * (i + 1)
    return answer
def fibonaci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonaci(n - 1) + fibonaci(n - 2) 
n = input('input N')
print(fibonaci(int(n)))

a = [4, 5, 6]
print(a)

a.append(3)
print(a)