from titanic.models.dataset import Dataset
from titanic.models.service import Service
import pandas as pd

class Controller(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocess(train, test)
        this.label = service.create_label(this)
        this.train = service.create_train(this)
        return this


    def preprocess(self, train, test) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model(train)
        this.test = service.new_model(test)
        this.id = this.test['PassengerId']
        # print(f'트레인 드랍 전 컬럼: {this.train.columns}')
        '''
        Index(['PassengerId', 'Survived', 'Pclass', 'Name', 
        'Sex', 'Age', 'SibSp','Parch', 'Ticket', 'Fare', 'Cabin',
        'Embarked'], dtype='object')
        '''

        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        # print(f'트레인 드랍 후 컬럼: {this.train.columns}')
        '''
        Index(['PassengerId', 'Survived', 'Pclass', 'Name', 
        'Sex', 'Age', 'SibSp','Parch', 'Fare', 'Embarked'],
        dtype='object')
        '''

        this = service.embarked_nominal(this)
        this = service.title_nominal(this)
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        this = service.drop_feature(this, 'Age')
        this = service.sex_nominal(this)
        this = service.fare_ordinal(this)
        this = service.fareBand_nominal(this)
        this = service.drop_feature(this, 'Fare')
        this = service.drop_feature(this, 'SibSp')
        this = service.drop_feature(this, 'Parch')

        print(f'전처리 마감 후 컬럼: {this.train.columns}'\n)
        print(f'train의 널 수량: {this.train.isnull().sum()}\n')
        print(f'test 널 수량: {this.test.isnull().sum()}')
        '''
        전처리 마감 후 컬럼: Index(['Survived', 'Pclass', 'Sex', 'Embarked', 'Title', 'AgeGroup', 'FareBand'], dtype='object')
        train의 널 수량: Survived    0
        Pclass      0
        Sex         0
        Embarked    0
        Title       0
        AgeGroup    0
        FareBand    0
        dtype: int64
        test 널 수량: Survived    0
        Pclass      0
        Sex         0
        Embarked    0
        Title       0
        AgeGroup    0
        FareBand    0
        dtype: int64
        '''
