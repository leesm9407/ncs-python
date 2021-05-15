'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제
'''
class Contacts:

    # __init__을 간소화한 형식 => 간소화된 객체지향 구조 (getter/setter 간소화)
    name = ''
    phone = ''
    email = ''
    address = ''

    # string 메소드 간소화
    def __str__(self):
        return  f'이름 : {self.name}\n' \
                f'전화번호 : {self.phone}' \
                f'이메일 : {self.email}' \
                f'주소 : {self.address}'


class ContactsService:

    def set_contact(self):
        obj = Contacts
        obj.name = input("이름 : ")
        obj.phone = input("전화번호 : ")
        obj.email = input("이메일 : ")
        obj.address = input("주소 : ")
        return obj

    def get_content(self, ls):
        print(f'\n===연락처 목록===\n----------')
        for i in ls:
            print(i)    # Contacts의 __str__을 정의함으로써 기본 print로 사용
            print(f'----------')
        print(f'===============\n')

    def del_contact(self, ls, name):
        for i, t in enumerate(ls):  # i = index, t = element (리스트 내부의 주소)
            if t.name == name:
                del ls[i]

    def print_menu(self):
        print("<< 연락처 메뉴>>\n1. 연락처 입력\n2. 연락처 출력\n3. 연락처 삭제\n4. 종료")

        menu = input("   >> 메뉴 선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        service = ContactsService

        while 1:  # 1은 true => 무한루프 => 4번 누르기 전까지 프로그램을 실행
            menu = service.print_menu()

            if menu == 1:
                t = service.set_contact()
                ls.append(t)
            elif menu == 2:
                service.get_content(ls)
            elif menu == 3:
                service.del_contact(ls, input("   >> 삭제할 이름 : "))
                print()
            elif menu == 4:
                break

if __name__ == '__main__':
    ContactsService.main()