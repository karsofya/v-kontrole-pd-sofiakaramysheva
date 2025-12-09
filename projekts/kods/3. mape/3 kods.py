fibonacci = [0, 1]
while len(fibonacci) < 100:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
for num in reversed(fibonacci):
    print(num, end=' ') 



