import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


class BreastCancer(object):

    cancer = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        cancer.data, cancer.target, stratify=cancer.target, random_state=42
    )

    tree = DecisionTreeClassifier(random_state=0)

    def train(self):
        tree = self.tree
        xtrain = self.X_train
        ytrain = self.y_train

        tree.fit(xtrain, ytrain)

        return tree

    @staticmethod
    def main():
        bc = BreastCancer()
        tree = bc.train()
        xtrain = bc.X_train
        ytrain = bc.y_train
        xtest = bc.X_test
        ytest = bc.y_test
        print('훈련세트의 정확도: {:.3f}'.format(tree.score(xtrain, ytrain)))
        print('테스트의 정확도: {:.3f}'.format(tree.score(xtest, ytest)))


BreastCancer.main()

"""
표본내 성능검증(in-sample testing) : 회귀분석 성능은 학습데이터 집합의 종속변수(y) 값의 예측 정확도를 
               결정계수(coefficient of determination)등을 이용하여 따지는 검증
표본외 성능검증(out-of-sample testing) 혹은 교차검증(cross validation) :
회귀분석 모형을 만드는 목적 중 하나는 종속변수의 값을 아직 알지 못하고 따라서 학습에 
사용하지 않은 표본에 대한 종속 변수의 값을 알아내고자 하는 것 즉 예측(prediction) 이다.
이렇게 학습에 쓰이지 않는 표본 데이터 집합의 종속변수값을 얼마나 잘 예측하는가를 검사하는 것
data : 독립 변수 데이터 배열 또는 pandas 데이터프레임
data2 : 종속변수 데이터. data 인수에 종속 변수 데이터가 같이 있으면 생략할 수 있다
test_size : 검증용 데이터 갯수. 1보다 작은 실수이면 비율을 나타낸다
train_zise : 학습용 데이터 갯수. 1보다 작은 실수이면 비율을 나타낸다. test_size 와 train_size 는 하나만 있어도 된다
random_state : 난수 시드 (계속 동일한 난수가 생성되도록 함)
독립변수의 개수가 많은 빅데이터에서는 과최적화가 쉽게 발생한다.
"""