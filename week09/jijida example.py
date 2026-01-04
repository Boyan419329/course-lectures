

# 验证题目2
assert is_palindrome("racecar") == True, "题目2测试失败"
assert is_palindrome("hello") == False, "题目2测试失败"
print("✓ 题目2测试通过")

# 验证题目3
assert unique_sorted_list([3, 1, 2, 2, 1]) == [1, 2, 3], "题目3测试失败"
print("✓ 题目3测试通过")

# 验证题目4
test_text = "a a b b b c"
result = word_frequency(test_text)
assert result == {'b': 3, 'a': 2, 'c': 1}, "题目4测试失败"
print("✓ 题目4测试通过")

print("\n所有题目完成!")