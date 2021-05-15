'''
클래스에 학생의 이름을 입력하면
해당 학생이 얻은 3과목의 평균 점수에 따라 A~F의 성적을 출력하시오
해당 문제를 해결하기 위해 교재 72페이지 list 참조하세요.
'''


class Grade:
    def __init__(self, name):
        self.name = name
        self.scores = []  # list로 초기화

    def addScore(self, score):
        self.scores.append(score)

    def avg(self):
        return sum(self.scores) / len(self.scores)

    def grade(self, score):
        grade = ''

        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        elif score >= 50:
            grade = 'E'
        else:
            grade = 'F'

        return grade

    @staticmethod
    def main():
        student = Grade(input("학생 이름 : "))
        for i in ['국어', '영어', '수학']:
            student.addScore(int(input(i + "점수 : ")))

        avg = student.avg()
        grade = student.grade(avg)
        print(f'{student.name}의 평균 점수는 {avg}입니다. 즉, 성적은 {grade}입니다.')

if __name__ == '__main__':
    Grade.main()
