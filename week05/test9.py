# 模拟取款机，设置一个变量用来表示你的余额，通过键盘输入接收一个取款金额，判断是否满足取款条件
#余额
s
balance= 5000

# 接收取款金额
money = int(input("请输入取款金额: "))

if money <= balance:      
     print ("正在准备中，请稍后...")          
else:    
     print ("余额不足，挣钱去吧...")
