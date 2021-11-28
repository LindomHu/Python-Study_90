class Caculator128():
    def jia(self,a,b):
        result = a + b
        return result

    def jian(self,a,b):
        result = a - b
        return result

    def chu(self,a,b):
        if b == 0 :
            print('除数不能为\033[31;1m%r\033[0m'%b)
            return
        result = a/b
        return result
