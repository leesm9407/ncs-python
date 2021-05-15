'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제
'''
class Contacts:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def print_info(self):
        print(f'이름 : {self.name}')
        print(f'전화번호 : {self.phone}')
        print(f'이메일 : {self.email}')
        print(f'주소 : {self.address}')

    @staticmethod
    def set_contact():
        name = input("이름 : ")
        phone = input("전화번호 : ")
        email = input("이메일 : ")
        address = input("주소 : ")
        return Contacts(name, phone, email, address)

    @staticmethod
    def get_content(ls):
        print(f'\n===연락처 목록===\n----------')
        for i in ls:
            i.print_info()
            print(f'----------')
        print(f'===============\n')

    @staticmethod
    def del_contact(ls, name):
        for i, t in enumerate(ls):      # i = index, t = element (리스트 내부의 주소)
            if t.name == name:
                del ls[i]

    @staticmethod
    def print_menu():
        print("<< 연락처 메뉴>>")
        print("1. 연락처 입력")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")

        menu = input("   >> 메뉴 선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while 1:                            # 1은 true => 무한루프 => 4번 누르기 전까지 프로그램을 실행
            menu = Contacts.print_menu()

            if menu == 1:
                t = Contacts.set_contact()
                ls.append(t)
            elif menu == 2:
                Contacts.get_content(ls)
            elif menu == 3:
                Contacts.del_contact(ls, input("   >> 삭제할 이름 : "))
                print()
            elif menu == 4:
                break

if __name__ == '__main__':
    Contacts.main()