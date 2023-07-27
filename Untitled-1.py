def fibonacci(n):
    fib_sequence = [0, 1]  # 斐波那契数列的初始前两个数字
    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]  # 计算下一个斐波那契数
        fib_sequence.append(next_number)
    return fib_sequence

# 输入一个正整数来确定要生成的斐波那契数列的长度
n = int(input("请输入斐波那契数列的长度: "))

# 生成并打印斐波那契数列
fib = fibonacci(n)
print(fib)

