class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'안녕하세요. 제 이름은 {self.name}이고, '
              f'나이는 {self.age}살이며, '
              f'{self.address}에 삽니다.')

    @staticmethod
    def main():
        maria = Person('마리아', 20, '서울')         # maria, tom : 객체 => 재활용성
        maria.greeting()

        tom = Person('톰', 22, '인천')
        tom.greeting()

if __name__ == '__main__':
    Person.main()