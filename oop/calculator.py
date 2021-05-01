class Calculator:
    def __init__(self, first, second):      #private
        self.first = first
        self.second = second

    def sum(self):                          #public
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    def mod(self):
        return self.first % self.second

    @staticmethod                           #decorator (메소드의 기능 정의)
    def execute():                          #staticmethod에는 self x
        #calc = Calculator(6, 2)
        calc = Calculator(int(input("첫번째 수 : ")), int(input("두번째 수 : ")))

        print(f'첫번째 수 = {calc.first}\n두번째 수 = {calc.second}')
        print(f'{calc.first} + {calc.second} = {calc.sum()}')   #외부에서 호출 시 def의 self는 기입 x
        print(f'{calc.first} - {calc.second} = {calc.sub()}')
        print(f'{calc.first} * {calc.second} = {calc.mul()}')
        print(f'{calc.first} / {calc.second} = {calc.div()}')
        print(f'{calc.first} % {calc.second} = {calc.mod()}')

if __name__ == '__main__':
    Calculator.execute()