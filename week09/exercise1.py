"""
编程练习题文件
包含4个不同的编程题目及其解答
"""

# ====== 题目1：斐波那契数列生成器 ======
print("题目1：生成斐波那契数列的前n项")


def fibonacci(n):
    """
    生成斐波那契数列的前n项
    """
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


# 测试题目1
n = 10
fib_result = fibonacci(n)
print(f"斐波那契数列前{n}项: {fib_result}")

# ====== 题目2：检查回文字符串 ======
print("\n题目2：检查字符串是否为回文")


def is_palindrome(s):
    """
    检查字符串是否为回文（忽略大小写和非字母数字字符）
    """
    # 清理字符串：只保留字母数字字符并转换为小写
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# 测试题目2
test_strings = ["racecar", "Hello", "A man, a plan, a canal: Panama"]
for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' 是否为回文: {result}")

# ====== 题目3：列表去重并排序 ======
print("\n题目3：列表去重并按升序排序")


def unique_sorted_list(lst):
    """
    去除列表中的重复元素并按升序排序
    """
    return sorted(set(lst))


# 测试题目3
sample_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_sorted = unique_sorted_list(sample_list)
print(f"原始列表: {sample_list}")
print(f"去重排序后: {unique_sorted}")

# ====== 题目4：统计单词频率 ======
print("\n题目4：统计文本中单词频率")


def word_frequency(text):
    """
    统计文本中每个单词的出现频率
    """
    # 转换为小写并分割单词
    words = text.lower().split()
    frequency = {}

    for word in words:
        # 去除标点符号
        word = word.strip('.,!?;:"\'')
        if word:
            frequency[word] = frequency.get(word, 0) + 1

    # 按频率降序排序
    return dict(sorted(frequency.items(), key=lambda x: x[1], reverse=True))


# 测试题目4
sample_text = "Hello world! Hello Python. Python is great, world is big."
freq_result = word_frequency(sample_text)
print(f"文本: '{sample_text}'")
print("单词频率统计:")
for word, count in freq_result.items():
    print(f"  {word}: {count}次")

