def fibonacci(n):
    fib_sequence = [0, 1]  # 初始化斐波那契数列
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]  # 计算下一个斐波那契数
        fib_sequence.append(next_fib)  # 添加到序列中
    return fib_sequence

# 输出前 8 个斐波那契数
n = 8
print(fibonacci(n))