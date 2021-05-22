import mglearn
import matplotlib.pyplot as plt
import numpy as np
from mglearn.datasets import make_wave
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor

class GreenStar(object):
    x, y = make_wave(n_samples=40)  # mglearn의 데이터셋 중 make_wave 에서 가져오는 샘플의 수이다.
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.3)

    def __init__(self):
        self._neighbors = 0  # 가장 가까운 이웃의 갯수이다. 예제에서는 3을 사용한다.
        self._jobs = 0  # 사용할 코어의 수이다. -1 이면 모든 코어 사용한다.

    @property
    def neighbors(self) -> 0:
        return self._neighbors

    @neighbors.setter
    def neighbors(self, neighbors):
        self._neighbors = neighbors

    @property
    def jobs(self) -> 0:
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        self._jobs = jobs

    def get_knn_reg_score(self):
        knn_reg = KNeighborsRegressor(n_neighbors=self.neighbors, n_jobs=self.jobs)  # 3, -1
        knn_reg.fit(self.x_train, self.y_train)
        return knn_reg.score(self.x_test, self.y_test)

    def plot_knn_reg(self):
        _, axes = plt.subplots(1, 3)  # 언더바 쉼표 입니다
        xtrain = self.x_train
        xtest = self.x_test
        ytrain = self.y_train
        ytest = self.y_test
        line = np.linspace(-5, 5, num=1000)
        line = line.reshape(-1, 1)
        for i, ax in zip([1, 3, 9], axes.ravel()):
            knn_reg = KNeighborsRegressor(n_neighbors=i, n_jobs=-1)
            knn_reg.fit(xtrain, ytrain)
            prediction = knn_reg.predict(line)
            ax.plot(line, prediction, label='model predict', c='k')
            ax.scatter(xtrain, ytrain, marker='^', c='darkred', label='train target')
            ax.scatter(xtest, ytest, marker='v', c='darkblue', label='test target')
            train_score = knn_reg.score(xtrain, ytrain)
            test_score = knn_reg.score(xtest, ytest)
            ax.set_title('k={}\n test score={:.3f}\n train score={:.3f}'.format(i, train_score, test_score))
            ax.set_xlabel('feature')
            ax.set_ylabel('target')
        axes[0].legend(loc=2)
        plt.show()

    @staticmethod
    def main():
        knn = GreenStar()
        while 1:
            menu = input('------------\n0.Exit\n 1.Plot\n 2.Score\n메뉴입력 : ')
            if menu == '0':
                break
            elif menu == '1':
                knn.neighbors = int(input('Please Enter a Neighbors Value.'))
                mglearn.plots.plot_knn_regression(n_neighbors=knn.neighbors)
                plt.show()
            elif menu == '2':
                knn.neighbors = int(input('Please Enter a Neighbors Value.'))
                knn.jobs = int(input('Please Enter a Jobs Value.'))
                score = knn.get_knn_reg_score()
                print("{:.3f}".format(score))  # 0.697
            elif menu == '3':
                knn.plot_knn_reg()
            else:
                print('Wrong Number. Enter Another Number')


GreenStar.main()