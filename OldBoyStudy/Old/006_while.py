 # Author:LindomHui
 # coding=---UTF-8---


user_choice = input("请输入钱数：")
while True:
    if user_choice.isdigit():
        n = int(user_choice)
        print(n,"个苹果")
        if user_choice == "np":
            m =int(user_choice)
            y = m/2
            print(y,"个苹果")
        break

